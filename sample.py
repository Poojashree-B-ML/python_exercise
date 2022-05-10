import yaml
import json

with open("sample1.yaml", 'r') as Yaml_Input, open("sample2.json", "w") as JSON_Output:
        yamlObject = yaml.safe_load(Yaml_Input) 
        print(type(yamlObject))
        json.dump(yamlObject, JSON_Output)
