import psycopg2


#Connects the database with the CLI Interface
def databaseconnect():
    connection = ()

    try:
        connection = psycopg2.connect(
            dbname="netflixmovietv",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        print("Connection to database successful")
    
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
                     
    return connection