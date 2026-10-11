def result(marks):
    total_marks = 0

    for mark in marks:
        total_marks += mark

    print("Total Marks: ",total_marks)

    percentage = total_marks/500
    print("Percentage", round(percentage*100, 3))

    for mark in marks:
        if mark > 90:
            print("A+")
        elif mark > 80:
            print("A")
        elif mark >70:
            print("B")
        elif mark >60:
            print("C")
        elif mark >50:
            print("D")
        elif mark >35:
            print("P")
        else:
            print("F")
        if len(marks) != 5:
                print("Input marks properly, missing value")

    

    
