import app as the_app
import pytest

@pytest.fixture
def app():
    yield the_app.app

def client(app):
    yield app.test_client()

def test_title(client):
    res = client.get('/')
    assert 200 == res.status_code
    assert '<title>The Ghost in the Shell</title>' in res.data.decode()
