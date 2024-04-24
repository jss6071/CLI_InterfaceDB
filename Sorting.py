import psycopg2


def sorting(connection):
    try:
        cursor = connection.cursor()
        
        value1 = input("What table would you like to search?:")
        value2 = input("What column would you like to select?(* = all):")
        value3 = input("What column would you like to order by?:")
        value4 = input("Would you like to order in ASC(Ascending) or DESC(Descending) order? (Leave blank if neither):")
        
        #Sorting query functionality
        sorting_query = """SELECT """ + value2 + """ FROM """ + value1 + """ ORDER BY """ + value3 + """ """ + value4 + """ LIMIT 10;"""
        
        #completes operation to sort data
        cursor.execute(sorting_query)
        
        #fetch all the rows
        rows = cursor.fetchall()
        
        print("SELECT " + value2 + " FROM " + value1 + " ORDER BY " + value3 + " " + value4 + " LIMIT 10;")
        
        areyousure = input("This is your query. Is this correct? yes or no.:")
        
        if areyousure == "yes":
            #Display the results of the sorting search
            if rows:
                print("Results:")
                for row in rows:
                    print(row)
                print("Sorting data searched successfully!")
            else:
                print("No matching records found.")
        
        if areyousure == "no":
            sorting(connection)
    
    except psycopg2.Error as e:
        connection.rollback()
        print("Error searching data", e)
    
    finally:
        cursor.close()
