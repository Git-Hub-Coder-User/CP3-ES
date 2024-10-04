"""
In VSCode build a class for a movie. Remember movies need to have titles, release year, director, rating, genre and cast. 

-Needs the init method - complete

-Needs string methods that will print out all the information for the movies - Complete

-Method that sorts the movies in alphabetical order - It's a function but it works - Method now

-Method that sorts the movies in chronological order - Also a function, but it works - Method now

-List genre - Completed

-Search director - Completed 

-search cast

-Implementation structure

Create at least 20 objects using your movie class. 
"""

class Movie():

    listed = []

    def __init__(self, title, release_date, directors, rating, genre, cast):
        self.title = title
        self.release_date = release_date
        self.directors = directors
        self.rating = rating
        self.genre = genre
        self.cast = cast
        Movie.listed.append(self)
    
    def __str__(self):
        return f"{self.title}: \n\tRelease date: {self.release_date} \n\tDirector(s): {self.directors} \n\tRating: {self.rating} \n\tGenre: {self.genre} \n\tCast: {self.cast}"
    
    def alphabetical(self, reversed):
        def function(value):
            return value.title
        Movie.listed.sort(reverse=reversed, key=function)
        return Movie.listed
    
    def chronological(self, reversed):
        def function(value):
            return value.release_date
        Movie.listed.sort(reverse=reversed, key=function)
        return Movie.listed
    
    def genre(self, genre):
        temp = []
        for value in listed:
            if value.genre == genre:
                temp.append(value)
        return temp
    
    def d_search(self, director):
        temp = []
        for value in listed: 
            if director in value.directors:
                temp.append(value)
        return temp
    
    def c_search(self, human):
        temp = []
        for value in listed: 
            for value2 in value.cast: 
                if human in value2:
                    temp.append(value)
        return temp
    

#These are functions that do the right things so I can reference them
def alphabetical(reversed):
    def function(value):
        return value.title
    listed.sort(reverse=reversed, key=function)
    return listed

def chronological(reversed):
    def function(value):
        return value.release_date
    listed.sort(reverse=reversed, key=function)
    return listed

def genre(genre):
    temp = []
    for value in listed:
        if value.genre == genre:
            temp.append(value)
    return temp

def search(director):
    pass

def print_list(listed):
    for value in listed:
        print(value)
    
for i in range(1): #To help make the code collapsable 
    movie1 = Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"])

    movie2 = Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"])

    movie3 = Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"])

    movie4 = Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"])

    movie5 = Movie("The Matrix", 1999, "Lana and Lilly Wachowski", "R", "Sci-Fi", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"])

    movie6 = Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", ["Tom Hanks", "Robin Wright", "Gary Sinise"])

    movie7 = Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"])

    movie8 = Movie("Schindler's List", 1993, "Steven Spielberg", "R", "Drama", ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"])

    movie9 = Movie("Fight Club", 1999, "David Fincher", "R", "Drama", ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"])

    movie10 = Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", ["Robert De Niro", "Ray Liotta", "Joe Pesci"])

    movie11 = Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"])

    movie12 = Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"])

    movie13 = Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", ["Elijah Wood", "Ian McKellen", "Orlando Bloom"])

    movie14 = Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"])

    movie15 = Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", ["Tom Hanks", "Michael Clarke Duncan", "David Morse"])

    movie16 = Movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", ["Tom Hanks", "Matt Damon", "Tom Sizemore"])

    movie17 = Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill", "Laura Dern", "Jeff Goldblum"])

    movie18 = Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"])

    movie19 = Movie("The Lion King", 1994, "Roger Allers and Rob Minkoff", "G", "Animation", ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"])

    movie20 = Movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", ["Jim Carrey", "Kate Winslet", "Kirsten Dunst"])

    movie21 = Movie("Inglourious Basterds", 2009, "Quentin Tarantino", "R", "War", ["Brad Pitt", "Christoph Waltz", "Mélanie Laurent"])

    movie22 = Movie("The Sixth Sense", 1999, "M. Night Shyamalan", "PG-13", "Thriller", ["Bruce Willis", "Haley Joel Osment", "Toni Collette"])

    movie23 = Movie("The Usual Suspects", 1995, "Bryan Singer", "R", "Mystery", ["Kevin Spacey", "Gabriel Byrne", "Chazz Palminteri"])

    movie24 = Movie("Memento", 2000, "Christopher Nolan", "R", "Thriller", ["Guy Pearce", "Carrie-Anne Moss", "Joe Pantoliano"])

    movie25 = Movie("Braveheart", 1995, "Mel Gibson", "R", "Biography", ["Mel Gibson", "Sophie Marceau", "Patrick McGoohan"])

    movie26 = Movie("The Terminator", 1984, "James Cameron", "R", "Sci-Fi", ["Arnold Schwarzenegger", "Linda Hamilton", "Michael Biehn"])

    movie27 = Movie("Back to the Future", 1985, "Robert Zemeckis", "PG", "Adventure", ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"])

    movie28 = Movie("Alien", 1979, "Ridley Scott", "R", "Horror", ["Sigourney Weaver", "Tom Skerritt", "John Hurt"])

    movie29 = Movie("The Truman Show", 1998, "Peter Weir", "PG", "Drama", ["Jim Carrey", "Laura Linney", "Noah Emmerich"])

    movie30 = Movie("If You're Reading This", 2000, "Autumn Merlin", "G", "Drama", ["Jessica Smith", "Lyra O'Brien", "Maya Doyle"])

listed = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, movie11, movie12, movie13, movie14, movie15, movie16, movie17, movie18, movie19, movie20, movie21, movie22, movie23, movie24, movie25, movie26, movie27, movie28, movie29, movie30,  ]


temp = Movie.c_search(Movie, "Freeman")

print_list(temp)