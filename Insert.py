import psycopg2

# function for inserting data
def insert_data(connection):
    try:
        cursor = connection.cursor()
        
        # Insert query functionality
        insert_query = """INSERT INTO netflixmovietv (show_id, type, title, director, "cast", country, date_added, release_year, rating, duration, listed_in, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        value2 = input("What is the show_id?:")
        value3 = input("What is the type?:")
        value4 = input("What is the title?:")
        value5 = input("Who is the director(s)?:")
        value6 = input("Who is in the cast?:")
        value7 = input("What Country is the film location?:")
        value8 = input("What is the date_added:")
        value9 = input("When was the release_year?:")
        value10 = input("What is the rating?:")
        value11 = input("What is the duration?:")
        value12 = input("What is the genre?:")
        value13 = input("What is the description?:")
        
        # Data inserted into table
        data = (value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13)
        
        print("INSERT INTO netflixmovietv (show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description) VALUES ("+ value2 + "," + value3 + "," + value4 + "," + value5 + "," + value6 + "," + value7 + "," + value8 + "," + value9 + "," + value10 + "," + value11 + "," + value12 + "," + value13 + ")")
        
        areyousure = input("This is your query. Is this Correct? yes or no.:")
        
        if areyousure == "yes":
          # Completes operation to insert data  
          cursor.execute(insert_query, data)  
          
          connection.commit()
        
          print("Data inserted successfully!")
        
        if areyousure == "no":
            insert_data(connection)
        
    except psycopg2.Error as e:
        connection.rollback()
        print("Error inserting data:", e)

    finally:
        cursor.close()

