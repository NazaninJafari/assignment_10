from mediac import Media

#mostanad
class Documentary(Media):
    def __init__(self, type, name, di, im, url, du, y, ca, p):
        Media.__init__(self ,type ,name ,di ,im ,url ,du ,y ,ca)
        self.parts = p
    
    def edit_doc(self):
        j = int(input('1-edit name\n2-edit director\n3-edit imdb score\n4-url\n5-edit duration\n6-edit year\n7-edit cast: '))
        if j==1 :
            self.name = input('enter name: ')    
        
        elif j==2:
            self.director = input('enter director: ') 

        elif j==3:
            self.IMDBscore = input('enter imdb: ')
        
        elif j==4:
            self.url = input('enter url: ')

        elif j==5:
            self.duration = input('enter duration en minute: ')
        
        elif j==6:
            self.year = input('enter year: ')
        
        elif j==7: 
            self.casts = input('enter casts: cast1-cast2... ')
        
        elif j==8:
            self.parts = input('enter namber of parts: ')          