from flask import Flask, render_template, request
import hackbright_app


app = Flask(__name__)

#concept:
# *add decorator 
# *name of handler
# *response of the handler


@app.route("/")
def get_github():
    return render_template('get_github.html')

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)

    first_name = row[0]
    last_name = row[1]
    github = row[2]

    grades = hackbright_app.show_grades(first_name, last_name)
    html = render_template('student_info.html', first_name=first_name,
                                                last_name=last_name,
                                                github=github,
                                                grades=grades,
                                                )
    return html

@app.route("/grades")
def get_project_grades():
    hackbright_app.connect_to_db()
    project_title = request.args.get("title")
    project_grades = hackbright_app.grades_by_title(project_title)

    html = render_template('project_grades.html', project_grades=project_grades)

    return html

@app.route("/newStudent")
def new_students():
    hackbright_app.connect_to_db()
    first_name = request.args.get("first_name")
    last_name= request.args.get("last_name")
    github= request.args.get("github")

    new_student = hackbright_app.make_new_student(first_name,last_name,github)
    grades = hackbright_app.show_grades(first_name, last_name)

    html = render_template("student_info.html", first_name=first_name,
                                                last_name=last_name,
                                                github=github,
                                                grades=grades,
                                                )

    return html

@app.route("/addProject")
def add_project():
    hackbright_app.connect_to_db()
    project_title = request.args.get("title")
    description = request.args.get("description")
    final_grade = request.args.get("max_grade")
    github= request.args.get("github")

    new_project = hackbright_app.make_new_project(project_title,description,final_grade)


    html = render_template("get_github.html")

    return html

@app.route('/assignGrade')
def assign_grade():
    hackbright_app.connect_to_db()
    project_title = request.args.get('title')
    grade = request.args.get('grade')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    assign_grade = hackbright_app.assign_grade_to_student(first_name,last_name,project_title,grade)
    project_grades = hackbright_app.grades_by_title(project_title)

    html = render_template("project_grades.html", project_grades=project_grades)
                                                
    return html

if __name__ == "__main__":
    app.run(debug=True)
