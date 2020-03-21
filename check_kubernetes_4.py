import redis

r = redis.Redis(host='192.168.99.107', port=30860, db=0)
reply = r.execute_command('GRAPH.QUERY', 'GRAPH_4', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
print(reply)