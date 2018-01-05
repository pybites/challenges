from itertools import permutations

from data import DICTIONARY


class WordPossibilities:
	
	def __init__(self, players_draw):
	    self.players_draw = players_draw
	    self.perms = list(permutations(self.players_draw.sort()))
	
	
	def get_possible_dict_words(self):
	    """Get all possible words from players_draw which are valid dictionary words.
	    Use the _get_permutations_draw helper and DICTIONARY constant"""
	    return list(filter(lambda word: word in DICTIONARY, self.perms))