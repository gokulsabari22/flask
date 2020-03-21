from flask import Flask, render_template, redirect, url_for, request, session
import pymysql
from passwordvalidation import validation

app = Flask(__name__)

'''connect to ur db'''

mysql = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="page_db"
) 



mycursor = mysql.cursor()


@app.route('/')
def home():

    return render_template('welcome.html')

@app.route('/home')
def home_page():
    
    return render_template('home.html')
    

@app.route('/login', methods = ['GET', 'POST'])
def login():

    if  request.method == 'POST':
        details = request.form
        mobilenumber = details['MobileNumber']
        password = details['Password']
        sql = "SELECT  `mobilenumber`,  `password` FROM `page_db` WHERE `mobilenumber` = %s  AND `password` = %s "
        values = (mobilenumber,password)
        mycursor.execute(sql,values)
        result = mycursor.fetchone()
        

        print(result)

        if result:
            
            return redirect('/home')

        else:

            return "Username or Password was Incorrect !!"

    return render_template('login.html')
       

@app.route('/registration', methods = ['GET', 'POST'])
def registration():
    
    if request.method == 'POST':

        details = request.form
        FirstName = details['FirstName']
        LastName = details['LastName']
        Email = details['E-mail']
        MobileNumber = details['MobileNumber']
        Password1 = details['Password']
        Password2 = details['Confirm Password']
        if Password1 == Password2:

            result = validation(Password1)

            if (len(MobileNumber)) == 10:
                if result:
                    query = "INSERT INTO `page_db` VALUES (%s, %s, %s, %s, %s)"
                    values = (FirstName, LastName, MobileNumber, Email, Password1)
                    mycursor.execute(query,values)
                    mycursor.connection.commit()
                    
                    return redirect('/login') 
                else:
                    return "Enter a valid password"
            else:
                return ("MobileNumber is not valid! Please try again ")
        else:
            return "Password does not match"   
    return render_template('registration.html')           

@app.route("/logout")
def logout():
    session['login'] = False
    return redirect('home')
    
if __name__ == '__main__':
    app.debug = True
    app.run()