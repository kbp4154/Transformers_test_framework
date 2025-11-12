from transformers import AutoTokenizer

def test_tokenizer_special_tokens():
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    tokens = tokenizer.tokenize("Hello world!")
    assert "[UNK]" not in tokens
