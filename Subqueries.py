import psycopg2


def subqueries(connection):
    try:
        cursor = connection.cursor()
        
        value1 = input("What table would you like to search from?:")
        value2 = input("What column(s) would you like to search from?:")
        value3 = input("What column would you like to search in a subquery?:")
        value4 = input("What table would you like to search in your subquery?")
        value5 = input("What column would you like to search in your subquery?")
        
        #Join query functionality
        subqueries_query = """SELECT """ + value2 + """ FROM """ + value1 + """ WHERE """ + value3 + """ IN (SELECT """ + value5 + """ FROM """ + value4 + """) LIMIT 10"""
        
        #completes operation to subquery data
        cursor.execute(subqueries_query)
        
        #fetch all the rows
        rows = cursor.fetchall()
        
        print("SELECT " + value2 + " FROM " + value1 + " WHERE " + value3 + " IN (SELECT " + value5 + " FROM " + value4 + ") LIMIT 10")
        
        areyousure = input("This is your query. Is this correct? yes or no.:")
        
        if areyousure == "yes":
            #Display the results on the subquery search
            if rows:
                print("Results:")
                for row in rows:
                    print(row)
                print("Subquery data searched successfully!")
            else:
                print("No matching records found.")
                
        if areyousure == "no":
            subqueries(connection)
    
    except psycopg2.Error as e:
        connection.rollback()
        print("Error subquerying data", e)
    
    finally:
        cursor.close()
