import redis

r = redis.Redis(host='192.168.99.107', port=31432, db=0)
reply = r.execute_command('GRAPH.QUERY', 'GRAPH_1', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
print(reply)