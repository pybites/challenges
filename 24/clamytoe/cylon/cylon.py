from collections import MutableSequence


class Cylon(MutableSequence):
    """Provides next() and prev() methods to a list object

    If you need to traverse your list object in either direction,
    then this is the module to use.
    """

    def __init__(self, items=None):
        """Initialize object with the list of items that are passed to it"""
        self.items = list() if items is None else items
        self._index = 0

    def __delitem__(self, index):
        """Remove the item at the index indicated"""
        del self.items[index]

    def __getitem__(self, index):
        """Return the item at the index indicated"""
        return self.items[index]

    def __len__(self):
        """Return the length of the object"""
        return len(self.items)

    def __next__(self):
        """Return the next item in the object"""
        self._index = self._next()
        return self.items[self._index]

    def __prev__(self):
        """Return the previous item in the object"""
        self._index = self._prev()
        return self.items[self._index]

    def __repr__(self):
        info = "".join(
            [
                self.__class__.__name__,
                "(",
                f"items={len(self)} ",
                f"index={self._index}",
                ")",
            ]
        )
        return info

    def __setitem__(self, index, value):
        """Set the value of the object at the specified index"""
        self.items[index] = value

    def __str__(self):
        """Return currently selected item"""
        if len(self) > 0:
            return self.items[self._index]
        else:
            return "empty"

    def _find_stop(self, stop):
        """Helper function to wrap stencil"""
        return stop - len(self) if stop > len(self) - 1 else stop

    def _next(self):
        """Helper function for next"""
        if self._index == len(self) - 1:
            next_index = 0
        else:
            next_index = self._index + 1
        return next_index

    def _prev(self):
        """Helper function for previous"""
        if self._index == 0:
            prev_index = len(self) - 1
        else:
            prev_index = self._index - 1
        return prev_index

    def current(self):
        """Return the current item"""
        return self.items[self._index] if self.items else None

    def insert(self, index, value):
        """Insert value/object at the given index"""
        self.items.insert(index, value)

    def next(self):
        """Display the next item without changing current"""
        return self.items[self._next()]

    def prev(self):
        """Display the previous item without changing current"""
        return self.items[self._prev()]

    def stencil(self, count=2):
        """Return a list with before and after neighbors of current item

        Count determines how many of each are displayed.
        """
        stop = self._find_stop(self._index + count + 1)
        before = list(range(self._index - count, self._index))

        if stop < self._index:
            end = list(range(self._index, len(self)))
            front = list(range(stop))
            after = end + front
        else:
            after = list(range(self._index, stop))

        indexes = before + after
        return [self.items[i] for i in indexes]
