import asyncio
from openai import AsyncOpenAI
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

    def _build_response_context(self, response, choice=None) -> str:
        context_parts = [f"model={self.model_name!r}"]
        response_id = getattr(response, "id", None)
        if response_id:
            context_parts.append(f"response_id={response_id!r}")
        if choice is not None:
            finish_reason = getattr(choice, "finish_reason", None)
            if finish_reason:
                context_parts.append(f"finish_reason={finish_reason!r}")
            message = getattr(choice, "message", None)
            if message is not None:
                tool_calls = getattr(message, "tool_calls", None)
                refusal = getattr(message, "refusal", None)
                if tool_calls:
                    context_parts.append("has_tool_calls=True")
                if refusal:
                    context_parts.append(f"refusal={refusal!r}")
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
            except Exception as e:
                raise e