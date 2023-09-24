month = input("Введите название месяца на английском.").lower()
date = int(input("Введите число."))
months = {"january": 31, "february": 28, "march": 31,
          "april": 30, "may": 31, "june": 30, "july": 31,
          "august": 31, "september": 30, "october": 31,
          "november": 30, "december": 31}
if month in months and months.get(month) >= date:
    print("True")
else:
    print("False")
