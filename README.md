# Detector Event Processor (PASA Python and Git Workshop)

You will write a small program that reads gamma ray events from a detector, works out which
isotope each one came from, and draws a live graph.

You type the main code yourself (the classes and the logic). We give you the parts that are
long or repetitive: the graph code, the file that runs everything, the data, and a test file.

## You need (we set this up together at the start)

- **Python 3.10 or newer** (check: `python --version`)
- **Git** (check: `git --version`)
- **VS Code**
- **A free GitHub account**
- **matplotlib** (install: `pip install matplotlib`)

## Get the files (Git part of the session)

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
| `data/events.csv` | Given | The detector events |
| `data/isotopes.csv` | Given | The list of known isotopes |
| `main.py` | Given | Runs everything. Do not edit. |
| `plotter.py` | Given | Draws the live graph. Do not edit. |
| `check.py` | Given | Tests your work. Do not edit. |
| `isotope.py` | **You** | One isotope |
| `library.py` | **You** | All isotopes, lookup by name or energy |
| `detector.py` | **You** | Processes events |
| `chain.py` | **You** | Follows a decay chain |
| `pqueue.py` | **You** | A priority queue |

The five files you write do not exist yet. You create them in VS Code during the session.

## Run and check

- Test your work: `python check.py`
- Run the program: `python main.py` (it needs all five files)

## Save your work to GitHub

```
git add .
git commit -m "Finish detector processor"
git push
```

## If you fall behind

A finished version is on the `finished` branch of the main repository on GitHub.
Open it in your browser and copy the file you need.
