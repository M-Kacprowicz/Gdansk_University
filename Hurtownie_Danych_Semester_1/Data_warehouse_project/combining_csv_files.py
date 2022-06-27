import glob
import csv
import pandas as pd

#combining the csv files into 1 csv file
def combining_csv_files():
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    combined_csv.to_csv('combined_csv.csv', index=False)
#combining_csv_files()

#reading the combined csv file and changing the ID integer to new
def combined_csv_reader_ID_changer():
    file = open('combined_csv.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows)
    number_of_rows = len(rows)
    file.close()
    #changing the ID integer to new
    df = pd.read_csv('combined_csv.csv')
    z: int = 0
    for x in range(0, number_of_rows):
        newIDinteger = x + 1
        df.loc[int(z), 'ID integer'] = f'{newIDinteger}'
        z += 1

    df.to_csv('combined_csv.csv', index=False)

    new_file = open('combined_csv.csv')
    new_csvreader = csv.reader(new_file)
    new_header = next(new_csvreader)
    print(new_header)
    new_rows = []
    for row in new_csvreader:
        new_rows.append(row)
    print(new_rows)
    file.close()

#combined_csv_reader_ID_changer()