from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/Technical-Events')
def techEvents():
    return render_template('technical-events.html')

@app.route('/Non-Technical-Events')
def nonTechEvents():
    return render_template('non-technical-events.html')

@app.route('/schedule')
def schedule():
    return render_template('schedules.html')





if __name__== '__main__':
    app.run(debug=True)