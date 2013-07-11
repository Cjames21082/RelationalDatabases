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
												grades= grades,
												)

	
	return html

@app.route("/grades")
def get_project_grades():
	hackbright_app.connect_to_db()

	#request agrs
	project_title = request.args.get("title") # to be fixed

	# pass arguments to db and return output
	project_grades = hackbright_app.project_by_title(project_title)

	#render to html page
	html_title = render_template('project_grades.html', project_grades= project_grades)

if __name__ == "__main__":
    app.run(debug=True)
