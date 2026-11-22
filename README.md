# Detector Event Processor (PASA Python and Git Workshop)

You will build a small program that reads gamma ray events from a detector, works out which
isotope each one came from, and draws a live graph.

## Before you start (we will do this together at the session)

You need these installed:
- **Python 3.10 or newer** (check with `python --version`)
- **Git** (check with `git --version`)
- **VS Code**
- **A free GitHub account**
- **matplotlib** (install with `pip install matplotlib`)

## Get the code (Git part of the session)

1. On GitHub, click **Fork** on this repository. This makes your own copy.
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

## Files

| File | What it does | Do you edit it? |
|---|---|---|
| `isotope.py` | One isotope (TODO 1, 2, 8) | Yes |
| `library.py` | All isotopes, lookup by name or energy (TODO 3, 4) | Yes |
| `detector.py` | Processes events (TODO 5, 6, 7, 12) | Yes |
| `chain.py` | Follows a decay chain (TODO 9) | Yes |
| `pqueue.py` | A priority queue (TODO 10, 11) | Yes |
| `main.py` | Runs everything | No |
| `plotter.py` | Draws the live graph | No |
| `check.py` | Tests your TODOs | No |
| `data/events.csv` | The detector events | No |
| `solutions/` | Finished versions, only for catching up | No |

## Run and check

- Test your work: `python check.py`
- Run the program: `python main.py`

## If you fall behind

Copy the finished file over yours, then keep going. Example for `library.py`:

- Mac or Linux: `cp solutions/library.py library.py`
- Windows: `copy solutions\library.py library.py`

## Save your work to GitHub

```
git add .
git commit -m "Finish detector processor"
git push
```
