from mysqlconnection import connectToMySQL


class User:
    def __init__(self, data:dict):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        #create a query for our database to use in SQL
        query = "SELECT * FROM users;"
        #call the function that connects to the schema we are using
        #querydb applies the query to the database
        #everything comes back wrapped in dictionaries with lists inside
        results:list[dict] = connectToMySQL('users_emails').query_db(query)
        #results is the list of dictionaries
        user_objects:list[User] = []
        #this for loop will loop through the first list of dictionaries
        #and append the instances from the database, which are all dictionaries
        for user in results:
            user_objects.append(cls(user))

        return user_objects
    
    @classmethod
    def insert_user(cls, data:dict):
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
        connectToMySQL('users_emails').query_db(query, data)