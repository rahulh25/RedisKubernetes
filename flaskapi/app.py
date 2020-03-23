from flask import Flask, render_template, request, redirect, jsonify
import redis
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/your_data',methods=['GET','POST'])
def your_data():
    if request.method=='POST':
        r = redis.Redis(host='192.168.99.108', port=30412, db=0)
        r1=redis.Redis(host='192.168.99.108', port=30776, db=0)
        r2=redis.Redis(host='192.168.99.108', port=30651, db=0)
        r3=redis.Redis(host='192.168.99.108', port=32124, db=0)
        r4=redis.Redis(host='192.168.99.108', port=30856, db=0)
        r5=redis.Redis(host='192.168.99.108', port=31703, db=0)
        r6=redis.Redis(host='192.168.99.108', port=31845, db=0)
        reply = r.execute_command('GRAPH.QUERY', 'GRAPH_DEMO',request.form['query'])
        reply1 = r.execute_command('GRAPH.QUERY', 'GRAPH_ONE', request.form['query'])
        reply2 = r.execute_command('GRAPH.QUERY', 'GRAPH_TWO',request.form['query'])
        reply3 = r.execute_command('GRAPH.QUERY', 'GRAPH_THREE', request.form['query'])
        reply4 = r.execute_command('GRAPH.QUERY', 'GRAPH_FOUR', request.form['query'])
        reply5 = r.execute_command('GRAPH.QUERY', 'GRAPH_FIVE', request.form['query'])
        reply6 = r.execute_command('GRAPH.QUERY', 'GRAPH_SIX', request.form['query'])
        return render_template('your_data.html',data="{GRAPH_DEMO:"+str(reply)+"}"+"\n"+"{GRAPH_ONE:"+str(reply1)+"}"+"\n"+"{GRAPH_TWO:"+str(reply2)+"}"+"\n"+"{GRAPH_THREE:"+str(reply3)+"}"+"\n"+"{GRAPH_FOUR:"+str(reply4)+"}"+"\n"+"{GRAPH_FIVE:"+str(reply5)+"}"+"\n"+"{GRAPH_SIX:"+str(reply6)+"}"+"\n")