import sqlite3

DB = None
CONN = None

######################### Grades ######################

# Enter new grade
def assign_grade_to_student(first_name, last_name, project_title, grade):
    query1 = """SELECT github FROM Students WHERE first_name = ? AND last_name = ?"""
    DB.execute(query1, (first_name, last_name))
    row = DB.fetchone()

    if row == None:
        print "Name does not exist."
    else:
        query2 = """INSERT into Grades values (?, ?, ?)"""
        DB.execute(query2,(row[0], project_title, grade))
        CONN.commit()

        return """\
Student: %s %s 
Github: %s
Project: %s
Grade: %s"""%(first_name, last_name, row[0], project_title, grade)

# Show grades
def show_grades(first_name, last_name):
    query = """SELECT project_title, grade FROM Grades INNER JOIN Students ON (github = student_github) WHERE first_name = ? and last_name = ? """
    DB.execute(query, (first_name,last_name))
    rows = DB.fetchall()
    return rows
    #print "Student: %s %s" %(first_name, last_name)

    #print "Projects and Grades:"
    #for i in range(len(rows)):
    #return " %s, %s" %(rows[i][0], rows[i][1])

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row
    # Student: %s %s
    # Github account: %s"""%(row[0], row[1], row[2])

# Find a grade for a project
def grade_by_project(first_name, last_name, project_title):
    query = """SELECT grade, project_title FROM Students INNER JOIN Grades ON github = student_github 
        WHERE first_name = ? AND last_name = ? AND project_title = ?"""
    DB.execute(query, (first_name, last_name, project_title))
    row = DB.fetchone()
    print """\
    Title: %s
    Grade: %s""" % (row[1], row[0])

################################### Projects ################################

# Enter new project
def make_new_project(title,description, max_grade):
    # DOES NOT WORK
    query= """INSERT into Projects values (?,?,?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s" %(title)

# Search for a specific project
def project_by_title(project_title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (project_title,))
    rows = DB.fetchall()
    return rows
    #print """\
#Title: %s
Description: %s
Max Grade: %d"""%(row[0], row[1], row[2])


########################## Student #############################################

#Enter new student
def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" % (first_name, last_name)

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> Use commas to seperate inputs!")
        tokens = input_string.split(",")
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project":
            project_by_title(*args)
        # elif command == "new_project":
        #     make_new_project()
        elif command == "grade":
            grade_by_project(*args)
        elif command == "assign_grade":
            assign_grade_to_student(*args)
        elif command == "show_grades":
            show_grades(*args)

    CONN.close()

if __name__ == "__main__":
    main()
