import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

# Testando a rota principal


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "Bem-vindo à API de Recomendação de Produtos"
    }
