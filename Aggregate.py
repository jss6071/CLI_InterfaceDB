import psycopg2

       
def aggregate_function(connection):
    try:
        cursor = connection.cursor()
        
        value1 = input("What table are you searching?:")
        value2 = input("What is the aggregate function?:")
        value3 = input("What is the column you are selecting?(* = all):")
        
        #Aggregate query functionality
        aggregate_query = """SELECT """ + value2 + """(""" + value3 + """)""" + """ FROM """ + value1 + """;"""
        
        #completes operation to aggregate data
        cursor.execute(aggregate_query)
        
        #fetch all the rows
        rows = cursor.fetchall()
        
        print("SELECT " + value2 + "(" + value3 + ")" + " FROM " + value1 + ";")
        
        areyousure = input("This is your query. Is this correct? yes or no.:")
        
        if areyousure == "yes":
            #Display the results of the aggregate search
            if rows:
                print("Results:")
                for row in rows:
                    print(row)
                print("Aggregate data searched successfully!")
            else:
                print("No matching records found.")
                
        if areyousure == "no":
            aggregate_function(connection)
            
    except psycopg2.Error as e:
        connection.rollback()
        print("Error searching data", e)
    
    finally:
        cursor.close()
