# https://www.programmingexpert.io/programming-fundamentals/assessment/3

# employees is a list of employee ["name", age, salary] (str, int, int)
# sort_by is always "age", "name" or "salary"

def sort_employees(employees, sort_by):
    sorted_employees = []

    for employee in employees:
        sort_Helper(sorted_employees, employee, sort_by)

    return sorted_employees


def sort_Helper(sorted_employees, employee, sort_by):
    if len(sorted_employees) == 0:
        sorted_employees.append(employee)
        return

    if sort_by == "name":
        idx = 0
    elif sort_by == "age":
        idx = 1
    elif sort_by == "salary":
        idx = 2

    first = sorted_employees.pop()
    if employee[idx] > first[idx]:
        sorted_employees.append(first)
        sorted_employees.append(employee)
    else:
        sort_Helper(sorted_employees, employee, sort_by)
        sorted_employees.append(first)
