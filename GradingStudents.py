def gradingStudents(grades):
    # Write your code here
    output = []
    for index,grade in enumerate(grades):
        if grade < 38 or grade % 5 < 3:
            output.append(grade)
        else: 
            output.append(grade + 5 - (grade % 5 ))
    return output
