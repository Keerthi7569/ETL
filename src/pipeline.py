import csv
from validate import validate_records
from transform import transform_records
from load import load_records
from audit import audit_success

try:
    with open("../data/employees.csv", "r") as file:
        records = list(csv.DictReader(file))

    valid, rejected = validate_records(records)
    transformed = transform_records(valid)
    inserted = load_records(transformed)

    audit_success(len(records), inserted, len(rejected))

    print("Pipeline completed successfully")
    print("Records read:", len(records))
    print("Valid records:", len(valid))
    print("Rejected records:", len(rejected))
    print("Records inserted:", inserted)

except Exception as error:
    print("Pipeline failed:", error)
    raise
