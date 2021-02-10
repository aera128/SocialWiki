import operator
import time

from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from sqlitedict import SqliteDict

from utils import extract_events

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

history = SqliteDict('database.sqlite', autocommit=True)
parser = reqparse.RequestParser()
parser.add_argument('query', type=str)
parser.add_argument('text', type=str)


class Generate(Resource):
    def post(self):
        start = time.time()
        args = parser.parse_args()
        query = str(args['query'])
        text = str(args['text'])
        if query is not None and text is not None:
            if history.get(query):
                json = history.get(query)
            else:
                json = dict()
                events = extract_events(text)
                events.sort(key=operator.itemgetter(0), reverse=True)
                events = list(dict.fromkeys(events))
                sentences = list()
                clean_events = list()
                for e in events:
                    if e[2] not in sentences:
                        sentences.append(e[2])
                        clean_events.append(e)
                json['posts'] = clean_events
                history[query] = json
            end = time.time()
            return jsonify({
                'status': 200,
                'data': json,
                'query': query,
                'time': end - start
            })
        else:
            return jsonify({
                'status': 404,
                'message': 'Missed parameter',
                'query': query,
            })


api.add_resource(Generate, '/api/generate', endpoint="socialwiki_generate")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
