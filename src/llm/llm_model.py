import asyncio
from openai import APIConnectionError, APIStatusError, APITimeoutError, AsyncOpenAI, OpenAIError, RateLimitError
from pydantic import BaseModel, Field


class LLMResponseError(RuntimeError):
    """Raised when an OpenAI-compatible provider response has invalid shape."""


class ChatCompletionsUsage(BaseModel):
    prompt: int = Field(...)
    completion: int = Field(...)
    total: int = Field(...)

class ChatCompletions(BaseModel):
    content: str = Field(...)
    usage: ChatCompletionsUsage = Field(...)


class LLM:
    def __init__(
            self, 
            model_name: str, 
            base_url: str, 
            api_key: str = "no-key",
            batch_size: int = 4
        ):
        self.model_name = model_name
        self._semaphore = asyncio.Semaphore(batch_size)
        self._client = AsyncOpenAI(
            api_key  = api_key,
            base_url = base_url,
        )

    def _short_repr(self, value, *, max_chars: int = 800) -> str:
        text = repr(value)
        if len(text) > max_chars:
            return text[:max_chars] + "...<truncated>"
        return text

    def _visible_attrs(self, obj, *, max_chars: int = 1200) -> str:
        if obj is None:
            return "None"
        if hasattr(obj, "model_dump"):
            try:
                return self._short_repr(obj.model_dump(exclude_none=False), max_chars=max_chars)
            except Exception:
                pass
        attrs: dict[str, object] = {}
        for name in dir(obj):
            if name.startswith("_"):
                continue
            try:
                value = getattr(obj, name)
            except Exception:
                continue
            if callable(value):
                continue
            if name in {"content", "refusal", "tool_calls", "role", "function_call", "reasoning_content", "reasoning"}:
                attrs[name] = value
        return self._short_repr(attrs or obj, max_chars=max_chars)

    def _build_response_context(self, response, choice=None) -> str:
        context_parts = [f"model={self.model_name!r}"]
        response_id = getattr(response, "id", None)
        if response_id:
            context_parts.append(f"response_id={response_id!r}")
        response_model = getattr(response, "model", None)
        if response_model:
            context_parts.append(f"response_model={response_model!r}")
        if choice is not None:
            finish_reason = getattr(choice, "finish_reason", None)
            if finish_reason:
                context_parts.append(f"finish_reason={finish_reason!r}")
            message = getattr(choice, "message", None)
            if message is not None:
                content = getattr(message, "content", None)
                context_parts.append(f"message.content={self._short_repr(content, max_chars=300)}")
                tool_calls = getattr(message, "tool_calls", None)
                refusal = getattr(message, "refusal", None)
                function_call = getattr(message, "function_call", None)
                reasoning_content = getattr(message, "reasoning_content", None)
                reasoning = getattr(message, "reasoning", None)
                if tool_calls:
                    context_parts.append(f"tool_calls={self._short_repr(tool_calls, max_chars=500)}")
                if function_call:
                    context_parts.append(f"function_call={self._short_repr(function_call, max_chars=500)}")
                if refusal:
                    context_parts.append(f"refusal={refusal!r}")
                if reasoning_content:
                    context_parts.append(f"reasoning_content={self._short_repr(reasoning_content, max_chars=500)}")
                if reasoning:
                    context_parts.append(f"reasoning={self._short_repr(reasoning, max_chars=500)}")
                context_parts.append(f"message_fields={self._visible_attrs(message)}")
            context_parts.append(f"choice_fields={self._visible_attrs(choice)}")
        return ", ".join(context_parts)

    def _build_openai_error_context(self, error: Exception) -> str:
        context_parts = [
            f"model={self.model_name!r}",
            f"error_type={error.__class__.__module__}.{error.__class__.__name__}",
            f"error={self._short_repr(str(error), max_chars=1000)}",
        ]
        status_code = getattr(error, "status_code", None)
        if status_code is not None:
            context_parts.append(f"status_code={status_code}")
        response = getattr(error, "response", None)
        if response is not None:
            context_parts.append(f"response_status_code={getattr(response, 'status_code', None)!r}")
            context_parts.append(f"response_headers={self._short_repr(dict(getattr(response, 'headers', {}) or {}), max_chars=800)}")
            text = getattr(response, "text", None)
            if text:
                context_parts.append(f"response_text={self._short_repr(text, max_chars=2000)}")
        body = getattr(error, "body", None)
        if body:
            context_parts.append(f"body={self._short_repr(body, max_chars=2000)}")
        return ", ".join(context_parts)

    def _extract_response_content(self, response) -> str:
        choices = getattr(response, "choices", None)
        if not choices:
            raise LLMResponseError(
                "OpenAI-compatible provider returned no choices "
                f"({self._build_response_context(response)})"
            )

        choice = choices[0]
        message = getattr(choice, "message", None)
        if message is None:
            raise LLMResponseError(
                "OpenAI-compatible provider returned a choice without message "
                f"({self._build_response_context(response, choice)})"
            )

        content = getattr(message, "content", None)
        if content is None:
            raise LLMResponseError(
                "OpenAI-compatible provider returned assistant message content=None; "
                "this is a system-level provider/API boundary error, not a model-output validation error "
                f"({self._build_response_context(response, choice)})"
            )
        if not isinstance(content, str):
            raise LLMResponseError(
                "OpenAI-compatible provider returned assistant message content with invalid type "
                f"{type(content).__name__}; expected str ({self._build_response_context(response, choice)})"
            )
        return content

    def _extract_response_usage(self, response) -> ChatCompletionsUsage:
        usage = getattr(response, "usage", None)
        if usage is None:
            return ChatCompletionsUsage(prompt=0, completion=0, total=0)
        return ChatCompletionsUsage(
            prompt=getattr(usage, "prompt_tokens", 0) or 0,
            completion=getattr(usage, "completion_tokens", 0) or 0,
            total=getattr(usage, "total_tokens", 0) or 0,
        )

    async def chat(
            self, 
            messages,
            max_tokens: int  = 1024,
            temperature: int = 0.5,
            top_p: int = 0.95,
            top_k: int = 40,
            enable_thinking: bool = False
        ):

        async with self._semaphore:
            try:
                response = await self._client.chat.completions.create(
                    messages=messages,
                    model=self.model_name,
                    max_tokens  = max_tokens,
                    temperature = temperature,
                    top_p       = top_p,
                    extra_body  = {
                        "top_k": top_k,
                        "chat_template_kwargs": {"enable_thinking": enable_thinking}
                    },
                )
                return ChatCompletions(
                    content=self._extract_response_content(response),
                    usage=self._extract_response_usage(response),
                )
            except LLMResponseError:
                raise
            except (APIStatusError, RateLimitError, APIConnectionError, APITimeoutError, OpenAIError) as e:
                raise LLMResponseError(
                    "OpenAI-compatible provider/API call failed; this is a run-level "
                    "provider/API boundary error, not a model-output validation error "
                    f"({self._build_openai_error_context(e)})"
                ) from e
            except Exception as e:
                raise LLMResponseError(
                    "OpenAI-compatible provider/API call failed with an unexpected exception; "
                    "this is a run-level provider/API boundary error, not a model-output "
                    "validation error "
                    f"({self._build_openai_error_context(e)})"
                ) from e