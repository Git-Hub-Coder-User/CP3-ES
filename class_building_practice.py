"""
In VSCode build a class for a movie. Remember movies need to have titles, release year, director, rating, genre and cast. 

-Needs the init method

-Needs string methods that will print out all the information for the movies

-Method that sorts the movies in alphabetical order

-Method that sorts the movies in chronological order

-List genre

-Search director

-search cast

Create at least 20 objects using your movie class. 
"""

class Movie():
    def __init__(self, title, release_date, directors, rating, genre, cast):
        self.title = title
        self.release_date = release_date
        self.directors = directors
        self.rating = rating
        self.genre = genre
        self.cast = cast
    
    def __str__():
        pass

    #Sort alphabetically
    def alphabetical():
        pass

    #Sort chronologically
    def chronological():
        pass

    #Show all movies of a genre
    def genre():
        pass

    #Search by director
    def director():
        pass

    #Search by cast
    def cast():
        pass