#student grade tracker
marks = float(input("please enter the marks (0-100): "))

#marks and grades
if 0 <= marks <= 100:
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print("Grade:" , grade)
else:
    print("Invalid marks. please enter a value between 0 and 100.")
            
