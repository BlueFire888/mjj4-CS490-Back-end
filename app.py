from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from flask import jsonify

app = Flask(__name__, template_folder= 'C:/Users/Michael Jones/git/CS490/mjj4-CS490-Front-end/templates')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Minecraft928'
app.config['MYSQL_DB'] = 'sakila'

mysql = MySQL(app)


with app.app_context():
#Creating a connection cursor
    cursor = mysql.connection.cursor()
 
#Executing SQL Statements
    cursor.execute("""SELECT f.title, count(*) as rented
FROM film as f, inventory as i, rental as r
WHERE f.film_id = i.film_id AND i.inventory_id = r.inventory_id
Group by f.title
ORDER BY rented DESC limit 5;""" )
    return_data = { 
        'TopMovies' : [],
        'TopActors':  [],
        'MovieDetails': [],
        'ActorDetails': [],
        'ActorMovies': []
    }
    output = cursor.fetchall()
    for item in output:
        return_data['TopMovies'].append(item[0].title())

#Saving the Actions performed on the DB
    mysql.connection.commit()

    cursor.execute("""SELECT A.first_name, A.last_name, COUNT(*)
FROM FILM_actor as FA, Actor as A
WHERE A.actor_id = fa.actor_id
GROUP BY A.actor_id
ORDER BY Count(*) DESC limit 5;""" )
    output = cursor.fetchall()
    for item in output:
        return_data['TopActors'].append(item[0].title() + "\n" + item[1].title())
 
#Closing the cursor
    cursor.close()

@app.route('/home', methods = ["GET"])
def home():
    return return_data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)