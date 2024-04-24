import psycopg2


def joins(connection):
    try:
        cursor = connection.cursor()
        
        value1 = input("What table would you like to search?:")
        value2 = input("What column would you like to select?(* = all):")
        value3 = input("What table would you like to join?:")
        value4 = input("What conditions would you like?")
        
        #Join query functionality
        join_query = """SELECT """ + value2 + """ FROM """ + value1 + """ JOIN """ + value3 + """ ON """ + value4 + """ LIMIT 10"""
        
        #completes operation to join data
        cursor.execute(join_query)
        
        #fetch all the rows
        rows = cursor.fetchall()
        
        print("SELECT " + value2 + " FROM " + value1 + " JOIN " + value3 + " ON " + value4 + " LIMIT 10")
        
        areyousure = input("This is your query. Is this correct? yes or no.:")
        
        if areyousure == "yes":
            #Display the results on the join search
            if rows:
                print("Results:")
                for row in rows:
                    print(row)
                print("Joining data searched successfully!")
            else:
                print("No matching records found.")
        
        if areyousure == "no":
            joins(connection)
    
    except psycopg2.Error as e:
        connection.rollback()
        print("Error joining data", e)
    
    finally:
        cursor.close()