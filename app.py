from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Minecraft928'
app.config['MYSQL_DB'] = 'sakila'

mysql = MySQL(app)


with app.app_context():
#Creating a connection cursor
    cursor = mysql.connection.cursor()
 
#Executing SQL Statements
    cursor.execute("""SELECT F.film_ID, F.title, c.name 
FROM FILM as F, FILM_Category as fc, Category as C
WHERE F.film_ID = fc.film_id AND fc.category_id = c.category_id;""" )
    output = cursor.fetchmany(size=5)
    newoutput = []
    for item in output:
        newoutput.append(item[1])
 
#Saving the Actions performed on the DB
    mysql.connection.commit()
 
#Closing the cursor
    cursor.close()

@app.route('/')
def home():
    return render_template('home.html', output=newoutput)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)