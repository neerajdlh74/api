from flask import Flask, request
import redis
import logging

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == 'POST':
        searchword = request.args.get('key', '')
        f= open("word.txt","w+")
        f.write(searchword)
        f.close()
        r = redis.Redis(host='127.0.0.1', port=6379, db=0)
        r.set('key', searchword)
        h = r.get('key')
        return h
    else:
        return f"Hello"
    

app.run(host="0.0.0.0", port=4000, debug=True)