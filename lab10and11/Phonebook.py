from re import S
import psycopg2, csv

config = psycopg2.connect(
  host='localhost', 
  database='postgres',
  port ='5432',
  user='postgres',
  password='postgres'
)

current = config.cursor()

sql_code = """CREATE TABLE contacts (
  id INTEGER,
  Name VARCHAR(250) NOT NULL,
  Number VARCHAR(250) NOT NULL,
  Email VARCHAR(250) NOT NULL
  created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP 
);"""

def insert():

    insert_table = '''

        INSERT INTO contacts VALUES(%s,%s,%s,%s);

    '''

    flag = input('yes если хотите ввести через терминал, no иначе: ')

    if flag == "yes":
        
        id=str(input("Введите user ID:"))

        name = str(input("Введите имя: "))

        number = str(input("Введите номер телефона: "))
        
        email = str(input("Введите почту:"))
        
        current.execute(insert_table, (id,name,number,email))




    if flag == "no":

        with open("a.csv", "r") as file:

            f = csv.reader(file, delimiter=",")

            for row in f:

                current.execute(insert_table,row)

        config.commit()

def delete():

    delete = """

    DELETE FROM contacts WHERE name = %s;

    """

    name = str(input("Введите имя: "))

    current.execute(delete,[name])

def update():


    id = input("Введите user ID: ")
    to_change = input("Что вы хотите поменять? ")
    data = input("To what value set the old value?: ")
    to_change = to_change.lower()
    
    if to_change == "name":

        update = '''
            UPDATE contacts SET name = %s WHERE id = %s;
        '''
        
    if to_change == "number":
        update = '''
            UPDATE contacts SET number = %s WHERE id = %s;
        '''
        
    if to_change == "email":
        update = '''
            UPDATE contacts SET email = %s WHERE id = %s;
        '''
    current.execute(update, (data, id))
    config.commit()


def select():

    select = """

    SELECT * FROM contacts;

    """

    current.execute(select)

    print(current.fetchall(), sep='\n')

    config.commit()

while True:

    command = str(input("insert,update,delete,select,exit: \n"))

    if command == 'insert':

        insert()

    if command == 'delete':

        delete()

    if command == 'update':

        update()

    if command == 'select':

        select()

    if command == 'exit':

        break


current.close()

config.commit()

config.close()
