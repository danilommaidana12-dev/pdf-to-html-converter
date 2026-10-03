from __future__ import annotations

from pathlib import Path


def test_detect_pdf_type():
    from book_converter.layout import detect_pdf_type
    assert detect_pdf_type(800) == "digital"
    assert detect_pdf_type(20, page_image_ratio=0.5) == "scanned"


def test_detect_columns():
    from book_converter.layout import detect_columns
    from book_converter.models import TextSpan
    spans = [
        TextSpan(0, 0, 180, 100, "columna 1"),
        TextSpan(200, 0, 380, 100, "columna 2"),
    ]
    cols = detect_columns(spans, 500, 300)
    assert len(cols) >= 2


def test_merge_paragraphs():
    from book_converter.layout import merge_paragraphs
    from book_converter.models import TextSpan
    spans = [
        TextSpan(0, 100, 180, 110, "hola"),
        TextSpan(0, 112, 180, 122, "mundo"),
        TextSpan(0, 200, 180, 210, "otro"),
    ]
    groups = merge_paragraphs(spans, vertical_gap=10)
    assert len(groups) >= 2


def test_split_hyphenated_words():
    from book_converter.layout import split_hyphenated_words
    assert split_hyphenated_words("con-ti-nuo") == "continuo"
    assert split_hyphenated_words("pe-rro") == "perro"


def test_detect_figure_captions():
    from book_converter.layout import detect_figure_captions
    from book_converter.models import TextSpan
    spans = [TextSpan(0, 0, 200, 20, "Figura 3. Mapa del sistema")]
    hits = detect_figure_captions(spans)
    assert hits and "Figura 3" in hits[0]


def test_rebuild_borderless_table():
    from book_converter.layout import rebuild_borderless_table
    words = ["A", "B", "C", "D", "E", "F", "G", "H"]
    table = rebuild_borderless_table(words, rows_estimate=2)
    assert len(table) > 0
    assert all(len(row) > 0 for row in table)


def test_order_blocks_for_reading():
    from book_converter.layout import order_blocks_for_reading
    from book_converter.models import LayoutBlock
    blocks = [
        LayoutBlock("figure", (0, 0, 200, 200), []),
        LayoutBlock("title", (0, 50, 300, 80), []),
    ]
    ordered = order_blocks_for_reading(blocks)
    assert ordered[0].kind == "title"
