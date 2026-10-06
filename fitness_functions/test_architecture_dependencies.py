from pathlib import Path

def test_marketplace_has_no_forbidden_internal_dependencies():
    source = Path("prototype/marketplace.py").read_text(encoding="utf-8")

    forbidden_imports = [
        "from prototype.smart_meter",
        "import prototype.smart_meter",
        "from prototype.settlement",
        "import prototype.settlement"
    ]

    for forbidden in forbidden_imports:
        assert forbidden not in source
