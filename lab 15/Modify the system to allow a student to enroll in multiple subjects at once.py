import sqlite3

# Connect to database
conn = sqlite3.connect('joshi_record.db')
cursor = conn.cursor()

# Drop and create table
cursor.execute('DROP TABLE IF EXISTS joshi_record')
cursor.execute('''
    CREATE TABLE joshi_record (
        Enrollment INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Subject1 TEXT NOT NULL, Mark1 INTEGER NOT NULL,
        Subject2 TEXT NOT NULL, Mark2 INTEGER NOT NULL,
        Subject3 TEXT NOT NULL, Mark3 INTEGER NOT NULL,
        Subject4 TEXT NOT NULL, Mark4 INTEGER NOT NULL,
        Subject5 TEXT NOT NULL, Mark5 INTEGER NOT NULL
    )
''')
conn.commit()

# Corrected data: separate subject and mark values
joshi_record = [
    (92510133013, 'krishna ', 'PWP', 95, 'SS', 95, 'COA', 95, 'ICE', 95, 'DMGT', 52),
    (92510133012, 'diya', 'PWP', 90, 'SS', 92, 'COA', 55, 'ICE', 65, 'DMGT', 53),
    (92510133010, 'isha', 'PWP', 95, 'SS', 75, 'COA', 85, 'ICE', 95, 'DMGT', 62),
    (92510133011, 'rutva', 'PWP', 95, 'SS', 90, 'COA', 65, 'ICE', 85, 'DMGT', 88),
    (92510133009, 'Dipali', 'PWP', 99, 'SS', 55, 'COA', 58, 'ICE', 55, 'DMGT', 55)
]

# Insert into table
cursor.executemany('''
    INSERT INTO joshi_record (
        Enrollment, Name, Subject1, Mark1, Subject2, Mark2,
        Subject3, Mark3, Subject4, Mark4, Subject5, Mark5)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', joshi_record)
conn.commit()

# Fetch and print all records
cursor.execute('SELECT * FROM joshi_record')
rows = cursor.fetchall()
print("All Student Records:")
for row in rows:
    print(row)

# Query students with Mark1 > 90
cursor.execute('SELECT Enrollment, Name, Subject1, Mark1 FROM joshi_record WHERE Mark1 > 90')
high_marks = cursor.fetchall()
print("\nStudents with Mark1 greater than 90:")
for student in high_marks:
    print(student)

# Update Mark1 for krishna 
cursor.execute('''
    UPDATE joshi_record SET Mark1 = 98
    WHERE Name = 'krishna ' AND Subject1 = 'PWP'
''')
conn.commit()

# Verify update
cursor.execute('SELECT Name, Mark1 FROM joshi_record WHERE Name = "krishna "')
updated = cursor.fetchone()
print(f"\nUpdated Mark1 for {updated[0]}: {updated[1]}")

# Delete record for diya
cursor.execute('DELETE FROM joshi_record WHERE Name = "diya"')
conn.commit()
print("\nRecord deleted where Name = 'diya'")
