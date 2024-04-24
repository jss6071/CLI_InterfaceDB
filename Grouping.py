import psycopg2

      
def grouping(connection):
    try:
        cursor = connection.cursor()
        
        value1 = input("What table would you like to search?:")
        value2 = input("What column(s) would you like to select from?:")
        value3 = input("What column would you like to group by?:")
        
        #Join query functionality
        grouping_query = """SELECT """ + value2 + """ FROM """ + value1 + """ GROUP BY """ + value3 + """ LIMIT 10"""
        
        #completes operation to join data
        cursor.execute(grouping_query)
        
        #fetch all the rows
        rows = cursor.fetchall()
        
        print("SELECT " + value2 + " FROM " + value1 + " GROUP BY " + value3 + " LIMIT 10")
        
        areyousure = input("This is your query. Is this correct? yes or no.:")
        
        if areyousure == "yes":
            #Display the results on the join search
            if rows:
                print("Results:")
                for row in rows:
                    print(row)
                print("Grouping data searched successfully!")
            else:
                print("No matching records found.")

        if areyousure == "no":
            grouping(connection)
            
    except psycopg2.Error as e:
        connection.rollback()
        print("Error grouping data", e)
    
    finally:
        cursor.close()
        