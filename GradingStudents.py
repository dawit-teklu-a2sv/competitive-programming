def gradingStudents(grades):
    # Write your code here
    output = []
    for index,grade in enumerate(grades):
        next_multiple = (( grade // 5 ) + 1) * 5                        
        if grade < 38:
            output.append(grade)
        elif next_multiple  - grade  < 3:
            output.append(next_multiple)
        else:
            output.append(grade)
    return output
