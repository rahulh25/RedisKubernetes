from flask import Flask, render_template, request, redirect, jsonify
import redis
import json
import os

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
        reply = r.execute_command('GRAPH.QUERY', 'GRAPH_DEMO',"MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
        reply1 = r.execute_command('GRAPH.QUERY', 'GRAPH_ONE', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
        reply2 = r.execute_command('GRAPH.QUERY', 'GRAPH_TWO', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
        reply3 = r.execute_command('GRAPH.QUERY', 'GRAPH_THREE', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
        reply4 = r.execute_command('GRAPH.QUERY', 'GRAPH_FOUR', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
        reply5 = r.execute_command('GRAPH.QUERY', 'GRAPH_FIVE', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
        reply6 = r.execute_command('GRAPH.QUERY', 'GRAPH_SIX', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
        return render_template('your_data.html',data="{GRAPH_DEMO:"+str(reply)+"}"+"\n"+"{GRAPH_ONE:"+str(reply1)+"}"+"\n"+"{GRAPH_TWO:"+str(reply2)+"}"+"\n"+"{GRAPH_THREE:"+str(reply3)+"}"+"\n"+"{GRAPH_FOUR:"+str(reply4)+"}"+"\n"+"{GRAPH_FIVE:"+str(reply5)+"}"+"\n"+"{GRAPH_SIX:"+str(reply6)+"}"+"\n")