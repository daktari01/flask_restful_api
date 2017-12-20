from flask import Flask, jsonify, request
from flask.ext.pymongo import Pymongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'prettyprinted_rest'
app.config['MONGO_URI'] = 'mongodb://pretty:printed@ds011863.mlab.com:11863/prettyprinted_rest'

mongo = Pymongo(app) 

@app.route('/framework', methods=['GET'])
def get_all_frameworks():
    framework = mongo.db.framework

    output = []

    for q in framework.find():
        output.append({'name' : q.name, 'language' : q.language})

    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)