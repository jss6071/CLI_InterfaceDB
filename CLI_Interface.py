import psycopg2
from Insert import insert_data
from Delete import delete_data
from Update import update_data
from Search import search_data
from Aggregate import aggregate_function
from Sorting import sorting
from Joins import joins
from Grouping import grouping
from Subqueries import subqueries
from Transaction import transaction
from DBconnect import databaseconnect
                   
def main():
    # connect to the database
    connection = databaseconnect()
    
    if connection is None:
        return
    
    while True:
        
        print("Welcome to Jameel Saccoh's Database CLI Interface.")
        print("")
        print("Select from the following options:")
        print("1. Insert Data")
        print("2. Delete Data")
        print("3. Update Data")
        print("4. Search Data")
        print("5. Aggregate Functions")
        print("6. Sorting")
        print("7. Joins")
        print("8. Grouping")
        print("9. Subqueries")
        print("10. Transactions")
        print("11. Exit")
        choice = input("Enter your choice: ")
        
        # This choice inserts data into the tables
        if choice == "1":
            insert_data(connection)
            return
         
        #This choice deletes data from tables
        elif choice == "2":
            delete_data(connection)
            return   
        
        elif choice == "3":
            update_data(connection)
            return
        
        elif choice == "4":
            search_data(connection)
            return
        
        elif choice == "5":
            aggregate_function(connection)
            return
        
        elif choice == "6":
            sorting(connection)
            return
        
        elif choice == "7":
            joins(connection)
            return
        
        elif choice == "8":
            grouping(connection)
            return
        
        elif choice == "9":
            subqueries(connection)
            return
        
        elif choice == "10":
            transaction(connection)
            return
        
        # This Choice closes the connection to the database.
        elif choice == "11":
            connection.close()
            print("Connection closed")
            return
            
        else:
            print("Choice unavaiable. Try again.")

if __name__ == "__main__":
    main()
