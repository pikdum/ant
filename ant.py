import json
import yaml
from flask import Flask, Response

with open('db.yml', 'r') as file:
    db = yaml.safe_load(file)

app = Flask(__name__)

@app.route('/name-lookup/<int:anilist_id>.json')
def name_lookup(anilist_id):
    if anilist_id in db:
        r = Response(json.dumps(db[anilist_id]))
        r.headers['Content-Type'] = 'application/json'
        return r, 200
    else:
        return "Not Found!", 404
