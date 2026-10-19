import csv

class Support:
    def __init__(self, id: int, customer: str, category: str, priority: str, status: str):
        self.id = id
        self.customer = customer
        self.category = category
        self.priority = priority
        self.status = status

    def __repr__(self):
        return f"Support(id={self.id}, customer={self.customer!r}, category={self.category!r}, priority={self.priority!r}, status={self.status!r})"

    def __str__(self):
        return f"ID: {self.id}, customer: {self.customer}, category: {self.category}, priority: {self.priority}, status: {self.status}"

    def is_open(self):
        return self.status == "Öppet"


support_cases = []

with open("Labb-Rum-3/supportarenden.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        case = Support(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )

        support_cases.append(case)

for case in support_cases:
    if case.is_open():
        print(case)