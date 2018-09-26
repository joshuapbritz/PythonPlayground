import pymongo
import uuid

CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
DBREF = CLIENT["library"]
members = DBREF['members']

def add_member():
    membership_id = str(uuid.uuid4())
    name = str(input('What is the members\'s first name? '))
    lastname = str(input('What is the members\'s last name? '))

    members.insert_one({
        "name": name,
        "surname": lastname,
        "membership_id": membership_id
    })

x = list(members.find({ "name":"Joshua" }))

print(x)
