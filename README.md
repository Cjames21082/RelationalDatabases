SQL and Relational Databases
============================
This is our latest work for the following lesson: 
https://github.com/chriszf/sql_lesson

Currently, the program hackbright_app.py performs the standard tasks listed at https://github.com/chriszf/sql_lesson/blob/master/HB_APP.md

The program hackbright_app.py will also:

* Add a student,
* Query for projects by title,
* Query for a student's grade given a project,
* Give a grade to a student, and
* Show all the grades for a student.

We are currently attempting to

* Add a project.

The problem? Adding multi-word project titles and/or multi-word project descriptions. The file parser.py is our current progress on this task.

**NOTE: The program now parses tokens at commas rather than spaces. Insert commands accordingly.**

--
Katherine Fellows & Cassandra Dixon