
import Media

class Documentory(Media.Media):
    
    def __init__(self,  n, d, s, u, dur, cs, y):
        super().__init__( n, d, s, u, dur, cs)
        self.year = y
    
    def showInfo(self):
        super().showInfo()
        print('Year: ', self.year)
        
    def edit(self):
        super().edit()
        new_year = input('Year = ')
        self.year = new_year