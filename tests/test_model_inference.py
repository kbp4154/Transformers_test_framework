import pytest
from transformers import pipeline

@pytest.mark.parametrize("model_name", ["distilbert-base-uncased", "bert-base-uncased"])
def test_inference_output_consistency(model_name):
    """Ensure model inference runs and output is stable."""
    nlp = pipeline("sentiment-analysis", model=model_name)
    outputs = [nlp("Transformers are amazing!") for _ in range(2)]
    assert outputs[0][0]['label'] == outputs[1][0]['label']
