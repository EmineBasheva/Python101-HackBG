import sqlite3


connect = sqlite3.connect('company.db')
cursor = connect.cursor()
create_company_table = cursor.execute("CREATE TABLE IF NOT EXISTS company(id INTEGER PRIMARY KEY,\
 name TEXT, monthly_salary TEXT, yearly_bonus int, position TEXT)")

result = cursor.execute("INSERT\
                        INTO company(name, monthly_salary, yearly_bonus, position)\
                        VALUES('Ivan Ivanov', 5000, 10000, 'Software Developer'),\
                        	  ('Rado Rado', 500, 0, 'Technical Support Intern'),\
                        	  ('Ivo Ivo', 10000, 100000, 'CEO'),\
                        	  ('Petar Petrov', 3000, 1000, 'Marketing Manager')")

connect.commit()
cursor.close()
