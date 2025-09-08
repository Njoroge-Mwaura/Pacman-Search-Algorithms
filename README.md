# Pacman AI Search Project

Welcome to the Pacman Search Project. This project showcases classic search strategies (DFS, BFS, UCS, A*) inside a visual Pacman environment, plus a simple launcher for quick demos.

## Quick Start

- Launch the arcade-style menu:
```bash
python3 launcher.py
```
Select a Layout, the Search Agent, and a Search Function, then click START GAME.

- Run from the command line (no launcher):
```bash
# DFS
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=dfs,prob=PositionSearchProblem -z 1

# BFS
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs,prob=PositionSearchProblem -z 1

# UCS
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs,prob=PositionSearchProblem -z 1

# A* (Manhattan)
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=astar,prob=PositionSearchProblem,heuristic=manhattanHeuristic -z 1
```

## Included Layouts
- tinyMaze
- mediumMaze
- visualShowcase
- visualShowcaseLarge
- halloweenShowcase (many walls, chambers, capsules; works best at smaller zoom such as `-z 0.8`)

Tip: If the board is larger than your screen, reduce zoom: `-z 0.8 --frameTime 0.08`.

## What the Strategies Do
- Depth-First Search (DFS): explores one path as deep as possible before backtracking. Not guaranteed optimal in steps.
- Breadth-First Search (BFS): explores level-by-level; optimal in unit-cost mazes.
- Uniform Cost Search (UCS): expands the frontier with least path cost; optimal with nonnegative costs.
- A*: UCS guided by a heuristic (e.g., Manhattan) for fewer expansions while preserving optimality if the heuristic is admissible/consistent.

## Visual Logging (optional)
Search algorithms write lightweight events to `search_log.txt` (created when searches run) with expansions and goals. This never affects correctness.

## Troubleshooting
- Window cropped or overlapping: lower zoom (e.g., `-z 0.8`) or run text mode with `-t`.
- Halloween layout with ghosts: movement may be harder to track; add `-k 0` to remove ghosts for clean path visualization.
- Launcher does nothing when clicking Start: ensure you have Python 3 and Tkinter available on your system (`python3 -m tkinter`).

## Notes
- DFS/BFS/UCS/A* implementations live in `search.py` and are used by `SearchAgent` in `searchAgents.py`.
- The launcher (`launcher.py`) is a thin UI wrapper; it does not change algorithm behavior.
