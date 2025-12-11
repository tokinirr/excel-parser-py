import yaml

def load_config(path):
    with open(path, "r", encoding="utf8") as f:
        return yaml.safe_load(f)
