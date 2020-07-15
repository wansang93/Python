import csv

file_path = ('C:/Users/wansang/Desktop/Gitrep/Python/'
    'How to use Python in Silicon Valley/08. File IO and System/test.csv')
    
with open(file_path, 'w', newline='') as csv_file:
    field_name = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, field_name)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

with open(file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])