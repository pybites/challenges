from boxes import Actor, Room, EndActor


class Level(object):
    """Instantiates all the rooms and actors for the game.
    Must have an EndActor in a reachable Room, with a proper and acquirable item_trigger to win the game
    After Rooms have been instantiated, 'doors' must be created by using room.add_destination(other_room)
    
    Attributes:
        start: The Room where the Player object is placed at the start of the game
        rooms: List of Rooms included in this level
            
    """
    def __init__(self):
        boss = Actor(dialog='Hello frined!',
                     name="A weird guy that I don't know. He looks friendly.",
                     description="Talk to the friendly weird guy I don't know",
                     item='Botato',
                     item_dialog='Take this botato, use is wisely!\n\nReceived 1 Holy Botato!',
                     done_dialog='You already have my everything, grasshopper.')
        altar = EndActor(dialog='It lacks a little something...',
                         name='An altar, in dire need of something to be put on it and worshipped',
                         description='Behold the altar',
                         item_trigger='Botato',
                         item_dialog='I place the holy relic into the altar, and I know that my Mission is fulfilled...')

        self.start = Room(description='This room is empty', content=[],
                     door_description='An empty and starting place')
        self.alt_room = Room(description="A pitch black room with a shining white altar in the center", content=[altar],
                        door_description='A place with a strange aura')
        self.end = Room(description='This normal looking room has a weird guy standing against the wall', content=[boss],
                   door_description='The light at the end of the tunnel')
        self.start.add_destination(self.alt_room)
        self.alt_room.add_destination(self.start)
        self.alt_room.add_destination(self.end)
        self.end.add_destination(self.alt_room)
        self.rooms = [self.start, self.alt_room, self.end]
