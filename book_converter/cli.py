from __future__ import annotations

import argparse
from pathlib import Path

from .models import ConversionOptions
from .pipeline import BookConverter
from .renderer import render_html_from_blocks
from .preview_server import create_preview_app


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convertidor de PDFs a HTML limpio")
    parser.add_argument("pdf", help="Ruta al PDF")
    parser.add_argument("--ocr", choices=["auto", "siempre", "no"], default="auto")
    parser.add_argument("--idioma", default="es+en")
    parser.add_argument("--formato", choices=["fiel", "fluido"], default="fluido")
    parser.add_argument("--tema", choices=["clasico", "moderno", "arial12"], default="moderno")
    parser.add_argument("--detector", choices=["cv", "ia"], default="cv")
    parser.add_argument("--limpiar", choices=["no", "suave", "fuerte"], default="suave")
    parser.add_argument("--mejorar", choices=["no", "suave", "esrgan"], default="no")
    parser.add_argument("--vectorizar", action="store_true")
    parser.add_argument("--depurar", action="store_true")
    parser.add_argument("--mate", choices=["auto", "no"], default="auto")
    parser.add_argument("--procesos", type=int, default=1)
    parser.add_argument("--reanudar", action="store_true")
    return parser


def run_command(args: argparse.Namespace) -> int:
    options = ConversionOptions(
        ocr=args.ocr,
        idioma=args.idioma,
        formato=args.formato,
        tema=args.tema,
        detector=args.detector,
        limpiar=args.limpiar,
        mejorar=args.mejorar,
        vectorizar=args.vectorizar,
        depurar=args.depurar,
        mate=args.mate,
        procesos=max(1, args.procesos),
        reanudar=args.reanudar,
    )

    converter = BookConverter(options)
    pages = converter.process(Path(args.pdf))

    blocks = []
    for page in pages:
        for block in page.layout_blocks:
            blocks.append({
                "kind": block.kind,
                "content": " ".join(s.text for s in block.items),
            })

    html = render_html_from_blocks(blocks, mode=options.formato, theme=options.tema)
    out_path = Path(args.pdf).with_suffix(".html")
    out_path.write_text(html, encoding="utf-8")

    app = create_preview_app(html)
    print(f"HTML generado: {out_path}")
    print("Vista previa local disponible en http://127.0.0.1:5000/preview")
    app.run(host="127.0.0.1", port=5000, debug=False)
    return 0
