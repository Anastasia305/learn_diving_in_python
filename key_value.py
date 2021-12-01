import os
import tempfile
import argparse
import json


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def write_data(data): 
    with open(storage_path, 'w') as fp:
        json.dump(data, fp)
        
def read_data():
    with open(storage_path, 'r') as fp:
        data = json.load(fp)
    return data


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--key')
    argument_parser.add_argument('--value')
    program_arguments = argument_parser.parse_args()
    key = program_arguments.key
    value = program_arguments.value
    try:
        data = read_data()
    except json.decoder.JSONDecodeError:
        data = {key:value}
        write_data(data)
    if key and value:
        if key in data:
            data[key] = data[key] + value
            write_data(data)
        else:
            data.update({key:value})
            write_data(data)

    if key and not value:
        if key in data:
            print(*data[key], sep=", ")
        else:
            print("")

if __name__ == "__main__":
    main()