from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("a_student")
    row = hackbright_app.get_student_by_github(student_github)
    try:
        student_lastname = request.args.get("a_studentlast")
        grades = hackbright_app.query_grades_by_student(student_lastname)
    except:
        grades = hackbright_app.query_grades_by_student(row[1])
##un fuck this up
    titles = []
    scores = []
    for i in range(len(grades)):
        titles.append(grades[i][0])
        scores.append(grades[i][1])

    html = render_template("student_info.html", first_name = row[0], last_name = row[1], a_student=row[2],titles = titles, scores = scores)
#grades = grades)

    return html

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/project_grades")
def title_grades():
    hackbright_app.connect_to_db()
    title = request.args.get("a_title")
    row = hackbright_app.query_grades_by_project_title(title)
    student_name = []
    grades = []
    print row
    print len(row)
    for i in range(len(row)):
        grades.append(row[i][0])
        student_name.append(row[i][1])

    html =  render_template("project_grades.html", project_title = title, students = student_name, grades = grades)
    return html

if __name__ == "__main__":
    app.run(debug=True)
