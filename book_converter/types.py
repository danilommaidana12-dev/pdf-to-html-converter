from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class ColumnSegment:
    left: float
    right: float


@dataclass
class Paragraph:
    lines: List[str]


@dataclass
class TableCell:
    row: int
    col: int
    text: str
