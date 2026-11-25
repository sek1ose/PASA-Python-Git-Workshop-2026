class IsotopeLibrary:
    """Stores every known isotope, by name and by gamma energy."""

    def __init__(self):
        self.isotopes = {}   # name -> Isotope
        self.lines = []      # (energy, name) tuples

    def add(self, isotope):
        self.isotopes[isotope.name] = isotope
        self.lines.append((isotope.energy, isotope.name))

    def get(self, name):
        # TODO 3: return the Isotope for name using try/except KeyError, or None if missing
        pass

    def find_by_energy(self, energy, tolerance=2.0):
        # TODO 4: loop through self.lines, get each isotope, and return the first match (or None)
        pass
