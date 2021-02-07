import sys

from string import ascii_lowercase

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

import re

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    
    def __init__(self, word):
        self.movie = word.lower()
        self.movie_on_start = " ".join(self.movie)
        self.size = len(self.movie)
        self.nb_missed = 0

    def _str_movie_on_start(self):
        #movie_tmp = re.sub(r' ', '  ', self.movie)
        movie_tmp = re.sub(r'[a-z]', '_', self.movie)
        return " ".join(movie_tmp)
    
    def _str_movie_find_on_start(self):
        arr_tmp = []
        for l in list(" ".join(self.movie)):
            arr_tmp.append({"letter": l, "found": True if l.isdigit() else False})
        return arr_tmp

    def _str_movie_letter_found(self, movie, letter):
        for l in movie:
            if l["letter"] == letter:
                l["found"] = True
        return movie
    
    def _is_movie_found(self, movie):
        for l in movie:
            if l["letter"] in ASCII and l["found"] == False:
                return False
        return True
    
    def _print_movie_2_find(self, word):
        movie_tmp = ""
        for l in word:
            if l["found"] == True or l["letter"] not in ASCII:
                movie_tmp += l["letter"]
            elif l["letter"] == " ":
                movie_tmp += " "
            else:
                movie_tmp += PLACEHOLDER
        print (movie_tmp)

    def start(self):
        # write the first time
        print("The title's movie find like this : ")
        print(self._str_movie_on_start())
        movie_find = self._str_movie_find_on_start()
        # 
        while True:
           letter = input("Suggest a letter for the title's movie: ")
           # 
           if letter in self.movie:
               movie_find = self._str_movie_letter_found(movie_find, letter)
               if self._is_movie_found(movie_find):
                   print("you win ! The title's movie is : "+ self.movie_on_start)
                   break
           else:
               letter = ""
               self.nb_missed += 1
               print(HANG_GRAPHICS[self.nb_missed] + '\n')
           #
           if self.nb_missed == ALLOWED_GUESSES - 1:
               print("dead! the  movie was : "+  self.movie_on_start)
               break
           else:
               self._print_movie_2_find(movie_find)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    # print(word)
    # init / call program
    Hangman(word).start()
