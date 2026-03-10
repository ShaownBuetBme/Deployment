"""Model loading and prediction helper.
This file should isolate model artifact IO from API logic.
"""

import hashlib
import json
from pathlib import Path

def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_model(artifact_path: str, manifest_path: str | None = None):
    path = Path(artifact_path)
    if not path.exists():
        raise FileNotFoundError(f"Model artifact not found at {artifact_path}")

    model_bytes = path.read_bytes()

    if manifest_path:
        mpath = Path(manifest_path)
        if not mpath.exists():
            raise FileNotFoundError(f"Manifest not found at {mpath}")

        manifest = json.loads(mpath.read_text())
        expected = manifest.get("artifact_checksum")
        if expected:
            actual = _sha256(path)
            if actual != expected:
                raise ValueError(
                    f"Checksum mismatch for {path}. expected={expected}, actual={actual}"
                )

    model = {
        "name": "demo_linear_model",
        "version": "v0.1.0",
        "weights": [0.3, 0.7],
        "bias": 0.1,
        "raw_bytes_len": len(model_bytes),
    }
    return model

def predict(model, features: dict):
    x1 = float(features.get("feature_1", 0.0))
    x2 = float(features.get("feature_2", 0.0))

    w1, w2 = model["weights"]
    b = model["bias"]

    score = w1 * x1 + w2 * x2 + b
    score = max(0.0, min(1.0, score))

    return {
        "model_name": model["name"],
        "model_version": model["version"],
        "score": round(score, 6),
    }