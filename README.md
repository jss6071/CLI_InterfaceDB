CLI Interface Documentation

GitHub Link: https://github.com/jss6071/CLI_InterfaceDB.git

Demo Video Link: https://psu.zoom.us/rec/play/gMM5D0CBect1523spgbQbmnYPcbZksd87DDPodnb7lKwX9b2DVrCJxNv_Vhh94fFiZJCP5Xxl8ZBCKeE.wTLRPMYA_kIzNssG?canPlayFromShare=true&from=my_recording&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fpsu.zoom.us%2Frec%2Fshare%2FZ4wpzOvZ3PC4yLJwbULOrU8_q8HSLC93N_sHEreP8BWN4GoGK15mXtuC-nSAEJUf.ourJtJzDVQMlUDPi&autoplay=true&startTime=1714000706000

How the codespace is set up

1.	When the code is run, the CLI interface will appear in the command lines. The code connects to the PostgreSQL database using the databaseconnect function, which contains all the PostgreSQL information for the database. 
2.	Once the interface is setup, the interface will pop up asking what query type you would like to enter for the database to interact with it. Whichever number input you select will trigger a next set of input options.
3.	You enter different parts of the query you would like to be accessed, such as the table or the columns within the table or tables. You can also set conditions for these queries if you would like. Some functionalities will display your query after you have entered all inputs. Select yes if it is correct, and no if it is incorrect and not the query you want. 
4.	If yes is selected, the queries will trigger and interact with the database. Inserts, Deletes, and updates will change, add, or remove records within the database and transactions can be used as well. Other functionalities such as Search, group, joins will display information that you like, but limit it to 10 entries to ensure that the command lines are not overloaded with information.
5.	If you wish to exit the database, There is an input (11) that will disconnect you from the database and interface and stop running the code.



 
![image](https://github.com/jss6071/CLI_InterfaceDB/assets/98573527/f5568a06-b4cd-4300-84f1-0074fe8be2b0)
