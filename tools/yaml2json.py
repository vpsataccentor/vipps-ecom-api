import os
import yaml
import json

base_path = os.path.join(os.path.dirname(__file__), "..", "docs")

yaml = yaml.safe_load(open(os.path.join(base_path, "swagger.yaml"), "r", encoding="utf-8"))
json_file = open(os.path.join(base_path, "swagger.json"), "w", encoding="utf-8")
json_file.write(json.dumps(yaml, indent=2, ensure_ascii=False))
