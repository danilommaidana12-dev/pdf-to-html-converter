from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any
import warnings


def warn_once(key: str, message: str) -> None:
    if not hasattr(warn_once, "_seen"):
        warn_once._seen = set()
    if key in warn_once._seen:
        return
    warn_once._seen.add(key)
    warnings.warn(message, RuntimeWarning)


def safe_json_dump(path: str | Path, payload: Any) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    try:
        with open(tmp, "w", encoding="utf-8") as fp:
            json.dump(payload, fp, ensure_ascii=False, indent=2)
        for _ in range(5):
            try:
                os.replace(tmp, target)
                return
            except OSError:
                time.sleep(0.2)
    except Exception:
        pass
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass
