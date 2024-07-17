#short circuit evaluators stops as soon as one operator returns false
# and stops at first false, or will look for true on either side of if not will be false
#see code below


high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible for a loan")
else:
    print("Ineligible for loan")