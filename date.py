from datetime import datetime, timedelta

data = datetime.now()

print("Date and Time: ", data)
print("Year: ", data.year)
print("month: ", data.strftime("%b"))
print("days: ", data.strftime("%a"))


class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.borrow_date = None
        self.return_date = None
    def borrow(self):
        self.borrow_date = datetime.now()
        self.return_date = self.borrow_date + timedelta(days=14)
        print(f"{self.title} borrowed on {self.borrow_date.strftime('%Y-%m-%d')}.")
        print(f"Due Date is {self.return_date.strftime('%Y-%m-%d')}")




br_book = LibraryBook("Atomic Habit")
print(br_book.borrow())