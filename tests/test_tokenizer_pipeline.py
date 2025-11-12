def test_tokenizer_encode_decode(model_and_tokenizer):
    _, _, tokenizer = model_and_tokenizer
    text = "Transformers make NLP easier"
    tokens = tokenizer.encode(text)
    decoded = tokenizer.decode(tokens)
    assert text.split()[0].lower() in decoded.lower()
