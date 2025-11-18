import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                         #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.
# set SECRET_KEY=367412045c345cde97f3102048adc2156b67b7ed82f1667bf457572ef8ce772d
@app.route('/')
def renderMain():
    session.clear()
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if request.method == 'POST':
            if "thirdPlanet" not in session:
                session["thirdPlanet"]=request.form['thirdPlanet']#saves it to session
            return render_template('page2.html')
    
@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if request.method == 'POST':
        if "resultColor" not in session:
            session["resultColor"]=request.form['resultColor']
    
    
    return render_template('page3.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    if request.method == 'POST':
        if "mixedColor1" and "mixedColor2" not in session:
            session["mixedColor1"]=request.form['mixedColor1']
            session["mixedColor2"]=request.form['mixedColor2']
           
    points=0
    if session["thirdPlanet"] in ['Earth', 'earth']:
        reply1 = "Correct!"
        points += 5
    else:
        reply1 = "Incorrect:/"
        
    if session["resultColor"] in ['Green', 'green']:
        reply2 = "Correct!"
        points += 5
    else:
        reply2 = "Incorrect:/"
        
    if session["mixedColor1"] in ['Yellow','yellow','Red','red']:
        reply3 = "Correct!"
        points += 5
    else:
        reply3 = "Incorrect!"
        
    if session["mixedColor2"] in ['Yellow','yellow','Red','red']:
        reply4 = "Correct!"
        points += 5
    else:
        reply4 = "Incorrect:/"

    return render_template('page4.html', response1 = reply1, response2 = reply2, response3 = reply3, response4 = reply4, points=points)
    
if __name__=="__main__":
    app.run(debug=True)
