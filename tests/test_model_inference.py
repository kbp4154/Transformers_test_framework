import torch

def test_model_inference(model_and_tokenizer):
    model_name, model, tokenizer = model_and_tokenizer
    inputs = tokenizer("Hello world", return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=5)
    assert outputs is not None
    assert outputs.shape[1] > 0
