# GIVEN FILE: you do not edit this one.
# It uses the classes you write in isotope.py, library.py, detector.py, chain.py and pqueue.py.
import csv

from chain import DecayChain
from detector import Detector
from isotope import Isotope
from library import IsotopeLibrary
from plotter import LivePlot


def build_library():
    library = IsotopeLibrary()
    with open("data/isotopes.csv") as file:
        for row in csv.DictReader(file):
            library.add(Isotope(row["name"], float(row["energy"]), row["half_life"]))
    return library


def load_events(detector, filename):
    with open(filename) as file:
        for row in csv.DictReader(file):
            detector.add_event(float(row["time"]), float(row["energy"]))


def main():
    library = build_library()

    # Decay chain (Rn-222 and Po-218 are skipped, they have no gamma line)
    radium = library.get("Ra-226")
    lead = library.get("Pb-214")
    bismuth = library.get("Bi-214")
    radium.add_daughter(lead)
    radium.add_daughter(lead)   # adding twice must not make a duplicate
    lead.add_daughter(bismuth)
    print("Decay chain:", " -> ".join(DecayChain(radium).trace_chain()))

    detector = Detector(library)
    load_events(detector, "data/events.csv")
    plot = LivePlot()

    while True:
        record = detector.process_next()
        if record is None:
            break
        time, energy, name = record
        print(f"t={time:6.1f} s   {energy:7.1f} keV   {name}")
        plot.update(detector.count_by_isotope())

    print("\nCounts:", detector.count_by_isotope())

    undone = detector.undo_last()
    print("Undid last event:", undone)
    plot.update(detector.count_by_isotope())

    print("\nUnknown events, highest energy first:")
    flagged = detector.flag_unknowns()
    while not flagged.is_empty():
        time, energy, name = flagged.pop()
        print(f"  {energy:7.1f} keV at t={time:.1f} s")

    answer = input("\nSave the graph as spectrum.png? (y/n) ")
    if answer.strip().lower() == "y":
        plot.save()
        print("Saved spectrum.png")
    plot.keep_open()


if __name__ == "__main__":
    main()
