import redis

r = redis.Redis(host='192.168.99.107', port=31245, db=0)
reply = r.execute_command('GRAPH.QUERY', 'GRAPH_5', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
print(reply)