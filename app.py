from flask import Flask, render_template, request, redirect
app = Flask(__name__)
#student list
# -demo data - student list page - a table on student list page 
#add a student 
#- add button on list of students page - a page with registrattion form and submit button
#expell a student
#edit a student
ALL_STUDENTS_DATA = [
    {
        'f_name': 'Mubashir',
        'l_name': 'Haider',
        'class': 'BSCS', 'dofbirth':
        '28/10/2003',
        'roll': '1',
        'fee': '25000'
    },
    {
        'f_name': 'Ali Raza',
        'l_name': 'Yameen',
        'class': 'BBA',
        'dofbirth':
        '5/10/2000',
        'roll': '2',
        'fee': '35000'
    },
    {
        'f_name': 'Usman',
        'l_name': 'Malik',
        'class': 'BSCS',
        'dofbirth': '26/10/2002',
        'roll': '3',
        'fee': '12000'
    }
]

ALL_TEACHERS_DATA =[
    {'f_name' : 'Noor',
    'l_name' : 'Fatima',
    'Qualification' : 'MSC',
    'dofbirth' : '12/7/1980',
    'id' : '12567',
    'salary' : '70,000'},

    {'f_name' : 'Sadia',
    'l_name' : 'Akhtar',
    'Qualification' : 'MS ENGLISH',
    'dofbirth' : '2/9/1985',
    'id' : '11762',
    'salary' : '75,000'},

    {'f_name' : 'Noreen',
    'l_name' : 'Riaz',
    'Qualification' : 'MS Mathematics',
    'dofbirth' : '11/2/1988',
    'id' : '15677',
    'salary' : '90,000'}
    ]
#home
@app.route('/')
def homepage():
    return render_template('home.html')

#View all students
@app.route('/view_all_students')
def view_all_students():
    return render_template('students/view_all_students.html', students=ALL_STUDENTS_DATA)

#add new student
@app.route('/add_new_student' , methods=["GET","POST"])
def add_new_student():
    if request.method == "GET":
        return render_template('students/add_new_student.html')
    elif request.method == "POST":
        first_name =  request.form["first_name"]
        last_name = request.form["last_name"]
        class_ = request.form["Course"]
        dob_ = request.form["dob"]
        roll_ = request.form["roll"]
        fees_ = request.form["fee"]
        student = {
            'f_name': first_name,
            'l_name': last_name,
            'class': class_,
            'dofbirth': dob_,
            'roll': roll_,
            'fee': fees_
            }

        ALL_STUDENTS_DATA.append(student)
        return redirect('/view_all_students')


#student detail
@app.route('/student.detail/<roll_number>')
def student_detail(roll_number):
    for students in ALL_STUDENTS_DATA:
        if students['roll'] == roll_number:
            return render_template('students/student_detail.html' , student =students)

#delete student
@app.route('/delete.student/<roll_number>')
def student_delete(roll_number):
    for student in ALL_STUDENTS_DATA:
        if student['roll'] == roll_number:
            ALL_STUDENTS_DATA.remove(student)
            return redirect('/view_all_students')

#edit student
@app.route('/student.edit/<roll_number>', methods=["GET","POST"])
def edit_student(roll_number):
    for student in ALL_STUDENTS_DATA:
            if student['roll'] == roll_number:
                if request.method == "GET":
                    return render_template('students/edit_student.html', student=student)
                elif request.method == "POST":
                    student['f_name'] =  request.form["first_name"]
                    student['l_name'] = request.form["last_name"]
                    student['class'] = request.form["Course"]
                    student['dofbirth'] = request.form["dob"]
                    student['roll'] = request.form["roll"]
                    student['fee'] = request.form["fee"]
                    return redirect('/view_all_students')


#TEACHERS --- View all Teachers
@app.route('/view-all-Teachers')
def view_all_Teachers():
    return render_template('teachers/view_all_Teachers.html' ,teachers= ALL_TEACHERS_DATA)

#add new Teacher
@app.route('/add-new-teacher', methods=["GET","POST"])
def add_new_teacher():
    if request.method == "GET":
        return render_template('teachers/add_new_teacher.html')
    elif request.method == "POST":
        f_name = request.form['first_name']
        l_name = request.form['last_name']
        qual = request.form['qualification']
        dob = request.form['dob']
        id_ = request.form['teacherid']
        pay = request.form['salary']
        
        new_teacher = {
        'f_name' : f_name,
        'l_name' : l_name,
        'Qualification' : qual,
        'dofbirth' : dob,
        'id' : id_,
        'salary' : pay
        }

        ALL_TEACHERS_DATA.append(new_teacher)
        return redirect('/view-all-Teachers')

#teacher detail
@app.route('/teacher.detail/<teacher_id>')
def teacher_detail(teacher_id):
    for teachers in ALL_TEACHERS_DATA:
        if teachers['id'] == teacher_id:
            return render_template('teachers/teacher_detail.html', teacher= teachers)

#delete teacher
@app.route('/expell.teacher/<teacher_id>')
def delete_teacher(teacher_id):
    for teacher in ALL_TEACHERS_DATA:
        if teacher['id'] == teacher_id:
            ALL_TEACHERS_DATA.remove(teacher)
            return redirect('/view-all-Teachers')

#edit Teacher
@app.route('/edit.teacher/<teacher_id>', methods=["GET","POST"])
def edit_teacher(teacher_id):
    for teacher in ALL_TEACHERS_DATA:
        if teacher['id'] == teacher_id:
            if request.method == "GET":
                return render_template('teachers/edit_teacher.html' , teacher=teacher)
            elif request.method == "POST":
                teacher['f_name'] = request.form['first_name']
                teacher['l_name'] = request.form['last_name']
                teacher['dofbirth'] = request.form['dob']
                teacher['Qualification'] = request.form['qualification']
                teacher['id'] = request.form['teacherid']
                teacher['salary'] = request.form['salary']
                return redirect('/view-all-Teachers')
