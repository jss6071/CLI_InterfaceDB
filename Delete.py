import psycopg2

# function for inserting data
def delete_data(connection):
    try:
        cursor = connection.cursor()
        
        deltable = input("What Table are you deleting from?:")
        
        value1 = input("What are your conditions? (Use a comma to seperate them):")
        data = value1
        
        # Delete query functionality
        delete_query = """DELETE FROM """ + deltable + """ WHERE """ + data + """;"""
        
        
        print("DELETE FROM " + deltable + " WHERE " + data)
        
        areyousure = input("This is your query. Is this Correct? yes or no.:")
        
        if areyousure == "yes":
          # Completes operation to insert data  
          cursor.execute(delete_query, data)  
          
          connection.commit()
        
          print("Data deleted successfully!")
        
        if areyousure == "no":
            delete_data(connection)
        
    except psycopg2.Error as e:
        connection.rollback()
        print("Error deleting data:", e)

    finally:
        cursor.close()