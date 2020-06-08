import yaml

filename = "prac4.yml"

with open(filename) as f:
    yaml.out = yaml.load(f)

print (yaml.out)

