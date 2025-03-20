import json
import Faker

def handler():
    fake = Faker()
    message = 'Hello {}!'.format(fake.name())
    info ={
        "Type": "Container Example",
        "Version": 1
    }
    print(info)
    return {
        "message": json.dumps(message),
        "status": 200
        }