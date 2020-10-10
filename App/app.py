from PySide2 import QtWidgets, QtCore

from App.movie import Movie


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cinéma Club")
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)

    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)

    def populate_movies(self):
        self.lw_movies.clear()
        for movie in Movie.get_movies():
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.movie = movie
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        title = self.le_movieTitle.text()
        if not title:
            return False
        Movie(title).add_to_movies()
        self.populate_movies()
        self.le_movieTitle.clear()

    def remove_movie(self):
        for lw_item in self.lw_movies.selectedItems():
            lw_item.movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(lw_item))


app = QtWidgets.QApplication([])
window = App()
window.show()
app.exec_()
