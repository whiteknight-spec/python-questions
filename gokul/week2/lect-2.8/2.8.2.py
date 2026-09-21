# take year of birth (YOB) as input,
# print the current age of the person and also print if the person is eligible to vote or not


# HINT : subtract current year from YOB

YOB=int(input("year of birth:"))
x=2026-YOB
if x>=18:
    print(x)
    print("eligible to vote")
else:
    print(x)
    print("not eligible")    