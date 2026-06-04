from faker import Faker
import csv

fake = Faker()

with open('test_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'lastname'])
    for _ in range(600):
        writer.writerow([fake.first_name(), fake.last_name()])

print("Файл test_data.csv создан с 600 строками!")