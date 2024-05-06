from connectfilm import *

def add_film(film_title, film_release, film_rating, film_duration, film_genre):
    try:
        db_cursor.execute('INSERT INTO tblFilms VALUES(NULL,?,?,?,?,?)', (film_title, film_release, film_rating, film_duration, film_genre))
        db_con.commit() 
        print(f'{film_title} Inserted in the films table')
        return True
    except sql.Error as e:
        print(f"Operational error because of {e}")
        return False
    finally: 
        print("Closing DB connection")
        #dbCon.close()

if __name__ == "__main__":
    add_film()