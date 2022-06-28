#SQL PROJECT USING POSTGRESQL (PSYCOPG2 LIBRARY)

#importing all needed libraries and modules
import psycopg2

#connection to database

conn = psycopg2.connect('host=localhost dbname=NFLdata user=postgres password=Matikacp14')

#creating cursor to work with database

cur = conn.cursor()

#deleting the table if already exists to avoid the duplication error
cur.execute("""
    DROP TABLE IF EXISTS nfl_data""")

#creating table

cur.execute("""
    CREATE TABLE nfl_data(
    Year smallint,
    Age smallint,
    Height float(2),
    Weight float(1),
    Sprint_40yd float(2),
    Vertical_Jump float(2),
    Bench_Press_Reps smallint,
    Broad_Jump float(2),
    Agility_3cone float(2),
    Shuttle float(2),
    BMI float(5),
    Player_Type text,
    Position_Type text,
    Position text,
    Drafted bool,
    Age_imp boolean,
    Agility_3cone_imp boolean,
    Shuttle_imp boolean,
    Bench_Press_Reps_imp boolean,
    Broad_Jump_imp boolean,
    Vertical_Jump_imp boolean,
    Sprint_40yd_imp boolean,
    Id integer PRIMARY KEY
)
""")


#loading the csv file into database

with open('dane_imputowane.csv', 'r') as file:
    next(file)
    cur.copy_from(file, 'nfl_data', sep=',')

conn.commit()
