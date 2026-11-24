import csv

from chain import DecayChain
from detector import Detector
from isotope import Isotope
from library import IsotopeLibrary
from plotter import LivePlot


def build_library():
    pass


def load_events(detector, filename):
    pass

def main():
    library = build_library()

    # Decay chain (Rn-222 and Po-218 are skipped, they have no gamma line)
    radium = library.get("Ra-226")
    lead = library.get("Pb-214")
    bismuth = library.get("Bi-214")
    radium.add_daughter(lead)
    radium.add_daughter(lead)   # adding twice must not make a duplicate
    lead.add_daughter(bismuth)

    """
    Space for code
    """

if __name__ == "__main__":
    main()
