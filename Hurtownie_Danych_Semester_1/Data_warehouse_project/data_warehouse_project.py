# DATA WAREHOUSE PROJECT USING POSTGRESQL (PSYCOPG2 LIBRARY)

#importing all needed libraries and modules
import psycopg2
import random_csv_generator as rcg
import combining_csv_files as ccf

#generating random csv files
amount_csv = input('Insert the value of how many csv files you would like to generate:   ')
rcg.random_csv_generate(int(amount_csv))

#combining the csv files into 1 combined file
ccf.combining_csv_files()

#reading the combined csv file before and after change of ID integers
ccf.combined_csv_reader_ID_changer()


#connection to database

conn = psycopg2.connect('host=localhost dbname=postgres user=postgres password=Matikacp14')

#creating cursor to work with database

cur = conn.cursor()

#deleting the table if already exists to avoid the duplication error
cur.execute("""
    DROP TABLE IF EXISTS people_data""")

#creating table

cur.execute("""
    CREATE TABLE people_data(
    id integer PRIMARY KEY,
    email_id text,
    name text,
    birth_date text,
    phone_number text,
    country text
)
""")

#loading the csv file into database

with open('combined_csv.csv', 'r') as file:
    next(file)
    cur.copy_from(file, 'people_data', sep=',')

conn.commit()
