import redis

r = redis.Redis(host='192.168.99.108', port=31845, db=0)
reply = r.execute_command('GRAPH.QUERY', 'GRAPH_SIX', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Addam Marbrand'}) RETURN r")
print(reply)