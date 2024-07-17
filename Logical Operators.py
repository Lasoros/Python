#and or not

high_income = True
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible for a loan")
else:
    print("Ineligible for loan")