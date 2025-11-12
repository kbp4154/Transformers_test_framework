import pytest

@pytest.fixture(scope="session")
def sample_text():
    return "Transformers make AI accessible to everyone."