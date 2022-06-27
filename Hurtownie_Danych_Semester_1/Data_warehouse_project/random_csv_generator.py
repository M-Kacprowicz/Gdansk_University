import csv
from faker import Faker
import datetime

#Generating 10 random csv files with data about random (not existing people)

def datagenerate(records, headers, number_of_csv_files):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')  # To generate phone numbers
    for z in range(1, number_of_csv_files + 1):
        with open(f"People_data{z}.csv", 'wt') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=headers)
            writer.writeheader()
            for i in range(records):
                full_name = fake.name()
                FLname = full_name.split(" ")
                Fname = FLname[0]
                Lname = FLname[1]
                domain_name = "@testDomain.com"
                userId = Fname + "." + Lname + domain_name
                Idinteger = i + 1

                writer.writerow({
                    "ID integer": Idinteger,
                    "Email Id": userId,
                    "Name": fake.name(),
                    "Birth Date": fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)),
                    "Phone Number": fake1.phone_number(),
                    "Country": fake.country(),
                })

def random_csv_generate(number_of_csv_files):
    for l in range (1, int(number_of_csv_files) + 1):
        # if __name__ == '__main__':
        records = 50
        headers = ["ID integer", "Email Id", "Name", "Birth Date", "Phone Number", "Country"]
        datagenerate(records, headers, number_of_csv_files)
        print("CSV generation complete!")
#random_csv_generate(10)
