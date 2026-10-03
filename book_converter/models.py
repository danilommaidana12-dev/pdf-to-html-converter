from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Literal

PageType = Literal["digital", "scanned"]


@dataclass
class TextSpan:
    x0: float
    y0: float
    x1: float
    y1: float
    text: str
    page: int = 0
    block_id: int = 0
    font: Optional[str] = None
    size: Optional[float] = None
    bold: bool = False
    italic: bool = False
    kind: str = "text"


@dataclass
class LayoutBlock:
    kind: str
    rect: tuple[float, float, float, float]
    items: List[TextSpan] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)


@dataclass
class FigureBlock:
    page: int
    rect: tuple[float, float, float, float]
    caption: Optional[str] = None
    image_path: Optional[str] = None
    source: str = "embedded"
    needs_review: bool = False


@dataclass
class EquationBlock:
    page: int
    rect: tuple[float, float, float, float]
    latex: Optional[str] = None
    image_path: Optional[str] = None
    needs_review: bool = False


@dataclass
class TableBlock:
    page: int
    rect: tuple[float, float, float, float]
    rows: List[List[str]] = field(default_factory=list)
    caption: Optional[str] = None
    needs_review: bool = False


@dataclass
class BookPage:
    page_number: int
    page_type: PageType
    text_spans: List[TextSpan] = field(default_factory=list)
    layout_blocks: List[LayoutBlock] = field(default_factory=list)
    figures: List[FigureBlock] = field(default_factory=list)
    equations: List[EquationBlock] = field(default_factory=list)
    tables: List[TableBlock] = field(default_factory=list)
    image_path: Optional[str] = None
    width: float = 595.0
    height: float = 842.0


@dataclass
class ConversionOptions:
    ocr: str = "auto"
    idioma: str = "es+en"
    formato: str = "fluido"
    tema: str = "moderno"
    detector: str = "cv"
    limpiar: str = "suave"
    mejorar: str = "no"
    vectorizar: bool = False
    depurar: bool = False
    mate: str = "auto"
    procesos: int = 1
    reanudar: bool = False
