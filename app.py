from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime
loc = ("")
import mysql.connector
from flask_table import Table, Col


#connect to local DB

mydb = mysql.connector.connect(
  host="localhost",
  user="rishabh",
  passwd="123456",
  database="power"
)

mycursor = mydb.cursor(buffered=True)



# create the application object
app = Flask(__name__,static_url_path='/static')

# use decorators to link the function to a url
@app.route('/', methods=['GET', 'POST'])
def home():
    return redirect(url_for('login'))
#lgoin page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('main'))
    return render_template('login.html', error=error)
#landing page
@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.html', methods=['GET', 'POST'])


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        timeform = request.form['datetimepicker']
        timeform = datetime.strptime(timeform, "%m/%d/%Y %I:%M %p")
        timeformdate = timeform.strftime("%Y-%m-%d %H:%M:%S")
        #timeformtime = timeform.strftime("%H:%M:%S")
        print(timeformdate)
        #print(timeformtime)
        sql = "SELECT * FROM sensor WHERE date <= " + "\'" + str(timeformdate) +"\'" + "ORDER BY date DESC"
        #print(sql)
        mycursor.execute(sql)
        
        val1 = mycursor.fetchone()
        val = mycursor.fetchmany(10)
        if val1 == None:
            print("date does not exist in records")
        else:
            print("exists")
        

        # Get some objects
            class ItemTable(Table):
                name = Col('Date & Time')
                description = Col('Current Reading')
            class Item(object):
                def __init__(self, name, description):
                    self.name = name
                    self.description = description
             #fetching custom values from DB              
            val = mycursor.fetchmany(10)
            fetchtime1, fetchvalue1 = val[0]
            fetchtime2, fetchvalue2 = val[1]
            fetchtime3, fetchvalue3 = val[2]
            fetchtime4, fetchvalue4 = val[3]
            fetchtime5, fetchvalue5 = val[4]
            # fetchtime6, fetchvalue6 = val[5]
            # fetchtime7, fetchvalue7 = val[6]
            # fetchtime8, fetchvalue8 = val[7]
            # fetchtime9, fetchvalue9 = val[8]
            # fetchtime10, fetchvalue10 = val[9]

            items = [Item(fetchtime1, fetchvalue1),
                    Item(fetchtime2, fetchvalue2),
                    Item(fetchtime3, fetchvalue3),
                    Item(fetchtime4, fetchvalue4),
                    Item(fetchtime5, fetchvalue5),]
                    # Item(fetchtime6, fetchvalue6),
                    # Item(fetchtime7, fetchvalue7),
                    # Item(fetchtime8, fetchvalue8),
                    # Item(fetchtime9, fetchvalue9),
                    # Item(fetchtime10, fetchvalue10),
            
            # Populate the table
            table = ItemTable(items)
            return render_template('form.html',methods=['GET', 'POST'], tableprint = table)            
    return render_template('form.html',methods=['GET', 'POST'])
        

    
    
@app.route('/result',methods = ['GET', 'POST'])
def request_data():
    
    return render_template('form.html', methods=['GET', 'POST'])

@app.route('/power')
def power():
    return render_template('power.html', methods=['GET', 'POST'])


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')