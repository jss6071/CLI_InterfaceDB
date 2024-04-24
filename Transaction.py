import psycopg2


def transaction(connection):
    try:
        cursor = connection.cursor()

        value1 = input("Enter your first query: ")
        value2 = input("Do you have any more queries?(yes or no): ")
        
        if value2 == "yes":
            value3 = input("Enter your second query: ")
            cursor.execute("BEGIN;")
            #Transaction query functionality
            update_query_yes = value1 + """ \n""" + value3
        
            # Execute the update statement
            cursor.execute(update_query_yes)
        
            # Commit the transaction
            cursor.execute("COMMIT;")
        
            print("Transaction completed successfully!") 
            
            
        if value2 == "no":
            cursor.execute("BEGIN;")
        
            #Transaction query functionality
            update_query_no = value1
        
            # Execute the update statement
            cursor.execute(update_query_no)
        
            # Commit the transaction
            cursor.execute("COMMIT;")
        
            print("Transaction completed successfully!") 
        
        

    except psycopg2.Error as e:
        cursor.execute("ROLLBACK;")
        print("Error performing transaction:", e)

    finally:
        cursor.close()
        