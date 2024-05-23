from movie import Movie
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Controller:
    def __init__(self):
        self.movies = []
        self.load_from_file()

    def add_movie(self, title, director, year):
        movie = Movie(title, director, year)
        self.movies.append(movie)

    def view_all_movies(self):
        return self.movies

    def search_movie(self, keyword):
        return [movie for movie in self.movies if keyword.lower() in movie.title.lower()]

    def delete_movie(self, title):
        self.movies = [movie for movie in self.movies if movie.title != title]

    def save_to_file(self):
        with open("movies.txt", "w") as file:
            for movie in self.movies:
                file.write(f"{movie.title},{movie.director},{movie.year}\n")

    def load_from_file(self):
        try:
            with open("movies.txt", "r") as file:
                for line in file:
                    title, director, year = line.strip().split(",")
                    self.add_movie(title, director, year)
        except FileNotFoundError:
            pass

    def run(self):
        root = tk.Tk()
        root.title("Movie Database")
        root.configure(bg="#F4EAD5")  # Set background color

        def add_movie():
            title = title_entry.get()
            director = director_entry.get()
            year = year_entry.get()
            self.add_movie(title, director, year)
            messagebox.showinfo("Success", "Movie added successfully! Save it to your file!")
            title_entry.delete(0, tk.END)
            director_entry.delete(0, tk.END)
            year_entry.delete(0, tk.END)

        def view_movies():
            for item in tree.get_children():
                tree.delete(item)
            movies = self.view_all_movies()
            for idx, movie in enumerate(movies, start=1):
                tree.insert("", "end", values=(idx, movie.title, movie.director, movie.year))

        def search_movies():
            keyword = search_entry.get()
            movies = self.search_movie(keyword)
            for item in tree.get_children():
                tree.delete(item)
            for idx, movie in enumerate(movies, start=1):
                tree.insert("", "end", values=(idx, movie.title, movie.director, movie.year))

        def delete_movie():
            selected_item = tree.selection()[0]
            title = tree.item(selected_item, "values")[1]
            self.delete_movie(title)
            tree.delete(selected_item)
            messagebox.showinfo("Success", "Movie deleted successfully!")

        def save_movies():
            self.save_to_file()
            messagebox.showinfo("Success", "Movies saved to file successfully!")

        # Labels and entry fields
        title_label = tk.Label(root, text="Title:", bg="#F4EAD5")
        title_label.grid(row=0, column=0, padx=5, pady=5)
        title_entry = tk.Entry(root)
        title_entry.grid(row=0, column=1, padx=5, pady=5)

        director_label = tk.Label(root, text="Director:", bg="#F4EAD5")
        director_label.grid(row=1, column=0, padx=5, pady=5)
        director_entry = tk.Entry(root)
        director_entry.grid(row=1, column=1, padx=5, pady=5)

        year_label = tk.Label(root, text="Year:", bg="#F4EAD5")
        year_label.grid(row=2, column=0, padx=5, pady=5)
        year_entry = tk.Entry(root)
        year_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = tk.Button(root, text="Add Movie", command=add_movie, bg="#F0B27A", fg="white", relief="flat")
        add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        search_label = tk.Label(root, text="Search:", bg="#F4EAD5")
        search_label.grid(row=4, column=0, padx=5, pady=5)
        search_entry = tk.Entry(root)
        search_entry.grid(row=4, column=1, padx=5, pady=5)

        search_button = tk.Button(root, text="Search", command=search_movies, bg="#F0B27A", fg="white", relief="flat")
        search_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        delete_button = tk.Button(root, text="Delete Selected", command=delete_movie, bg="#E74C3C", fg="white", relief="flat")
        delete_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        save_button = tk.Button(root, text="Save Movies to File", command=save_movies, bg="#5DADE2", fg="white", relief="flat")
        save_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        view_button = tk.Button(root, text="View Movies", command=view_movies, bg="#58D68D", fg="white", relief="flat")
        view_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        # Treeview for displaying movies
        tree_frame = tk.Frame(root, bg="#F4EAD5")
        tree_frame.grid(row=0, column=2, rowspan=8, padx=5, pady=5)
        movie_list_label = tk.Label(tree_frame, text="MOVIE LIST", bg="#F4EAD5", font=("Arial", 12, "bold"),  anchor="center")
        movie_list_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tree = ttk.Treeview(tree_frame, columns=("Index", "Title", "Director", "Year"), show="headings")
        tree.heading("Index", text="Index")
        tree.heading("Title", text="Title")
        tree.heading("Director", text="Director")
        tree.heading("Year", text="Year")
        tree.column("Index", width=50, anchor="center")  # Adjust column width
        tree.column("Title", width=150, anchor="center")
        tree.column("Director", width=150, anchor="center")
        tree.column("Year", width=100, anchor="center")
        tree.grid(row=1, column=0, sticky="nsew")  # Add borders
        tree_frame.grid_rowconfigure(1, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        root.mainloop()

# Main program

if __name__ == "__main__":
    controller = Controller()
    controller.run()