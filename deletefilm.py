from connectfilm import *

def delete_film(film_id):
    try:
        db_cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = ?", (film_id,))
        aRecord = db_cursor.fetchone()

        if aRecord is None:
            print(f"No record with the filmID {film_id} exists!")
            return False
        else:
            db_cursor.execute(f"DELETE FROM tblFilms WHERE filmID = ?", (film_id,))
            db_con.commit()
            print(f"{film_id} deleted")
            return True
    except sql.OperationalError as oe:
        print(f"Failed because: {oe}")
        return False

if __name__ == "__main__":
    film_id = input("Enter the filmID to delete a record:")
    delete_film(film_id)