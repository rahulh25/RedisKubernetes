import redis

r = redis.Redis(host='192.168.99.100', port=6379, db=0)
reply = r.execute_command('GRAPH.QUERY', 'MotoGP', "MATCH (r:Rider)-[:rides]->(t:Team) WHERE t.name = 'Yamaha' RETURN r.name, t.name")
print(reply)