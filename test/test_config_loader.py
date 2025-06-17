
from framework.utils.config_loader import load_config

def test_config_loader():
    config = load_config("framework/config/test_config.yaml")
    assert "rack_id" in config
