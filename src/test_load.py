import csv
from load import load_records

with open("../data/employees.csv") as file:
    records = list(csv.DictReader(file))

for r in records:
    r["employee_id"] = int(r["employee_id"])
    r["salary"] = float(r["salary"])

count = load_records(records)
print("Records inserted:", count)
