
class Room(object):
    """A container for Actors and/or the Player.    
    
    Attributes:
        destinations: A dictionary with strings as keys and rooms as values
        For sanity, destinations may be appended after instancing the Rooms with the add_destination method
        description:  A string describing the room
        content: A list of Actors
        door_description: A string, describing how the user sees this room from other rooms
    """
    def __init__(self, description, door_description, content=None):
        self.description = description
        if content is None:
            self.content = []
        else:
            self.content = content
        self.destinations = {}
        self.door_description = door_description

    def __repr__(self):
        return self.door_description

    def add_destination(self, room):
        if isinstance(room, Room):
            self.destinations[room.door_description] = room

    @property
    def possible_actions_and_exits(self):
        return self.content.copy(), self.destinations.copy()


class Actor(object):
    """A non player character or immobile object for the Player to interact with.
    May give or trade items with the Player.

    Attributes:
        name: A string
        description:  A string describing the Actor
        dialog: A string that is displayed to the Player when he interacts with this Actor
        item: A string, the item is given after the second interaction with the Player, or, if item_trigger is not None,
        when the Player has item_trigger in his Inventory
        item_dialog: A string, displayed when adding the item to the Player's Inventory
        done_dialog: A string, displayed when the Player interacts with the Actor after it has given away its item
        unknown: A bool, starts as True, sets to False after the Player's first interaction with this Actor
        done: A bool, starts as False, sets to True after the Actor gives or trades its item
    """
    def __init__(self, name, dialog, description, item=None, item_trigger=None, item_dialog=None, done_dialog=None):
        self.name = name
        self.dialog = dialog
        self.description = description
        self.item = item
        self.item_trigger = item_trigger
        self.item_dialog = item_dialog
        self.done = False
        self.done_dialog= done_dialog
        self.unknown = True

    def interact(self, player):
        if self.done:
            return self.done_dialog if self.done_dialog else self.dialog
        try:
            if self.item_trigger in player.inventory and not self.unknown:
                self._trade_item(player)
                return self.done_dialog
        except AttributeError:
            pass
        if not self.item_trigger and self.item and not self.unknown:
            self._give_item(player)
            return self.item_dialog
        self.unknown = False
        return self.dialog

    def __repr__(self):
        return self.description

    def _give_item(self, player):
        if not self.done:
            player.inventory.append(self.item)
            self.done = True

    def _trade_item(self, player):
        if not self.done:
            player.inventory.append(self.item)
            player.inventory.remove(self.item_trigger)
            self.done = True


class EndActor(Actor):
    """A subclass of Actor, sets player.win to True after trading an item with the Player"""
    def interact(self, player):
        if self.done:
            return self.done_dialog if self.done_dialog else self.dialog
        if self.item_trigger in player.inventory and not self.unknown:
            self._trade_item(player)
            player.win = True
            return self.item_dialog
        self.unknown = False
        if not self.item_trigger and self.item:
            self._give_item(player)
            player.win = True
        return self.dialog


class Player(object):
    """A Player character. Moves between Rooms, interacts with Actors and holds items.

    Attributes:
        location: A Room object
        win:  A bool, starts at False, is set to True by an Actor, signaling the end of the game
        inventory: A list of strings
    """
    def __init__(self, start_location):
        self.win = False
        self.location = start_location
        self.inventory = []

    @property
    def actions_and_moves(self):
        return {**self.actions, **self.moves}

    @property
    def actions(self):
        actions, _ = self.location.possible_actions_and_exits
        action_dict = {f'{i}) {action}': (action.interact, self) for i, action in enumerate(actions, start=1)}
        action_dict[f'{len(actions)+1}) Inventory'] = (self.check_inventory, None)
        return action_dict

    @property
    def moves(self):
        _, exits = self.location.possible_actions_and_exits
        return {f'{i}) {room}': (self.move, self.location.destinations[room]) for i, room in enumerate(exits, start=len(self.actions)+1)}

    @staticmethod
    def list_to_dict(l, start):
        return {str(i): a for i, a in enumerate(l, start=start)}

    @staticmethod
    def perform_action(action):
        f, p = action
        if not p:
            return f()
        return f(p)

    def move(self, room):
        if isinstance(room, Room):
            self.location = room
            return f'I move into {room.door_description.lower()}'
        raise TypeError("Can't move to something that is not a Room")

    def check_inventory(self):
        if not self.inventory:
            return 'My bag is empty...'
        return '\n'.join([line for line in ['In my bag I have:'] + self.inventory[:]])
