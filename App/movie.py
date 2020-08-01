#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import os
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def add_to_movies(self):
        movies_titles = Movie.get_movies_titles()
        if self.title not in movies_titles:
            movies_titles.append(self.title)
            Movie.write_movies(movies_titles)
        else:
            logging.warning(f"The movie {self.title} already exists.")

    def remove_from_movies(self):
        movies_titles = Movie.get_movies_titles()
        if self.title in movies_titles:
            movies_titles.remove(self.title)
            Movie.write_movies(movies_titles)
        else:
            logging.warning(f"The movie {self.title} does not exist.")

    @classmethod
    def write_movies(cls, movies):
        with open(DATA_FILE, 'w') as json_file:
            json.dump(movies, json_file, indent = 4)

    @classmethod
    def get_movies_titles(cls):
        with open(DATA_FILE, 'r') as json_file:
            return json.load(json_file)

    @classmethod
    def get_movies(cls):
        return [Movie(movie_title) for movie_title in Movie.get_movies_titles()]


def test_function():
    harry_potter = Movie("Harry Potter")
    harry_potter.add_to_movies()
    marry_poppins = Movie("Marry Poppins")
    marry_poppins.remove_from_movies()
    print(Movie.get_movies_titles())
    print(Movie.get_movies())


if __name__ == "__main__":
    test_function()
