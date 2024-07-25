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

#funtion to calculate cumulative assessment of student
def calculate_cumulative_score_of_student(a_scores, q_scores, m_scores, e_scores):
    '''
    calculates students cumulative scores
    return it as total score

    '''
    total_score = a_scores + q_scores + m_scores + e_scores
    return total_score

#function to calculate and save cumulative scores of students
def calc_save_cumulative_scores(input_filename, output_filename):
    '''
    reads scores from input filname
    calculates cumulative scores of students
    saves results to output filename

    '''
    students_data = read_func(input_filename)

    with open(output_filename, 'w') as output_file:
        for student_data in students_data:
            student_name = student_data[0]
            assignments_score = student_data[1]
            quiz_score = student_data[2]
            midsem_score = student_data[3]
            exams_score = student_data[4]
            
            cumulative_score = calculate_cumulative_score_of_student(assignments_score, quiz_score, midsem_score, exams_score)
            output_file.write(f'{student_name} had a total score of {cumulative_score}% last semester \n')


input_file = 'students.txt'
output_file = 'cumulativeScores.txt'

calc_save_cumulative_scores(input_file, output_file)