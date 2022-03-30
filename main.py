
from ast import fix_missing_locations
from numpy import append
from clip import Clip
from documentry import Documentary
from film import Film
from serial import Series
from mediac import Media
from actor import Actor

class Main:

    def __init__(self):
        file = open('listdata.txt','r')
        line = file.read().split('\n')
        self.movie = []
        for i in range(len(line)):
            info = line[i].split(',')
            if info[0] == 'film':
                self.movie.append(Film(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7]))

            elif info[0] == 'serial':
                self.movie.append(Series(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8]))
            
            elif info[0] == 'documentry':
                self.movie.append(Documentary(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8]))
                
            elif info[0] == 'clip':
                self.movie.append(Clip(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7]))    
              

        file.close()
        Main.menu(self)

    def menu(self):
        while True:
            print('0.show list')
            print('1.add')
            print('2.edit')
            print('3.delet')
            print('4.search')
            print('5.advance search')
            print('6.downlode')
            print('7.exit')
            x = int(input('Enter number your choice: '))

            if x == 0:
                Main.show_list(self)
            
            if x == 1:
                Main.add(self)

            elif x == 2:
                Main.edit(self)
    
            elif x == 3:
                Main.delet(self)

            elif x == 4:
                Main.search(self)
    
            elif x == 5:
                Main.search_plus(self)

            elif x == 6:
                Main.download_file(self)

            elif x == 7:                  
                Main.save(self)
                break
    
    def show_list(self):
        for i in self.movie :
            if i.type == 'serial' or i.type == 'documentry':
                Series.show_info(i)
                print('...............')
            else:
                Media.show_info(i)
                print('...............')

    def add(self):
        new_type = input('write type: \nfilm\nserial\nclip\ndocumentry: ')
        new_name = input('enter name: ')
        new_director = input('enter directore: ')
        new_imdb = input('enter imdb score: ')
        new_url = input('enter url: ')
        new_duration = input('enter duration(minute): ')
        new_year = input('enter year: ')
        new_casts = input('enter casts: cast1-cast2-... ')

        if new_type == 'film':
            self.movie.append(Film(new_type, new_name, new_director ,new_imdb , new_url ,new_duration , new_year ,new_casts))

        elif new_type == 'clip':
            self.movie.append(Clip(new_type, new_name, new_director ,new_imdb , new_url ,new_duration , new_year ,new_casts))

        elif new_type == 'serial':
            new_part = input('enter number of episods: ')
            self.movie.append(Series(new_type, new_name, new_director ,new_imdb , new_url ,new_duration , new_year ,new_casts, new_part)) 

        elif new_type == 'documentry' :
            new_part = input('enter number of episods: ')
            self.movie.append(Documentary(new_type, new_name, new_director ,new_imdb , new_url ,new_duration , new_year ,new_casts, new_part))
        
        print('aded!')
    
    def edit(self):
        k = 0
        y1 = input('name: ')
        for movie in self.movie:
            if y1 == movie.name:
                k = 1
                #j = int(input('1-edit name\n2-edit director\n3-edit imdb score\n4-url\n5-edit duration\n6-edit year\n7-edit cast: '))
                if movie.type == 'serial' :
                    Series.edit_serial(movie)
                elif movie.type == 'documentry':
                    Documentary.edit_doc(movie)
                elif movie.type == 'film':
                    Film.edit_film(movie)
                elif movie.type == 'clip':
                    Clip.edit_clip(movie)                   
                print('Edited') 
                print('.............')   
        
        if k == 0:
            print('not fonded')

    def delet(self):
        n = input('enter movie_name: ')
        for movie in self.movie :
            if n == movie.name :
                self.movie.remove(movie)
                print('deleted!')
                print('..............')
                break
            if movie == len(self.movie) and n!= movie.name :
                print('not found')

    def search(self):
        k = 1
        n = input('enter name :')
        for i in self.movie :
            if n == i.name :
                Media.show_info(i)
                k = 0
        if k == 1:
            print('not found')        

    def search_plus(self):
        k = 0
        m1 = int(input('enter minimom time: '))
        m2 = int(input('enter maximom time: '))
        for i in self.movie:
            if m1 <= int(i.duration) <= m2 :
                Media.show_info(i)
                k = 1
        if k == 0 :
            print('not exist')        
    
    def download_file(self):
        n = input('enter name of the movie: ')
        for movie in self.movie:
            if n == movie.name :
                Media.download(movie)
                print('.............')

    def save(self):
        file = open('listdata.txt','w')
        for i in self.movie:
            if i.type == 'serial' or i.type == 'documentry' : 
                if i != len(self.movie)-1 :
                    str1 = i.type +','+ i.name +','+ i.director +','+ i.IMDBscore +','+ i.url +','+ i.duration +','+ i.year +','+ i.casts +','+ i.parts + '\n'
                else:
                    str1 = i.type +','+ i.name +','+ i.director +','+ i.IMDBscore +','+ i.url +','+ i.duration +','+ i.year +','+ i.casts +','+ i.parts            
                file.write(str1)

            elif i.type == 'film' or i.type == 'clip' :
                if i != len(self.movie)-1 :
                    str1 = i.type +','+ i.name +','+ i.director +','+ i.IMDBscore +','+ i.url +','+ i.duration +','+ i.year +','+ i.casts +'\n'
                else:
                    str1 = i.type +','+ i.name +','+ i.director +','+ i.IMDBscore +','+ i.url +','+ i.duration +','+ i.year +','+ i.casts
                file.write(str1)
            
        file.close()

Main()  

