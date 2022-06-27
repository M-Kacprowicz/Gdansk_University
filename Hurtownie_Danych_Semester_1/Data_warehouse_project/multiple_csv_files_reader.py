import csv

#Reading the 10 random generated csv files
def multiple_csv_files_reader():
    for i in range(1,11):
        file = open(f"People_data{i}.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        file.close()