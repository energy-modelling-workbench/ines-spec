import os
from pathlib import Path
import spinedb_api as api
import json
import toml
import yaml

filedirectory = Path(__file__).parent.resolve()
os.chdir(filedirectory)
spinepath = "sqlite:///ines-spec.sqlite"
jsonpath = "ines-spec.json"
yamlpath = "ines-spec.yaml"
tomlpath = "ines-spec.toml"

with api.DatabaseMapping(spinepath) as db_map:
    fulldata = api.export_data(db_map,parse_value=api.parameter_value.load_db_value)
    data = {
        k:fulldata[k] for k in [
            "entity_classes",
            "entity_alternatives",
            "parameter_value_lists",
            "parameter_definitions"
        ]
    }
    with open(jsonpath, 'w') as f:
        json.dump(data, f, indent=4)

# the direct conversion from spinedb to yaml causes problems so the conversion is done indirectly through json
with open(jsonpath, 'r') as f:
    data = json.load(f)
    with open(yamlpath, 'w') as f:
        yaml.dump(data, f)
    with open(tomlpath, 'w') as f:
        toml.dump(data, f, encoder=toml.TomlEncoder())