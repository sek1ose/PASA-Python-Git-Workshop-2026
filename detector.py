from collections import deque

MIN_ENERGY = 20      # keV, below this is electronic noise
MAX_ENERGY = 3000    # keV, above this is outside the detector range


class Detector:
    """Takes gamma events in, identifies the isotope, keeps a history."""

    def __init__(self, library):
        self.library = library
        self.queue = deque()   # events waiting to be processed (first in, first out)
        self.history = []      # processed events (last in, first out)

    def add_event(self, time, energy):
        self.queue.append((time, energy))

    def process_next(self):
        # TODO 5: pop from self.queue, skip out-of-range energies with continue/or,
        # identify the isotope ("Unknown" if None), append (time, energy, name) to self.history,
        # and return the record (or None if no valid event remains)
        pass

    def undo_last(self):
        # TODO 6: if not self.history return None, otherwise pop and return the last record
        pass

    def count_by_isotope(self):
        # Bonus TODO: count how many times each isotope name appears in self.history using a dict
        pass
