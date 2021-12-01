import json

def to_json(func):
    def wrapper():
        return (json.dumps(func()))
    return wrapper

@to_json
def get_data():
    return {
            'data': 42
    }
    
print(type(get_data()))