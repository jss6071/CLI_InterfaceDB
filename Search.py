import psycopg2


def search_data(connection):
    try:
        cursor = connection.cursor()
        
        value1 = input("What table are you selecting?:")
        value2 = input("What column are you selecting (* = all):")
        
        #Select query functionality
        select_query = """SELECT """ + value2 + """ FROM """ + value1 + """ limit 10;"""
        
        #completes operation to search data
        cursor.execute(select_query)
       
        # Fetch all the rows
        rows = cursor.fetchall()
        
        print("SELECT " + value2 + " FROM " + value1 + " limit 10;")
        
        areyousure = input("This is your query. Is this Correct? yes or no.:")
        
        if areyousure == "yes":
            # Display the results of the search
            if rows:
                print("Results:")
                for row in rows:
                    print(row)
                print("Data searched successfully!")
            else:
                print("No matching records found.")
                
        if areyousure == "no":
            search_data(connection)
            
    except psycopg2.Error as e:
        connection.rollback()
        print("Error searching data", e)
    
    finally:
        cursor.close()