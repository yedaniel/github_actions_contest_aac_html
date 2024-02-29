import yaml
import json
import sys

def extract_parameters(data_section):
    extracted = {}
    for key, value in data_section.items():
        if key.endswith('key'):
            value_key = key.replace('key', 'value')
            extracted[value] = data_section.get(value_key, "")
    return extracted

def extract_tags(data_section):
    extracted = {}
    for key, value in data_section.items():
        if key.endswith('key'):
            value_key = key.replace('key', 'value')
            extracted[value] = data_section.get(value_key, "")
    return extracted

def convert_yaml_to_json(yaml_file_path):
    with open(yaml_file_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            combined = {
                "parameters": {},
                "tags": {}
            }

            # Extract parameters
            if 'parameters' in data:
                combined["parameters"] = extract_parameters(data['parameters'])

            # Extract tags
            if 'tags' in data:
                combined["tags"] = extract_tags(data['tags'])

            return combined
        except yaml.YAMLError as exc:
            print(exc)
            return {}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 convert_yaml_to_json.py <yaml_file_path>")
    else:
        yaml_file_path = sys.argv[1]  # Get YAML file path from command line argument
        combined_json = convert_yaml_to_json(yaml_file_path)
        print(json.dumps(combined_json, indent=2))
