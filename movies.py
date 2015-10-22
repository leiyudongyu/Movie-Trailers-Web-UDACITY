import webbrowser


class Movie():
    '''This class defines the format of movie'''
    def __init__(self, movie_dict):
        self.title = movie_dict["title"]
        self.storyline = movie_dict["storyline"]
        self.trailer_youtube_url = movie_dict["trailer_youtube_url"]
        self.poster_image_url = movie_dict["poster"]

    def show_trailer(self):
        webbrowser.open(trailer_youtube_url)
