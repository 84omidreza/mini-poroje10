import Film, serial, Clip, Documentory
from pyfiglet import Figlet

f = Figlet(font='standard')
print(f.renderText('MULTI MEDIA'))

media = []
address = 'media.txt'
qrcode_address = 'qrcode.png'

def show_menu():
    print('1- Show List')
    print('2- Add Media')
    print('3- Edit Media')
    print('4- Delete Media')
    print('5- Search')
    print('6- Advanced Search')
    print('7- Download Media')
    print('8- Qr Code')
    print('9- Exit & Save')

    
def database(address):
    database_file = open(address, 'r')
    data = database_file.read()
    database_file.close()
    data = data.strip()
    return data

def load():
    print('Loading ...')
    data = database(address)
    media_list = data.split('\n')
    
    for i in range(len(media_list)):
        media_info = media_list[i].split(',')
        if media_info[0] == 'film':
            film = Film.Film (media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], media_info[7], media_info[8])
            media.append(film)
        elif media_info[0] == 'Clip':
            clip = Clip.Clip(media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], media_info[7])
            media.append(clip)
        elif media_info[0] == 'Series':
            series = serial.Series(media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], media_info[7], media_info[8], media_info[9])
            media.append(series)
        elif media_info[0] == 'Documentory':
            documentary = Documentory.Documentory(media_info[1], media_info[2], media_info[3], media_info[4], media_info[5], media_info[6], media_info[7])
            media.append( documentary)
            

def show_list():
    for i in range(len(media)):
        print('(', i, ')')
        print('<<', type(media[i]).__name__, '>>')
        media[i].showInfo()
        
def add_media():
    mode = int(input('1.Film  -  2.Series -  3.Clip  -  4.Documentary  = ' ))
    if mode == 1:
        name = input('Name = ')
        director = input('Director = ')
        score = input('IMDB Score = ')
        url = input('URL = ')
        duration = input('Duration = ')
        casts = input('Casts = ')
        genre = input('Genre = ')
        year = input('Year = ')
        film = Film.Film(name, director, score, url, duration, casts, genre, year)
        media.append(film)
       
    elif mode == 2:
        name = input('Name = ')
        director = input('Director = ')
        score = input('IMDB Score = ')
        url = input('URL = ')
        duration = input('Duration = ')
        casts = input('Casts = ')
        genre = input('Genre = ')
        season = input('Season = ')
        episode = input('Episode = ')
        serie = serial.Series(name, director, score, url, duration, casts, genre, season, episode)
        media.append(serie)
    elif mode == 3:
        name = input('Name = ')
        director = input('Director = ')
        score = input('IMDB Score = ')
        url = input('URL = ')
        duration = input('Duration = ')
        casts = input('Casts = ')
        subject = input('Subject = ')
        clip = Clip.Clip(name, director, score, url, duration, casts, subject)
        media.append(clip) 
    else:
        name = input('Name = ')
        director = input('Director = ')
        score = input('IMDB Score = ')
        url = input('URL = ')
        duration = input('Duration = ')
        casts = input('Casts = ')
        year = input('Year = ')
        documentary = Documentory.Documentory(name, director, score, url, duration, casts, year)
        media.append(documentary)
        

def edit_media():
    print('Choose between 0 -', len(media)-1)
    choice = int(input())
    if choice > (len(media)-1) or choice < 0:
        print('Wrong choice!')
        return False
    media[choice].edit()
    
def delete_media():
    print('Choose between 0 -', len(media)-1)
    choice = int(input())
    if choice > (len(media)-1) or choice < 0:
        print('Wrong choice!')
        return False
    media.pop(choice)

def search(): # search by name
    flag = 0
    search_name = input('your media name? ')
    for i in media:
        if i.name == search_name:
            i.showInfo()
            flag = 1
    if flag == 0:
        print('Not Found :(')

def adv_search(): 
    flag = 0
    time_a = int(input('Enter your first time: '))
    time_b = int(input('Enter your second time: '))
    for i in media:
        time = int(i.getDuration())
        if time >= time_a and time <= time_b:
            i.showInfo()
            flag = 1
    if flag == 0:
        print('Not Found :(')

def download_media():
    print('Choose between 0 -', len(media)-1)
    choice = int(input())
    if choice > (len(media)-1) or choice < 0:
        print('Wrong choice!')
        return False
    media[choice].download()

def QrCode():
    print('Choose between 0 -', len(media)-1)
    choice = int(input())
    if choice > (len(media)-1) or choice < 0:
        print('Wrong choice!')
        return False
    


def save():
    database_file = open(address, 'w')
    for i in range(len(media)):
        f = media[i]
        name_cast = ''
        for j in f.casts:
            name_cast += j.showInfo()
            name_cast += ' - '
            name_cast = name_cast[:-2]
        if type(f).__name__ == 'Film':
            database_file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%('Film',f.name,f.director,f.IMDB_scores,f.url,f.duration,name_cast,f.genre,f.year))
        elif type(f).__name__ == 'Clip':
            database_file.write('%s,%s,%s,%s,%s,%s,%s,%s\n'%('Clip',f.name,f.director,f.IMDB_scores,f.url,f.duration,name_cast,f.subject))
        elif type(f).__name__ == 'Series':
            database_file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%('Series',f.name,f.director,f.IMDB_scores,f.url,f.duration,name_cast,f.genre,f.season,f.episode))
        elif type(f).__name__ == 'Documentary':
            database_file.write('%s,%s,%s,%s,%s,%s,%s,%s\n'%('Documentary',f.name,f.director,f.IMDB_scores,f.url,f.duration,name_cast,f.year))

    database_file.close()
    print('Your changes saved well :)')

def main_media():   
    while True:
        show_menu()
        choice = int(input('Please choose a number:  '))

        if choice == 1: 
            show_list()
            
        if choice == 2: 
            add_media()

        elif choice == 3: 
            edit_media()

        elif choice == 4: 
            delete_media()

        elif choice == 5: 
            search()

        elif choice == 6: 
            adv_search()

        elif choice == 7: 
            download_media()

        elif choice == 8: 
            QrCode()

        elif choice == 9:
            save()
            print('the save was successful')
            break
        else:
            print('Please choose a correct number ')
            continue
        
load()
main_media()