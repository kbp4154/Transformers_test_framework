# 🧪 Transformers Test Framework

A lightweight yet scalable testing framework inspired by **Hugging Face’s Transformers testing ecosystem**.  
It automates validation for model inference, tokenization, and cross-version compatibility—designed to scale toward 100K+ tests through CI/CD.

---

### ⚙️ Features
- 🔁 **Dynamic model validation:** runs inference checks across multiple Transformer architectures  
- 🧩 **Tokenizer and pipeline consistency:** validates encode/decode parity and pipeline output shapes  
- 🔄 **Cross-version compatibility:** ensures reproducibility between different `transformers` and `torch` versions  
- 🚀 **CI/CD ready:** integrated GitHub Actions workflow for distributed and nightly testing  
- 📊 **Extensible:** modular test structure that can grow into a full test-infra system  

---

### 📦 Quick Start
```bash
git clone https://github.com/kbp4154/transformers-test-framework.git
cd transformers-test-framework
pip install -r requirements.txt
pytest -v --maxfail=1 --disable-warnings
