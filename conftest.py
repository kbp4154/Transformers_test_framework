import pytest
from transformers import AutoTokenizer, AutoModelForCausalLM

MODELS = ["distilgpt2", "facebook/opt-125m"]

@pytest.fixture(scope="session", params=MODELS)
def model_and_tokenizer(request):
    model_name = request.param
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model_name, model, tokenizer
