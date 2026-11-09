
import pytest
from fastapi.testclient import TestClient
import socket
import threading
import time
import uvicorn
from app.main import app
from app.data.hospedes import hospedes
from app.data.reservas import reservas


@pytest.fixture
def client():
    hospedes.clear()
    reservas.clear()

    with TestClient(app) as test_client:
        yield test_client

    hospedes.clear()
    reservas.clear()

@pytest.fixture(scope="session")
def server_url():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        porta = sock.getsockname()[1]

    config = uvicorn.Config(
        app=app,
        host="127.0.0.1",
        port=porta,
        log_level="warning"
    )

    server = uvicorn.Server(config=config)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()

    time.sleep(1)

    yield f"http://127.0.0.1:{porta}"

    server.should_exit = True
    thread.join(timeout=2)
