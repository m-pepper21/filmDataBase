from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
from addfilm import add_film
from deletefilm import delete_film
from updatefilm import update_film

# create an instance of the Flask class
app = Flask(__name__)

db_con = sql.connect('filmflix.db')
db_cursor = db_con.cursor()

#home route
@app.route('/')
@app.route('/index')
def index():
     with sql.connect('filmflix.db') as db_con:
        db_cursor = db_con.cursor()
        
        # Fetch all films from the database
        db_cursor.execute('SELECT * FROM tblFilms')
        films = db_cursor.fetchall()
     return render_template('index.html', title = "Home Page", films=films)

@app.route('/delete')
def about():
    return render_template('delete.html', title = "Delete Page")

@app.route('/update')
def contact():
    return render_template('update.html', title = "Update Page")

@app.route('/addfilm', methods=['POST'])
def add_film_route():
    if request.method == 'POST':
        film_title = request.form['title']
        film_release = request.form['release']
        film_rating = request.form['rating']
        film_duration = request.form['duration']
        film_genre = request.form['genre']

        with sql.connect('filmflix.db') as db_con:
            db_cursor = db_con.cursor()
            
            db_cursor.execute('INSERT INTO tblFilms VALUES(NULL,?,?,?,?,?)', 
                              (film_title, film_release, film_rating, film_duration, film_genre))
            db_con.commit() 
            
            print(f'{film_title} Inserted in the films table')
            return render_template('success.html', action='added')
    try:
        raise sql.ProgrammingError("An example error")
    except sql.ProgrammingError as pe:
        print(f"Programming error because: {pe}")
        return render_template('error.html')
    except sql.OperationalError as oe:
        print(f"Operational error because of {oe}")
        return render_template('error.html')
    except sql.Error as e:
        print(f"Operational error because of {e}")
        return render_template('error.html')
    # For Delete    
@app.route('/deletefilm', methods=['POST'])
def delete_film_route():
    if request.method == 'POST':
        film_id = request.form['id']
        try:
            conn = sql.connect('filmflix.db')
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM tblFilms WHERE filmID = ?", (film_id,))
            conn.commit()
            print(f"{film_id} deleted")
            return render_template('success.html', action='deleted')
        except sql.Error as e:
            print(f"Operational error because of {e}")
            return render_template('error.html')
        finally:
            conn.close()
  # For Update    
@app.route('/updatefilm', methods=['GET', 'POST'])
def update_film_route():
    film_id = None
    if request.method == 'POST':
        film_id = request.form.get('id', None)

        if film_id is not None:
            # Check if the film exists in the database
            with sql.connect('filmflix.db') as db_con:
                db_cursor = db_con.cursor()
                db_cursor.execute('SELECT * FROM tblFilms WHERE filmID = ?', (film_id,))
                film = db_cursor.fetchone()

            if film is None:
                # If the film doesn't exist, display an error message
                error_message = f"Film with ID {film_id} does not exist!"
                return render_template('update.html', title="Update Film", error=error_message, film_id=film_id)
            else:
                # If the film exists, check if the form data is submitted
                if 'title' in request.form:
                    # Update the film in the database
                    film_title = request.form['title']
                    film_release = request.form['release']
                    film_rating = request.form['rating']
                    film_duration = request.form['duration']
                    film_genre = request.form['genre']

                    with sql.connect('filmflix.db') as db_con:
                        db_cursor = db_con.cursor()
                        db_cursor.execute("""
                            UPDATE tblFilms
                            SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ?
                            WHERE filmID = ?
                        """, (film_title, film_release, film_rating, film_duration, film_genre, film_id))
                        db_con.commit()

                    return render_template('success.html', action='updated')
                else:
                    # Render the update form with the film details
                    return render_template('update.html', title="Update Film", film=film, film_id=film_id)
        else:
            # If film_id is None, redirect to the update page
            return redirect(url_for('update_film_route'))
    else:
        return render_template('update.html', title="Update Film", error=None, film_id=film_id)


# to run the flask app
if __name__== "__main__":
    app.run(debug=True)
