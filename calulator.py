def calculate_result(marks):
    if marks >= 33:
        return "Pass"
    else:
        return "Fail"

marks = 75
print(calculate_result(marks))