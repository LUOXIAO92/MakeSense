"""
Base provider class for upstream data producers.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

from pipeline.schema import PipelineRecord


class BaseProvider(ABC):
    """
    Abstract base class for upstream providers.

    Providers generate initial artifacts (such as transcriptions or translations)
    and populate them into a PipelineRecord. They do NOT perform downstream
    processing like alignment, segmentation, reconstruction, or mapping.
    """

    def __init__(
        self,
        name: str = "",
        max_retries: int = 6,
    ):
        self.name = name or self.__class__.__name__
        self.max_retries = max_retries

    @abstractmethod
    async def provide(
        self,
        record: PipelineRecord,
        audio: Optional[str | Path | bytes] = None,
        **kwargs,
    ) -> PipelineRecord:
        """
        Produce upstream artifacts and populate the given PipelineRecord.

        Args:
            record: The PipelineRecord to populate.
            audio: Audio input if required (path, URL, base64 data URL, or raw bytes).
            **kwargs: Additional provider-specific arguments.

        Returns:
            The updated PipelineRecord with new artifacts populated.
        """
        ...