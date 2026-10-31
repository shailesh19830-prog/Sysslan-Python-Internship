import json

def save_records(filename, data):
    # Using JSON to easily save dictionaries to a file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("Records saved successfully.")

def load_records(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

# Save data
student_records = [{"ID": 1, "Name": "Shailesh"}, {"ID": 2, "Name": "Riya"}]
save_records("records.json", student_records)

# Retrieve data
loaded_data = load_records("records.json")
print("Retrieved Data:", loaded_data)