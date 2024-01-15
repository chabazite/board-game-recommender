# Using Flask for the web app
from flask import Flask, request, jsonify, render_template
#from recommendation_model import recommend_games  # Your model script
import requests
import xml.etree.ElementTree as ET


app = Flask(__name__)


@app.route('/')

def index():
    return render_template('index.html')


@app.route('/recommend', methods=['GET'])

def recommend():
    game_name = request.args.get('game')
    response = requests.get(f"https://www.boardgamegeek.com/xmlapi2/search?query={game_name}")

    if response.status_code == 200:
    #    root = ET.fromstring(response.content)
    #    for item in root.findall('item'):
    #        name = item.find('name').attrib['value']
    #        year_published = item.find('yearpublished').attrib['value']
        return {'yes':1}
    else:
        return {'non':1}
    #    return jsonify(f"Name: {name}: Year: {year_published}")
    #else:
    #    return {"Game not found": 404}

if __name__ == '__main__':
    app.run(debug=True)
