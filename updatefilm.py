from connectfilm import *
def update_film():
    try:
        # id of the record to be updated
        idField = input("Enter the filmID to update a record:")
        
        db_cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idField}")
        #Fetch one returns a specific record based on search criteria
        aRecord = db_cursor.fetchone()
        
        #None: is a single object that checks if a value is absent
        if aRecord == None:
            print(f"No record with the filmID{idField} exists!")
        
        else: 
            film_title = input("Enter the film's title : ")
            film_release = input("Enter the film's year of release: ")
            film_rating = input("Enter the film's rating: ")
            film_duration = input("Enter the film's duration: ")
            film_genre = input("Enter the film's genre: ")

            film_title = "'"+film_title+"'"
            film_release = "'"+film_release+"'"
            film_rating = "'"+film_rating+"'"
            film_duration = "'"+film_duration+"'"
            film_genre = "'"+film_genre+"'"
            
            # dbCursor.execute(f"UPDATE songs SET Title, Artist, Genre(?,?,?) WHERE SongID = ?", (song_title,song_artist,song_genre,idField))
            db_cursor.execute(f"UPDATE tblFilms SET title = {film_title}, yearReleased = {film_release}, rating = {film_rating}, duration = {film_duration}, genre = {film_genre} WHERE filmID = {idField}")
            db_con.commit()
            print(f"{idField} updated")
    except sql.OperationalError as oe:
        print(f"Failed because: {oe}")
if __name__ == "__main__":
    update_film()

    
