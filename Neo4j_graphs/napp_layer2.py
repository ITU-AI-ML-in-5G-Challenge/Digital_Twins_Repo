#Neo4j code for creating the database graph shown in the report and presentation (layer 2)
from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable

# To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
# The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/

class napp:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
          
    def create_node(self, label, name, level):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_node, label, name, level)
            print(result)
            
    @staticmethod
    def _create_node(tx, label, name, level):
        query = (
            "CREATE (n1:"+ label + "{ name: $name,  level: $level})"
        )
        result = tx.run(query, label = label, name = name, level = level)
        try:
            return result
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

    def delete_node(self, name):
        with self.driver.session() as session:
            result = session.write_transaction(self._delete_node, name)
            print(result)
            
    @staticmethod
    def _delete_node(tx, name):
        query = (
            "MATCH (n1{name: $name}) DETACH DELETE n1"
        )
        result = tx.run(query, name = name)
        try:
            return result
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise
            
    def delete_label_node(self, label):
        with self.driver.session() as session:
            result = session.write_transaction(self._delete_label_node, label)
            print(result)
    
    @staticmethod
    def _delete_all(tx):
        query = (
            "MATCH (n1) DETACH DELETE n1"
        )
        result = tx.run(query)
        try:
            return result
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise
            
    def delete_all(self):
        with self.driver.session() as session:
            result = session.write_transaction(self._delete_all)
            print(result)
            
    @staticmethod
    def _delete_label_node(tx, label):
        query = (
            "MATCH (n1:"+ label + ")DETACH DELETE n1"
        )
        result = tx.run(query, label = label)
        try:
            return result
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise
            
    def create_link(self, name1, name2, link):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(
                self._create_link, name1, name2, link)
            for row in result:
                print("Created link between: {n1}, {n2}".format(n1 = row['n1'], n2 = row['n2']))

    @staticmethod
    def _create_link(tx, name1, name2, link):
        query = (
            "MATCH (n1{name: $name1}),(n2{name: $name2})"
            "CREATE (n1)-[:"+link+"]->(n2) "
            "RETURN n1, n2"
        )
        result = tx.run(query, name1 = name1, name2 = name2)
        try:
            return [{"n1": row["n1"]["name"], "n2": row["n2"]["name"]} for row in result]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise
    
    
    def delete_link(self, name1, name2, link):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(
                self._delete_link, name1, name2, link)
            for row in result:
                print(result)

    @staticmethod
    def _delete_link(tx, name1, name2, link):
        query = (
            "MATCH (n1{name: $name1}),(n2{name: $name2})"
            "MATCH (n1)-[l:"+link+"]->(n2) "
            "DELETE l"
        )
        result = tx.run(query, name1 = name1, name2 = name2, link = link)
        try:
            return result
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise   
    

    def set_node(self, name, key, value):
        with self.driver.session() as session:
            result = session.write_transaction(self._set_node, name, key, value)
            print(result)
            
            
    @staticmethod
    def _set_node(tx, name, key, value):
        query = (
            "MATCH (n1{name: $name}) SET n1." + key +  "= $value" 
        )
        result = tx.run(query, name = name, key = key, value = value)
        try:
            return result
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

            
if __name__ == "__main__":
    app = napp("bolt://localhost:7687", "neo4j", "build")
    app.delete_all()
    app.create_node('PY','Ev_Py', 1)
    app.create_node('NODE','Ev_NJS', 1)
    app.create_node('IPFS','Ev_IPFS', 1)
    
    app.create_node('PY','Exp_Py', 1)
    app.create_node('NODE','Exp_NJS', 1)
    app.create_node('IPFS','Exp_IPFS', 1)
    
    app.create_node('PY','Cur_Py', 1)
    app.create_node('NODE','Cur_NJS', 1)
    app.create_node('IPFS','Cur_IPFS', 1)
    
    app.create_node('PY','DT_Py', 1)
    app.create_node('IPFS','DT_IPFS', 1)
    
    
    
    app.create_link('Ev_Py', 'Ev_NJS', 'CTR_JSON')
    app.create_link('Ev_NJS', 'Ev_IPFS', 'CTR_JSON')
    app.create_link('Exp_NJS', 'Ev_Py', 'EXP_REP_JSON')
    
    app.create_link('Ev_NJS', 'Exp_Py', 'CTR_JSON')
    
    app.create_link('Exp_Py', 'Exp_NJS', 'EXP_REP_JSON')
    app.create_link('Exp_NJS', 'Exp_IPFS', 'EXP_REP_JSON')
    
    app.create_link('Exp_NJS', 'Cur_Py', 'EXP_REP_JSON')
    
    app.create_link('Cur_Py', 'Cur_NJS', 'PTR_CTR_JSON')
    app.create_link('Cur_NJS', 'Cur_IPFS', 'PTR_CTR_JSON')
    
    app.create_link('Exp_Py', 'DT_Py', 'EXP_TO_RUN_JSON')
    app.create_link('DT_Py', 'Exp_Py', 'EXP_RESULTS_JSON')
    
    app.create_link('DT_Py', 'DT_IPFS', 'TO_BE_IMPLEMENTED')