import redis

r = redis.Redis(host='192.168.99.108', port=30651, db=0)
reply = r.execute_command('GRAPH.QUERY', 'GRAPH_TWO', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Joffrey Baratheon'}) RETURN r")
print(reply)