from flask import Flask,request
import redis

app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def Hello():
    if request.method == 'POST':
        r=redis.Redis(host='127.0.0.1',port=6379,db=0)
        r.set('name','neeraj')
        h=r.get('jay')
        return h
    else:
        return f'Hello World!'


app.run(host="0.0.0.0", port=4000, debug=True)