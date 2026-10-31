# Using a list of dictionaries to store records
records = []

def add_record(records, name, age):
    record = {"Name": name, "Age": age}
    records.append(record)
    print(f"Added: {name}")

# Adding data
add_record(records, "Shailesh", 22)
add_record(records, "Amit", 21)

# Displaying data
print("\n--- Current Records ---")
for rec in records:
    print(rec)