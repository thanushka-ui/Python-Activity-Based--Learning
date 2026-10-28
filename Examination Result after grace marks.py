marks = int(input("Enter marks out of 100: "))

if marks >= 40:
    print("Pass")
elif marks >= 35:
    grace = 40 - marks
    print("Pass after grace marks:", grace)
else:
    print("Fail")