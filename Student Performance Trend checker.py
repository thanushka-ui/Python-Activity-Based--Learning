m1 = int(input("Enter first exam marks: "))
m2 = int(input("Enter second exam marks: "))

if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100:
    print("Invalid marks")
else:
    print("First exam:", m1)
    print("Second exam:", m2)

    if m2 > m1:
        print("Performance improved")
    elif m2 < m1:
        print("Performance declined")
    else:
        print("No change in performance")
