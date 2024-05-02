# Flat-File Database - CSV file

- data can often be described in patterns of columns and tables.
- Spreadsheets like those created in Microsoft Excel and Google Sheets can be outputted to a csv or comma-separated values file.
-  If you look at a csv file, you’ll notice that the file is flat in that all of our data is stored in a single table represented by a text file. We call this form of data a flat-file database.
- Python comes with native support for csv files.

## 1. favorites  📚 → [favorites.py](https://github.com/AkiMadi16/14Days_of_python/blob/main/csv_file.py/favorites.py) 
- `import csv` library
- we created a reader that will hold the results 
- `csv.reader` function reads the each row from the file, we declared a variable called reader to initiate all data of rows from the file.


## 2. next  → [next.py](https://github.com/AkiMadi16/14Days_of_python/blob/main/csv_file.py/next.py) 
- the `next` function is used to skip to the next line of our reader 


## 3. DictReader { } → [DictReader.py](https://github.com/AkiMadi16/14Days_of_python/blob/main/csv_file.py/DictReader.py) 
- `DictReader` is a class in Python's `csv` module that allows you to read CSV files as dictionaries. It reads each row of the CSV file as a dictionary where the keys are the column headers and the values are the corresponding values in the row.


    | ID                                                    | Name | Age               |
    | ----------------------------------------------------------- | --------------- | ---------------------- |
    | 001 | Aki Madi     | 10 |
    | 002| Thili Aki  | 35 |





``` diff
import csv

# Assuming you have a CSV file named 'data.csv' with columns 'name' and 'age'
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['age'])
```

In this example, each row variable is a dictionary where you can access values by their column names, such as row['name'] and row['age']. This makes it easier to work with CSV data, especially when dealing with files that have many columns.



## 4. count ⩲ → [counts.py](https://github.com/AkiMadi16/14Days_of_python/blob/main/csv_file.py/counts.py) 
- this file directly utilizes the title key in the print 
- count the total of same title we need exist in the file
- for that we initiate the value of item(i.e- title) we need as zero and iterarte through the file and adding one to the same title exists in the file
- then we print the items we need using print function 


## 5. sort 🔡 → [sortEachItem.py](https://github.com/AkiMadi16/14Days_of_python/blob/main/csv_file.py/sortEachItem.py) 
- python allows sorting the total we take as counts
- https://docs.python.org/3/howto/sorting.html
- check `sorted` function in the python documentation.

# Relational Databases

- Relational databases store data in rows and columns in structures called tables.
- SQL allows for four types of commands:
        Create
        Read
        Update
        Delete

- created a SQL database at the terminal by typing 
 
           $ sqlite favorites.db 
           $ favorites.db
           sqlite3> .mode csv
           sqlite3> .import favorites.csv favorites
           sqlite3> .schema
           sqlite3> SELECT columns FROM table;
            ** ^--- error here
           sqlite3> SELECT * FROM favorites;
           sqlite3> SELECT title FROM favorites;
           sqlite3> SELECT COUNT(title) FROM favorites;
           sqlite3> SELECT COUNT(DISTINCT(title)) FROM favorites;
           sqlite3> SELECT COUNT(*) FROM favorites WHERE title = 'Friends'

           🌟 To exit sqlite3 press control + D or exit


## 1. Modified code 🔡 → [db.py](https://github.com/AkiMadi16/14Days_of_python/blob/main/csv_file.py/db.py) 
- CS50 library will assist with the complicated steps of utilizing SQL within your Python code.
- line that begins with rows executes SQL commands utilizing `db.execute`
- `rows` is returned as a list of dictionaries. In this case, there is only one result, one row, returned to the rows list as a dictionary.