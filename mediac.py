from numpy import append
import pytube

class Media:
    def __init__(self ,type, name ,di ,im ,url ,du ,y ,ca):
        self.type = type
        self.name = name
        self.director = di 
        self.IMDBscore = im
        self.url = url
        self.duration = du
        self.year = y
        self.casts = ca

    def show_info(self):  
        print(self.type+'\n'+self.name+'\n'+self.director+'\n'+ self.IMDBscore +'\n'+self.url+'\n'+ self.duration +'\n'+ self.year+'\n'+self.casts)
    
    def download(self):
        link = self.url
        first_stream =pytube.YouTube(link).streams.first()
        first_stream.download(output_path = './' , filename = 'dl.mp4')
        print('downloaded!')
        