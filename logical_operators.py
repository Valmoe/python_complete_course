"""
if applicant has high income AND good credit
    eligible for loan
    AND and OR and AND NOT conditions
"""
has_high_income = True
has_good_credit = True
criminal_record = True

if has_high_income and not criminal_record :
    print("Eligible for Loan")
else:
    print("Not Eligible for loan. Try again after 7 days")