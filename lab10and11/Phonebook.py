from re import S
import psycopg2, csv

conn = psycopg2.connect(
  host='localhost', 
  database='postgres',
  port ='5432',
  user='postgres',
  password='postgres'
)
cursor = conn.cursor()

sql_code = """CREATE TABLE contacts (
  id INTEGER,
  PhoneNumber VARCHAR(250) NOT NULL,
  FullName VARCHAR(250) NOT NULL,
  Email VARCHAR(250) NOT NULL,
  PRIMARY KEY (id)
);"""

arr = []

sql = '''
    INSERT INTO contacts
    VALUES (%s, %s, %s, %s);
'''

try:
    with open('a.csv') as f:
        reader = csv.reader(f, delimiter=',')
        
        for row in reader:
            # print(type(row))
            # print(row)
            row[0] = int(row[0])
            arr.append(row)
    for row in arr:
        cursor.execute(sql, row)

except:
    id = int(input("ID:"))

    username = input("Username:")

    number = input("Number:")

    email = input("eMail:")
    cursor.execute(sql, (id, username, number, email))
    
try:
    user_id = input("Enter ID: ")
    to_change = input("What do you want to change?: ")
    data = input("To what value set the old value?: ")
    to_change = to_change.lower()
    if to_change == "username":

        sql = '''
            UPDATE contacts SET username = %s WHERE id = %s;
        '''
        
    if to_change == "number":
        sql = '''
            UPDATE contacts SET number = %s WHERE id = %s;
        '''
        
    if to_change == "email":
        sql = '''
            UPDATE contacts SET email = %s WHERE id = %s;
        '''
    cursor.execute(sql, (data, user_id))
    
except:
    print("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
sql1 = '''
    SELECT * FROM contacts;
'''
cursor.execute(sql1, [])
table = cursor.fetchall()

for i in table:
    print(*i, sep = "     ")
print("~~~~~~")
id_number = input("ID:")
column = input("What do you want to see?  Print '*' if you want to see full information: ")
if column == '*':

    sql = '''
        SELECT * from contacts
        WHERE id = %s;

    '''
    cursor.execute(sql, [id_number])

    data = cursor.fetchone()
    
    print(f"ID: {data[0]}")
    print(f"Username: {data[1]}")
    print(f"Phone number: {data[2]}")
    print(f"Email: {data[3]}")

else:
    if column == "username":
        sql = '''
            SELECT username from contacts
            WHERE id = %s;
        '''
        cursor.execute(sql, [id_number])
    if column == "number":
        sql = '''
            SELECT number from contacts
            WHERE id = %s;
        '''
        cursor.execute(sql, [id_number])
    if column == "email":
        sql = '''
            SELECT email from contacts
            WHERE id = %s;
        '''
        cursor.execute(sql, [id_number])
    data = cursor.fetchone()
    print(*data)
    
id_number = input("ID:")
sql = '''
    DELETE FROM contacts
    WHERE id = %s;

'''
cursor.execute(sql, (id_number))
    
cursor.execute(sql_code)
conn.commit()
