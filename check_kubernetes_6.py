import redis

r = redis.Redis(host='192.168.99.107', port=30917, db=0)
reply = r.execute_command('GRAPH.QUERY', 'GRAPH_6', "MATCH (r:nodes)-[:edges]->(t:nodes {Label:'Addam Marbrand'}) RETURN r")
print(reply)