import psycopg2

try:
    connection = psycopg2.connect(database='staff', user = "nec",
                                  password = 'papa7579', host = '127.0.0.1',
                                  port = "5432")
except psycopg2.Error as e:
    print("An error was generated!")
else:
    print("Connection to database was successfull!")

cursor = connection.cursor()
"""
query = '''create table mystaff.employees
        (id int primary key not null,
        first_name varchar(25) not null,
        last_name varchar(25) not null,
        department varchar(25) not null,
        phone varchar(25),
        address varchar(50),
        salary int);'''
"""
'''
query = """insert into mystaff.employees (id,first_name,last_name,department,
        phone,address,salary) values (1, 'john','smith','sales','897656',
        '1st street','2345'),
        (2,'smith','doe','iT','2345','2st street','2345678');"""
        
query = """update mystaff.employees set department = 'Logistics' where last_name ='doe
';"""

query = """delete from mystaff.employees where salary > 5000;"""
cursor.execute(query)
'''
f = open("C:\\Users\\admin\\Desktop\\PY\\employee.txt")
records = []
for i in f.readlines():
    records.append(i.split("/"))

try:
    for i in records:
        cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) values (%s,%s,%s,%s,%s,%s,%s);",(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
except psycopg2.Error as e:
    print("An error was generated while inserting the records!")
else:
    print("Records inserted successfully!\n")

connection.commit()
connection.close()
