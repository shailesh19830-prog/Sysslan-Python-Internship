import csv

def read_csv_file(filename):
    try:
        with open(filename, mode='r') as file:
            # csv.reader reads the file line by line
            reader = csv.reader(file)
            print("--- CSV Data ---")
            for row in reader:
                # Join the columns with a separator for clean output
                print(" | ".join(row))
    except FileNotFoundError:
        print("CSV file not found.")

# Create a dummy CSV file
with open("data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "City"])
    writer.writerow(["1", "Shailesh", "Yavatmal"])
    writer.writerow(["2", "Amit", "Pune"])

read_csv_file("data.csv")