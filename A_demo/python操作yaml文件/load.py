import yaml

with open('./test.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

print(type(data))
print(data)