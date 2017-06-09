# importing media.py and fresh_tomatoes.py files
import media
import fresh_tomatoes

#
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@"
                     "._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School of Rock", "After being kicked out of a rock band, Dewey Finn becomes a substitute "
                                               "teacher of a strict elementary private school, only to try and turn it "
                                               "into a rock band.",
                             "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/"
                             "large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg", "https://www.youtube.com/watch?v=28iEsXRAM9I")
ratatouille = media.Movie("Ratatouille", " A rat who can cook makes an unusual alliance with a young kitchen worker at "
                                         " a famous restaurant.", "http://www.gstatic.com/tv/thumb/dvdboxart/165058/"
                                                                  "p165058_d_v8_aa.jpg",
                          "https://www.youtube.com/watch?v=niD-jahFURU")
midnight_in_paris = media.Movie("Midnight in Paris", "While on a trip to Paris with his fiance's family, a nostalgic "
                                                     "screenwriter finds himself mysteriously going back to the 1920s "
                                                     "everyday at midnight.",
                                "http://t3.gstatic.com/images?q=tbn:ANd9GcT"
                                "k3ssys2bKM5-U6XMgvoD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("Hunger Games", "A televised competition in which two teenagers from each of the twelve "
                                           "Districts of Panem are chosen at random to fight to the death.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNz"
                           "kyNw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [avatar, toy_story, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
