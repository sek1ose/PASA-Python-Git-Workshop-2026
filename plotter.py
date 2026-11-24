import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


class LivePlot:
    """Bar chart of how many events each isotope has, redrawn after every event."""

    def __init__(self):
        plt.ion()
        self.figure, self.axes = plt.subplots(figsize=(9, 5))

    def update(self, counts):
        self.axes.clear()
        names = sorted(counts)
        values = [counts[name] for name in names]
        colors = ["tab:gray" if name == "Unknown" else "tab:blue" for name in names]
        self.axes.bar(names, values, color=colors)
        self.axes.set_ylabel("Events")
        self.axes.set_title("Detector Event Processor")
        self.axes.yaxis.set_major_locator(MaxNLocator(integer=True))
        self.axes.tick_params(axis="x", rotation=45)
        self.figure.tight_layout()
        plt.pause(0.15)

    def save(self, filename="spectrum.png"):
        self.figure.savefig(filename)

    def keep_open(self):
        plt.ioff()
        plt.show()
