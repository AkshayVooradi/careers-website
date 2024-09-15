from flask import Flask,render_template, jsonify

app = Flask(__name__)

jobs=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru, India',
        'Salary':'Rs. 10,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi, India',
        'Salary':'Rs. 15,00,000'
    },
    {
        'id':3,
        'title':'Full Stack Developer',
        'location':'Remote',
    },
    {
        'id':4,
        'title':'Backend Developer',
        'location':'San Francisco, USA',
        'Salary':'$ 120,000'
    },

]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs)

if __name__ == '__main__' :
    app.run(host='0.0.0.0',debug=True)
