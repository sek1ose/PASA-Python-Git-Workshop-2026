# Detector Event Processor (PASA Python and Git Workshop)

You will write a small program that reads gamma ray events from a detector, works out which
isotope each one came from, and draws a live graph.

## You need
- **Python 3.10 or newer** (check: `python --version`)
- **Git** (check: `git --version`)
- **VS Code**
- **A free GitHub account**
- **matplotlib** (install: `pip install matplotlib`)

## Get the files

1. On GitHub, click **Fork** on this repository.
2. In a terminal, clone **your fork** (use your username):
   ```
   git clone https://github.com/YOUR-USERNAME/detector-workshop.git
   cd detector-workshop
   ```
3. Make your own branch:
   ```
   git switch -c my-work
   ```
4. Open the folder in VS Code:
   ```
   code .
   ```

## What is in the folder

| File | Who writes it | What it is |
|---|---|---|
| `data/events.csv` | The detector events |
| `data/isotopes.csv` | The list of known isotopes |
| `main.py` | Runs everything. Do not edit. |
| `plotter.py` | Draws the live graph. Do not edit. |
| `isotope.py` | One isotope |
| `library.py` | All isotopes, lookup by name or energy |
| `detector.py` | Processes events |
| `chain.py` | Follows a decay chain |
| `pqueue.py` | A priority queue |

