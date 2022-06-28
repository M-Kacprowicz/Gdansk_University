#SQL PROJECT USING POSTGRESQL (PSYCOPG2 LIBRARY)

#importing all needed libraries and modules
import psycopg2

#connection to database

conn = psycopg2.connect('host=localhost dbname=NFLdata user=postgres password=Matikacp14')

#creating cursor to work with database

cur = conn.cursor()

#Queries
cur.execute("""
    SELECT age, bmi, weight, height, player_type FROM nfl_data WHERE sprint_40yd<4.3
""")
rows_1 = cur.fetchall()
print("Parametry zawodnikow, ktorzy pokojnuja sprint na 40 jardow w mniej niz 4.3s:")
for row in rows_1:
    print("wiek =", row[0])
    print("bmi =", row[1])
    print("waga =", row[2], "kg")
    print("wzrost =", row[3], "m")
    print("typ zawodnika =", row[4], "\n")

cur.execute("""
    SELECT bench_press_reps, id FROM nfl_data WHERE bench_press_reps_imp = true
""")
rows_2 = cur.fetchall()
for row in rows_2:
    print(f"Zmienna bench_press_reps zostala zaimputowana dla wiersza numer {row[1]}. Imputowana wartosc =", row[0])
print(f"Zaimputowano {len(rows_2)} pozycji.\n")

cur.execute("""
    SELECT * FROM nfl_data WHERE age_imp=true OR agility_3cone_imp=true OR shuttle_imp=true OR bench_press_reps_imp=true OR broad_jump_imp=true OR vertical_jump_imp=true OR sprint_40yd_imp=true
""")
rows_3 = cur.fetchall()
print(f"W {len(rows_3)} wierszach zaimputowano przynajmniej jedną zmienną.\n")

cur.execute("""
    SELECT DISTINCT age, bmi, weight, height FROM nfl_data WHERE weight=(SELECT MAX(weight) FROM nfl_data)
""")
rows_4 = cur.fetchall()
for row in rows_4:
    print(f"Najciezszy zawodnik z bazy danych ma {row[0]} lat/a wazy {row[2]} kilogramow! Jego bmi to {row[1]}, a wzrost to {row[3]}m.\n")

cur.execute("""
    SELECT age, avg(sprint_40yd), avg(vertical_jump), avg(bench_press_reps), avg(broad_jump), avg(agility_3cone), avg(shuttle)
    FROM nfl_data
    GROUP BY age
    ORDER BY age
""")
rows_5 = cur.fetchall()
for row in rows_5:
    print(f"""Zawodnicy w wieku {row[0]} lat pokonuja sprint na 40 jardow srednio w {round(row[1], 2)}s, 
skacza pionowo srednio na wysokość {round(row[2], 2)}cm, 
wyciskaja na lawce srednio {round(row[3], 0)} powtorzen, 
skacza w dal srednio na odleglosc {round(row[4], 2)}cm, 
pokonuja test 3 rozkow na zwinnosc srednio w {round(row[5], 2)}s, 
a bieg pomiedzy 2 slupkami srednio koncza w {round(row[6], 2)}s.\n""")

conn.commit()
