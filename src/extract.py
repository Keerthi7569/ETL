import csv
file_path = "../data/employees.csv"
with open(file_path, "r") as file: 
    reader = csv.DictReader(file)
    records = list(reader)
print("Records extracted:", len(records))
