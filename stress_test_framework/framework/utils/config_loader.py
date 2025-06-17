
import yaml

def load_config(path="framework/config/test_config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
