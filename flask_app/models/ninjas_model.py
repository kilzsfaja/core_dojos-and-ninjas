from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import dojos_model

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# --------------------- CREATE NINJA -------------------
    @classmethod
    def create_one_ninja(cls, data):
        query = """
            INSERT INTO ninjas (dojo_id, first_name, last_name, age)
            VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

# ----------------------GET ONE NINJA --------------------
    # @classmethod
    # def get_one_ninja(cls, dojo_id):
    #     query = """
    #         SELECT *
    #         FROM ninjas
    #         WHERE dojo_id = %(dojo_id)s;
    #     """
    #     result = connectToMySQL(DATABASE).query(query, {'dojo_id': dojo_id})
    #     return result