#create Video class to store and override method to Movie and Tv_show class
class Video():
    def __init__(self,title_media,duration_media):
	    self.title = title_media
	    self.duration = duration_media
	    
#Create Movie and Tv_Show class to store the data require to display on website		
class Movie(Video):
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self,title_media,duration_media,description_media,
	         thumbnail_url,trailer_url):
	    Video.__init__(self,title_media,duration_media)
	    self.description = description_media
	    self.thumbnail = thumbnail_url
	    self.trailer = trailer_url
		
class Tv_Show(Video):
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self,title_media,duration_media,description_media,
	         thumbnail_url,trailer_url):
	    Video.__init__(self,title_media,duration_media)
	    self.description = description_media
	    self.thumbnail = thumbnail_url
	    self.trailer = trailer_url
