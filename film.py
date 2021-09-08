import Media

class Film(Media.Media):
    
    def __init__(self, n, d, s, u, dur, cs ,g, y):
        super().__init__(n, d, s, u, dur, cs)
        self.genre = g
        self.year = y
        
    def showInfo(self):
        super().showInfo()
        print('Genre: ', self.genre)
        print('Year: ', self.year)
        
    def edit(self):
        super().edit()
        new_genre = input('Genre = ')
        new_year = input('Year = ')
        self.genre = new_genre
        self.year = new_year