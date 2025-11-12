import transformers, torch

def test_version_compatibility():
    t_version = transformers.__version__
    pt_version = torch.__version__
    assert int(pt_version.split('.')[0]) >= 1
    print(f"Tested with Transformers {t_version} and PyTorch {pt_version}")
