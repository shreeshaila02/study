from datetime import datetime

subjects = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    sub = input(f"Enter subject {i+1}: ")
    subjects.append(sub)

exam_date = input("Enter exam date (YYYY-MM-DD): ")
today = datetime.today()

exam = datetime.strptime(exam_date, "%Y-%m-%d")

days_left = (exam - today).days

if days_left <= 0:
    print("Exam date already passed or today!")
else:
    print("\n📚 Study Plan:\n")

    per_day = max(1, len(subjects) // days_left + 1)

    day = 1
    index = 0

    while index < len(subjects):
        print(f"Day {day}:")

        for i in range(per_day):
            if index < len(subjects):
                print(" -", subjects[index])
                index += 1

        day += 1
        print()