#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print()
        print('Initializing the program...')
        conn = psycopg2.connect(**params)
        print()
        print("Welcome you beautiful user!")
        
        # create a cursor
        cur = conn.cursor()
        
        menu()
       


    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print()
            print('See you soon you beautiful user!')
            print()
            exit()


def menu():
    print()
    print("Choose one of the following action:")
    print("0. Exit program")
    print("1. Reset the database")
    print("2. Insert new record")
    print()
    choice = input(">>> ")

    if choice == 0:
        pass
    if choice == 1:
        reset_database()

def reset_database():
    # reset = 
    menu()



if __name__ == '__main__':
    connect()