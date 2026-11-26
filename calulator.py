def calculate_result(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

marks = 75
print(calculate_result(marks))