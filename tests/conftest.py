import pytest
import os
import sys

# Agregar la raíz del proyecto al PYTHONPATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()
