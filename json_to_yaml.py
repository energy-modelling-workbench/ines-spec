import json
import toml
import yaml

with open('ines-spec.json', 'r') as file:
    configuration = json.load(file)

with open('ines-spec.yaml', 'w') as yaml_file:
    yaml.dump(configuration, yaml_file)

with open('ines-spec.toml', 'w') as toml_file:
    toml.dump(configuration, toml_file, encoder=toml.TomlEncoder())

