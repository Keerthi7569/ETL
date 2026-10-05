def transform_records(records):
    transformed_records = []

    for record in records:
        transformed_records.append({
            "employee_id": record["employee_id"],
            "name": record["name"].title(),
            "department": record["department"].upper(),
            "salary": record["salary"],
            "joining_date": record["joining_date"]
        })

    return transformed_records
