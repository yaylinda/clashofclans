import yaml

YAML_FILE_PATH = 'clashofclans.yaml'


def to_camel_case(name):
    name = name.lower().split('_')  # convert to lower case and split
    return name[0] + ''.join(word.title() for word in name[1:])  # return camel-cased word


# Recursive function to traverse the nested dictionaries/lists
def traverse(node):
    if isinstance(node, list):
        return [traverse(item) for item in node]
    elif isinstance(node, dict):
        for key, value in node.items():
            if key == "enum":
                node[key] = [to_camel_case(item) for item in value]
            else:
                node[key] = traverse(value)
    return node


def enums_to_camel_case():
    # Read the YAML file
    with open(YAML_FILE_PATH, 'r') as file:
        data = yaml.safe_load(file)

    # Apply transform function to convert enums
    data = traverse(data)

    # Write the YAML file
    with open(YAML_FILE_PATH, 'w') as file:
        yaml.safe_dump(data, file)


if __name__ == '__main__':
    """
    Define various function here to "clean up" the yaml. Then run `make gen` to regenerate the client.
    """
    enums_to_camel_case()
