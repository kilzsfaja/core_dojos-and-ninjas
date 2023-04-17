from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# from flask_app.models import ninjas_model

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ------------- DISPLAY ALL DOJOS ------------------
    @classmethod
    def display_all_dojos(cls):
        query = """
            SELECT *
            FROM dojos;
        """
        result = connectToMySQL(DATABASE).query_db(query)

        list_of_dojos = []
        for dojo in result:
            list_of_dojos.append( cls(dojo) )
        return list_of_dojos

# ------------ CREATE DOJO ------------------
    @classmethod
    def create_dojo(cls, data):
        query = """
            INSERT INTO dojos (name)
            VALUES (%(name)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

# ------------- GET ONE DOJO ----------------

    @classmethod
    def get_one_dojo(cls, data):
        query = """
            SELECT * FROM dojos
            LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
            WHERE dojo_id = (%(id)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        return result



        # current_dojo = cls(result[0])

        # for row in result:
        #     current_ninja = {
        #         'id': row['id'],
        #         'name': row['name'],
        #         'created_at': row['created_at'],
        #         'updated_at': row['updated_at']
        #     }
        # return current_dojo