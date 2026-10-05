import csv
from datetime import datetime

def validate_records(records):
    valid_records = []
    rejected_records = []

    for record in records:
        try:
            employee_id = int(record["employee_id"])
            name = record["name"].strip()
            department = record["department"].strip()
            salary = float(record["salary"])
            joining_date = datetime.strptime(record["joining_date"], "%Y-%m-%d").date()

            if not name or not department:
                raise ValueError("Name or department is empty")

            if salary <= 0:
                raise ValueError("Salary must be greater than 0")

            valid_records.append({
                "employee_id": employee_id,
                "name": name,
                "department": department,
                "salary": salary,
                "joining_date": joining_date
            })

        except (ValueError, KeyError) as error:
            rejected_records.append({
                "record": record,
                "reason": str(error)
            })

    return valid_records, rejected_records


if __name__ == "__main__":
    with open("../data/employees.csv", "r") as file:
        records = list(csv.DictReader(file))

    valid, rejected = validate_records(records)

    print("Valid records:", len(valid))
    print("Rejected records:", len(rejected))
