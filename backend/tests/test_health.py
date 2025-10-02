import sys
from pathlib import Path

from fastapi.testclient import TestClient

backend_path = Path(__file__).resolve().parents[1] / "app"
sys.path.append(str(backend_path.parent))

from app.main import app  # type: ignore  # noqa: E402


def test_health_endpoint_returns_ok():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
