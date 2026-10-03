# PDF2HTMLBook

Conversor de textos en PDF (digitales o escaneados) a una versión HTML limpia, con texto seleccionable, vista previa local y dos modos principales de salida: fiel y fluido.

## Características
- Detección simple de PDF digital vs escaneado
- OCR opcional con Tesseract (es+en por defecto)
- Limpieza básica de escaneo y orden de lectura por columnas
- Reconstrucción básica de tablas sin bordes
- Detección heurística de figuras y pies de figura
- HTML con tema clásico, moderno y Arial 12
- Vista previa local desde Flask
- CLI con opciones para OCR, tema, layout, procesos y reanudación

## Instalación

### Windows
1. Instala Python 3.11+
2. Instala Tesseract OCR desde:
   https://github.com/UB-Mannheim/tesseract/wiki
3. Asegúrate de que `tesseract` esté en PATH.
4. Ejecuta:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
brew install tesseract
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr python3-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Uso

```bash
python app.py libro.pdf --ocr auto --idioma "es+en" --formato fluido --tema arial12 --procesos 4
```

### Opciones principales
- `--ocr auto|siempre|no`
- `--idioma es+en`
- `--formato fiel|fluido`
- `--tema clasico|moderno|arial12`
- `--detector cv|ia`
- `--limpiar no|suave|fuerte`
- `--mejorar no|suave|esrgan`
- `--vectorizar`
- `--depurar`
- `--mate auto|no`
- `--procesos N`
- `--reanudar`

## Estructura del proyecto

```text
pdf2htmlbook/
├─ app.py
├─ requirements.txt
├─ README.md
├─ book_converter/
│  ├─ __init__.py
│  ├─ cli.py
│  ├─ layout.py
│  ├─ models.py
│  ├─ pipeline.py
│  ├─ preview_server.py
│  ├─ renderer.py
│  └─ utils.py
├─ tests/
│  └─ test_layout.py
└─ pyproject.toml
```

## Vista previa

Después de ejecutar el programa, se abre o se sirve una vista previa local en:

```text
http://127.0.0.1:5000/preview
```

## Limitaciones conocidas
- No se conservan exactamente negritas, cursivas y fuentes del original.
- OCR puede fallar en escaneos de baja resolución.
- Las tablas sin bordes y las ecuaciones complejas necesitarán revisión manual.
- Este proyecto entrega una base sólida y ejecutable, no una solución “casi perfecta” de producción para todo tipo de libros.

## Pruebas

```bash
pytest -q
```
