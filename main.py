import csv

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

    plot.keep_open()


if __name__ == "__main__":
    main()
