import csv

class Support:
    def __init__(self, id: int, customer: str, category: str, priority: str, status: str):
        self.id = id
        self.customer = customer
        self.category = category
        self.priority = priority
        self.status = status

    def __repr__(self):
        return f"Support(id={self.id}, customer={self.customer}, category={self.category}, priority={self.priority}, status={self.status})"

    def 



with open("Labb-Rum-3/supportarenden.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    