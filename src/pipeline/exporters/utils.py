"""Shared helpers for final dataset exporters."""

from __future__ import annotations

from collections import OrderedDict
from typing import Iterable


def normalize_author_name(author: str) -> str:
    author = (author or "").strip()
    if not author:
        return ""
    return author.split("/")[-1]


def collapse_authors(authors: Iterable[str]) -> str:
    ordered: OrderedDict[str, None] = OrderedDict()
    for author in authors:
        normalized = normalize_author_name(author)
        if normalized and normalized not in ordered:
            ordered[normalized] = None
    return ",".join(ordered.keys())
