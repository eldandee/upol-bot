def open_json():
    with open('upol.json') as json_file:
        data = json.load(json_file)
    return data


def save_json(data):
    with open('upol.json', 'w') as outfile:
        json.dump(data, outfile)


def open_db():
    # This will crash :hyperlul:
    client = pymongo.MongoClient(MONGODB_URI)
    db = client.get_default_database()
    upol = db[DB_NAME]
    return client, upol


def read_db():
    client, upol = open_db()
    data = upol.find_one()
    client.close()
    return data
