import operator
import time

import bs4
import wikipedia
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from utils import extract_events

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

history = dict()


@app.route('/generate', methods=['GET', 'POST'])
@cross_origin()
def generate():
    start = time.time()
    query = request.args.get('q')
    if query:
        if history.get(query):
            json = history.get(query)
        else:
            json = dict()
            try:
                p_wiki = wikipedia.page(title=wikipedia.search(query)[0], auto_suggest=False)
                try:
                    soup = bs4.BeautifulSoup(p_wiki.html(), features="html.parser")
                    table = soup.find('table', class_='infobox')
                    result = {}
                    for tr in table.find_all('tr'):
                        if tr.find('th') and tr.find('td'):
                            if tr.find('td') != "":
                                result[tr.find('th').text] = tr.find('td').text
                    json['description'] = result
                    json['profilepic'] = soup.find('table', class_='infobox').find('a', class_='image').find('img')[
                        'src']
                except AttributeError as e:
                    print(e)
                text = p_wiki.summary + ' ' + p_wiki.content
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
                json['images'] = [image for image in p_wiki.images if '.jpg' in image]
                json['title'] = p_wiki.title
                json['categories'] = p_wiki.categories
            except wikipedia.PageError:
                return jsonify({
                    'status': 404,
                    'data': wikipedia.search(query),
                    'query': query,
                })
            except wikipedia.DisambiguationError:
                return jsonify({
                    'status': 404,
                    'data': wikipedia.search(query),
                    'query': query
                })
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
