import movies
import fresh_tomatoes
import re

''' Main function, run this file'''

def is_valid_url(url) :
    ''' Used to check whether the url is a valid url'''
    return re.match(r'^https?:/{2}\w.+$',url)

class EntertainmentCenter() :
    commandBar = '''
a. Add your favorite movie.
b. Remove a move from your list.
c. Show the website of movies.
d. Exit
'''
    def __init__(self) :
        self.movie_list = []

    def addMovie(self) :
        movie = self.getMovie()
        self.movie_list.append(movie)

    def getMovie(self) :
        ''' Get movie from the user's input '''
        movie_dict = {}
        
        print("Please input the movie's name:")
        movie_dict["title"] = raw_input()
        
        print("Please input the storyline of the movie")
        movie_dict["storyline"] = raw_input()
        
        print("Please input the poster url of the movie")
        url_poster = raw_input()
        while (not is_valid_url(url_poster)) :
            print("Please input a valid url")
            url_poster = raw_input()
        movie_dict["poster"] = url_poster

        print("Please input the youtube trailer url")
        url_trailer = raw_input()
        while (not is_valid_url(url_trailer)) :
            print("Please input valid trailer url")
            url_trailer = raw_input()
        movie_dict["trailer_youtube_url"] = url_trailer

        movie = movies.Movie(movie_dict)
        print(movie.title)
        return movie

    def removeMovie(self) :
        ''' Remove the movie based on the user's input '''
        if len(self.movie_list) is 0 :
            print("There is no movie in the list")
            return
        print("Movies in our list:")
        for movie in self.movie_list :
            print(movie.title)
        print("Please write down the movie you want to remove from the list or enter EXIT to leave this commamd")
        name = raw_input()
        if name is "EXIT" :
            return
        for mv in self.movie_list :
            if mv.title == name :
                self.movie_list.remove(mv)
        return

    def showWebpage(self):
        fresh_tomatoes.open_movies_page(self.movie_list)
        return

    def printinfo(self, text):
        print(text)
    def options(self, choice) :
        try :
            { 'a' : lambda : self.addMovie(),
              'b' : lambda : self.removeMovie(),
              'c' : lambda : self.showWebpage(),
              'd' : lambda : self.printinfo("Welcome Again")
            }[choice]()
        except KeyError:
            print("Please choose one of the options above")


def main() :
    en = EntertainmentCenter()
    while (True) :
        print(EntertainmentCenter.commandBar)
        choice = raw_input()
        if choice is 'd' :
            break
        en.options(choice)

if __name__=="__main__" :
    main()
                
            
            
        

















        
