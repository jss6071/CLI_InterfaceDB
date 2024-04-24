import psycopg2

#function for updating data
def update_data(connection):
    try:
        cursor = connection.cursor()
        
        value1 = input("What column do you want to update and update to what? Example: title = 'Test Movie':")
        value2 = input("What are the conditions of your update? (Use a comma to seperate them):")
        
        #Update  query functionality
        update_query = """UPDATE netflixmovietv SET """ + value1 + """ WHERE """ + value2 + """;"""

        print("UPDATE netflixmovietv SET " + value1 + " WHERE " + value2 + ";")
        
        areyousure = input("This is your query. Is this Correct? yes or no.:")
        
        if areyousure == "yes":
            #completes operation to update data
            cursor.execute(update_query)
            connection.commit()
            print("Data updated successfully!")
        
        if areyousure == "no":
            update_data(connection)
        
        
    except psycopg2.Error as e:
        connection.rollback()
        print("Error updating data:", e)
    
    finally:
        cursor.close()    
    