import media
import fresh_tomatoes

# each instance has the title of the movie, description, poster image and a
# youtube trailer.
toy_story = media.Movie("Toy Story",
                        "Animation: A cowboy doll is profoundly threatened and"
                        " jealous when a new spaceman figure supplants him as "
                        "top toy in a boy's room.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5B"
                        "MDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyX"
                        "kFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about "
                     "the true nature of his reality and his "
                     "role in the war against its controllers.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQ"
                     "zOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZ"
                     "jNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY10"
                     "00_CR0,0,665,1000_AL_.jpg",
                     "https://youtu.be/m8e-FF8MsqU")

lucy = media.Movie("Lucy",
                   "When a boyfriend tricks Lucy (Scarlett Johansson) into "
                   "delivering a briefcase to a supposed business contact, a "
                   "once-carefree student is abducted by thugs who intend to "
                   "turn her into a drug mule. She is surgically implanted "
                   "with a package containing a powerful chemical, but it "
                   "leaks into her system, giving her superhuman abilities, "
                   "including telekinesis and telepathy. With her former "
                   "captors in pursuit, Lucy seeks out a neurologist (Morgan "
                   "Freeman), who she hopes will be able to help her.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BODcxM"
                   "zY3ODY1NF5BMl5BanBnXkFtZTgwNzg1NDY4MTE"
                   "@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
                   "https://youtu.be/bN7ksFEVO9U")

law_abiding_citizen = media.Movie("Law Abiding Citizen",
                                  "A man with nothing left to lose seeks "
                                  "justice in the system that denied him his.",
                                  "http://q.likesuccess.com/114/5654421-"
                                  "law-abiding-citizen-movie.jpg",
                                  "https://youtu.be/BJ3tHqGlCHg")

iron_man = media.Movie("Iron Man",
                       "After being held captive in an Afghan cave, "
                       "billionaire engineer Tony Stark creates a unique "
                       "weaponized suit of armor to fight evil.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BM"
                       "TczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw"
                       "@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                       "https://youtu.be/8hYlB38asDY")

pineapple_express = media.Movie("Pineapple Express",
                                "A process server and his marijuana dealer "
                                "wind up on the run from hitmen and a "
                                "corrupt police officer after he witnesses "
                                "his dealer's boss murder a competitor while "
                                "trying to serve papers on him.",
                                "https://images-na.ssl-images-amazon.com/"
                                "images/M/MV5BMTY1MTE4NzAwM15BMl5BanBnXkFtZ"
                                "TcwNzg3Mjg2MQ@@._V1_.jpg",
                                "https://youtu.be/_GnV2u30oOU")

movies = [toy_story, matrix, lucy, law_abiding_citizen, iron_man,
          pineapple_express]
# call function in fresh_tomatoes.py passing in the movies variable array.
fresh_tomatoes.open_movies_page(movies)
