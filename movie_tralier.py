import media
#import fresh_tomato

#create a method to get the movie list
def getmovie(new_list):
    movie = []
    #create the movie review contents
    the_emoji_movie = media.Movie("The Emoji Movie","86 mins",
                                  "Gene,a multi-expressional emoji, sets \
                                   out on a journey to become a normal emoji.",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMzM3OTM2Ml5BMl5BanBnXkFtZTgwMDM0NDU3MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                  "https://www.youtube.com/watch?v=UWn8zsYtbtY"
                                  )
    atomic_blonde = media.Movie("Atomic Blonde (2017)","115 mins",
                                "An undercover MI6 agent is sent \
                                 to Berlin during the Cold War to investigate\
                                 the murder of a fellow agent and recover a \
                                 missing list of double agents.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM5NDYzMzg5N15BMl5BanBnXkFtZTgwOTM2NDU1MjI@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=nI7HVnZlleo")
    An_Inconvenient = media.Movie("An Inconvenient Seqeul: Truth to Power(2017)","98 mins",
                                  "A decade after An Inconvenient Truth \
                                   brought climate change into the heart \
                                   of popular culture comes \
                                   the follow-up that shows just how close\
                                   we are to a real energy revolution.",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BNTkzNTQ0MzA3Ml5BMl5BanBnXkFtZTgwNzg4OTcyMjI@._V1_UX140_CR0,0,140,209_AL_.jpg",
                                  "https://www.youtube.com/watch?v=huX1bmfdkyA")
    the_midwife = media.Movie("The Midwife(2017)","117 mins",
                              "A midwife gets unexpected news from her father's old mistress.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BM2IwMDM4NDUtZjJlMS00YjQxLWIzNGEtMzE2OTMyMWU5ZmY0XkEyXkFqcGdeQXVyNDU0NjMyNTQ@._V1_UY209_CR0,0,140,209_AL_.jpg",
                              "https://www.youtube.com/watch?v=S_FLOFTvqdQ")
    menashe = media.Movie("Menashe","82 mins",
                          "Within Brooklyn's ultra-orthodox Jewish \
                           community, a widower battles for custody \
                           of his son. A tender drama performed entirely in Yiddish,\
                           the film intimately \
                           explores the nature of faith and the price of \
                           parenthood.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BZjQxYTc1MGEtNzhhOS00YWJmLWJlOWUtZWJlZjA5Yzk4NDA0XkEyXkFqcGdeQXVyNTAzMTY4MDA@._V1_UY209_CR0,0,140,209_AL_.jpg",
                          "https://www.youtube.com/watch?v=83UoZcdX__Y")
    p2p = media.Movie("Person to Person (2017)","84 mins",
                      "Follows a variety of New York characters as they \
                       navigate personal relationships \
                       and unexpected problems over the course of one day.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU4NDEzNjc3Ml5BMl5BanBnXkFtZTgwMDg2Nzg2MjI@._V1_UY209_CR2,0,140,209_AL_.jpg",
                      "https://www.youtube.com/watch?v=xYu0Mg8I3Mk")
    new_list = [the_emoji_movie,atomic_blonde,An_Inconvenient,the_midwife,menashe,p2p]
    return new_list

print(getmovie().new_list.the_midwife.title_media)
    
