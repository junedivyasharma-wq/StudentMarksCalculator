def calculate_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

marks = 75
print(calculate_result(marks))