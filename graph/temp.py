# from py2neo import Graph, Path
# graph = Graph('http://192.168.1.57:7474/data/',username='neo4j',password='password')

# tx = graph.begin()
# for name in ["Alice", "Bob", "Carol"]:
#     tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
# alice, bob, carol = [result.one for result in tx.commit()]

# friends = Path(alice, "KNOWS", bob, "KNOWS", carol)
# graph.create(friends)

from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://192.168.1.57:7687", auth=basic_auth("neo4j", "password"))
session = driver.session()

session.run("CREATE (a:Person {name: {name}, title: {title}})",
            {"name": "Arthur", "title": "King"})

result = session.run("MATCH (a:Person) WHERE a.name = {name} "
                    "RETURN a.name AS name, a.title AS title",
                    {"name": "Arthur"})
for record in result:
    print("%s %s" % (record["title"], record["name"]))

session.close()