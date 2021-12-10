from flask_frozen import Freezer
from ant import app, db

freezer = Freezer(app)

@freezer.register_generator
def name_lookup():
    for id in db.keys():
        yield {'anilist_id': id}

if __name__ == '__main__':
    freezer.freeze()
