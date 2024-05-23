class View:
    @staticmethod
    def display_movies(movies):
        if not movies:
            return "No movies found!"
        else:
            movie_list = ""
            for movie in movies:
                movie_list += f"{movie.title} - {movie.director} ({movie.year})\n"
            return movie_list

    @staticmethod
    def display_menu():
        return "Movie Database Menu:\n1. Add a Movie\n2. View All Movies\n3. Search Movies\n4. Delete a Movie\n5. Save Movies to File\n6. Exit"

    @staticmethod
    def get_movie_details():
        title = input("Enter the movie title: ")
        director = input("Enter the movie director: ")
        year = input("Enter the movie release year: ")
        return title, director, year