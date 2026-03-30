# Simple test to check if we can connect to the Neo4j database.
from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "episteme_local")

driver = GraphDatabase.driver(URI, auth=AUTH)

with driver.session() as session:
    result = session.run("RETURN 'Episteme connected to Neo4j' AS message")
    record = result.single()
    print(record["message"])

driver.close()