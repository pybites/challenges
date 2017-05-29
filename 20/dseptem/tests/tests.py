import unittest

# https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
import rooms
from rooms import boxes

class TestBoxes(unittest.TestCase):
    def setUp(self):
        """ setups a test level """
        self.actor_one = boxes.Actor('Dude', 'Hello dude', 'A dude', item='Dudething',
                                     item_dialog='Take this dude, dude', done_dialog='It is done, dude')
        self.actor_win = boxes.EndActor('Dudewin', 'It is time to win, dude, give me the thing', description='A winning dude',
                                        item_trigger='Dudething', item_dialog='YOU WIN DUDE', done_dialog='This should not happen')
        self.room_one = boxes.Room('A description', 'A door description', content=[self.actor_win])
        self.room_two = boxes.Room('A second description', 'A second door', content=[self.actor_one])
        self.room_one.add_destination(self.room_two)
        self.room_two.add_destination(self.room_one)
        self.player = boxes.Player(self.room_one)

    def test_starting_location(self):
        """ make sure the player starts in the starting location """
        self.assertEqual(self.player.location, self.room_one)

    def test_first_interact_dude(self):
        """ make sure the player gets the first dialog when interacting for the first time """
        self.player.location = self.room_two
        self.assertEqual(self.actor_one.interact(self.player), self.actor_one.dialog)

    def test_second_interact_dude(self):
        """ make sure the player gets the item on the second interaction, with its dialog"""
        self.player.location = self.room_two
        self.actor_one.interact(self.player)
        self.assertEqual(self.actor_one.interact(self.player), self.actor_one.item_dialog)
        self.assertIn('Dudething', self.player.inventory)

    def test_third_interact_dude(self):
        """ make sure the player gets the done dialog """
        self.player.location = self.room_two
        self.actor_one.interact(self.player)
        self.actor_one.interact(self.player)
        self.actor_one.interact(self.player)
        self.assertEqual(self.actor_one.interact(self.player), self.actor_one.done_dialog)

    def test_win(self):
        """ make sure the player can win when he has the win condition item """
        self.player.location = self.room_two
        self.actor_one.interact(self.player)
        self.actor_one.interact(self.player)
        self.player.location = self.room_one
        self.actor_win.interact(self.player)
        self.actor_win.interact(self.player)
        self.assertNotIn('Dudething', self.player.inventory)
        self.assertTrue(self.player.win)

if __name__ == '__main__':
    unittest.main()
