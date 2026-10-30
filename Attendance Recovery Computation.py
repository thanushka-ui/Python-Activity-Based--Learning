total_classes = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))

if total_classes <= 0 or attended < 0 or attended > total_classes:
    print("Invalid attendance details")

else:
    percentage = (attended / total_classes) * 100

    print("Current attendance:", percentage, "%")

    if percentage >= 75:
        print("You are eligible for exams")

    else:
        print("You are not eligible yet")

        future_classes = 0

        while ((attended + future_classes) /
               (total_classes + future_classes)) * 100 < 75:
            future_classes = future_classes + 1

        print("Minimum classes to attend:", future_classes)
        print("Attend all these classes to reach 75%")
