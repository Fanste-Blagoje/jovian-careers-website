from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Novi Sad, Serbia',
        'salary': 'RSD 120000'
    },
{
        'id': 2,
        'title': 'Software Engineer',
        'location': 'Nis, Serbia',
        'salary': 'RSD 130000'
    },
{
        'id': 3,
        'title': 'Backend Developer',
        'location': 'Belgrade, Serbia',
        'salary': 'RSD 110000'
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)