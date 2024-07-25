#developer: Abednego Dunyah
#date: 24/07/2024

# function to read from student.txt
def read_func(filename):
    '''
    opens students.txt file
    read each line
    split each line to get students data based on instruction given
    returns tuple of each student's data 

    '''

    with open(filename, 'r') as students:
        lines = students.readlines()

    #read students data from students.txt file and return as it as tuple
    students_data = []
    for line in lines:
        parts = line.strip().split()
        #get name, assignment score, quiz score, mid semester score and exam score
        name = parts[0]
        assignment_score = int(parts[1])
        quiz_score = int(parts[2])
        mid_sem_score = int(parts[3])
        exams_score = int(parts[4])
        students_data.append((name, assignment_score, quiz_score, mid_sem_score, exams_score))
        
    return students_data