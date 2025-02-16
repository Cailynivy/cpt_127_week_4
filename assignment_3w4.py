'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv

'''
with open('student_grades.csv','r') as f:

    # collect all lines from the file
    lines = f.readlines()


    # validate file has data
    if len(lines) > 0:
        grades = []
        person = []
        # iterate through each line and collect the grade
        # skipping the first 'header' line
        for line in lines[1:]:
            person.append(line.replace('\n',''))
            # split the line into a list (i.e. columns)
            row = line.split(',')

            # convert the grade to a float and add it to the list
            grades.append(float(row[3].replace('\n','')))

        avg = sum(grades) / len(grades)

with open('student_grade_differences.csv','w') as s:
    # clears file
    s.truncate()
    # writes header
    s.write(f'id,first_name,last_name,grade,difference\n')
    s.close()
with open('student_grade_differences.csv','a') as s:
    if len(person) > 0:
        dif = []
        for line in person[0:]:
            row = line.split(',')
            # difference of grade - average
            dif = (float(row[3])) - (float(avg))
            # writes current line to file
            s.write(str(line))
            s.write (f', {dif}')
            s.write("\n")

