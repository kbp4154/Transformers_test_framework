import torch
from transformers import AutoModel, AutoTokenizer

def test_cross_version_inference():
    """Validates model forward pass doesn't break across versions."""
    model = AutoModel.from_pretrained("bert-base-uncased")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    inputs = tokenizer("Scaling tests in transformers", return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    assert outputs.last_hidden_state.shape[-1] == model.config.hidden_size
