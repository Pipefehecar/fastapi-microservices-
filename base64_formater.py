"""
Script for encoding values of a JSON file to base64.
The JSON file must have the following structure:
{
    "key1": "value1",
    "key2": "value2",
    ...
}
use this tool to encode kubernetes secrets values to base64.
"""

import base64
import json


def encode_values_to_base64(json_file) -> dict:
    """
    Encode the values of a JSON file to base64.
    """
    with open(json_file, "r") as file:
        json_content = json.load(file)

    encoded_content = {}
    for key, value in json_content.items():
        value_str = str(value)
        base64_bytes = base64.b64encode(value_str.encode("utf-8"))
        base64_str = base64_bytes.decode("utf-8")
        encoded_content[key] = base64_str

    return encoded_content


if __name__ == "__main__":
    json_file = "kubernetes/environments.json"

    encoded_result = encode_values_to_base64(json_file)

    print("Contenido con valores en base64:")
    print(json.dumps(encoded_result, indent=2))
