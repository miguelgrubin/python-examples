import datetime
import pprint

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.pytest
collection = db.samples

"""   INSERT ROW   """
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}
"""
post_id = collection.insert_one(post).inserted_id
print(post_id)
"""

"""
    BULK INSERT
"""
new_posts = [
    {
        "author": "Mike",
        "text": "Another post!",
        "tags": ["bulk", "insert"],
        "date": datetime.datetime(2009, 11, 12, 11, 14)
    },
    {
        "author": "Eliot",
        "title": "MongoDB is fun",
        "text": "and pretty easy too!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    }
]

result = collection.insert_many(new_posts)
print("###  BULK INSERT  ###")
print(result.inserted_ids)


print("###  FIND ONE  ###")
one_row = collection.find_one({"author": "Mike"})
pprint.pprint(one_row)

print("###  FIND ALL  ###")
for sample in collection.find({"author": "Mike"}).sort("date"):
    pprint.pprint(sample)
