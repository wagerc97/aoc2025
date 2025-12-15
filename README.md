# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025) challenges.

## Project Structure

```
aoc2025/
├── day01/              # Day 1 challenge
│   ├── solution.py     # Solution code
│   └── input.txt       # Puzzle input
├── day02/              # Day 2 challenge
│   ├── solution.py
│   └── input.txt
├── ...                 # Days 3-11
├── day12/              # Day 12 challenge
│   ├── solution.py
│   └── input.txt
├── utils.py            # Common utility functions
├── run.py              # Main runner script
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/wagerc97/aoc2025.git
cd aoc2025
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## Usage

### Running a Specific Day

To run the solution for a specific day:

```bash
python run.py 1          # Run day 1
python run.py 5          # Run day 5
```

### Running All Days

To run all days at once:

```bash
python run.py all
```

### Running Directly

You can also run a day's solution directly:

```bash
cd day01
python solution.py
```

## Adding Puzzle Input

For each day, add your puzzle input to the corresponding `input.txt` file:

1. Go to [Advent of Code 2025](https://adventofcode.com/2025)
2. Navigate to the specific day
3. Copy your personalized puzzle input
4. Paste it into the corresponding `dayXX/input.txt` file

## Solution Template

Each day follows this template structure:

```python
def parse_input(input_text):
    """Parse the input text into a usable format"""
    # Parsing logic here
    pass

def part1(data):
    """Solve part 1 of the puzzle"""
    # Solution for part 1
    pass

def part2(data):
    """Solve part 2 of the puzzle"""
    # Solution for part 2
    pass

def main():
    """Main function to run both parts"""
    with open('input.txt', 'r') as f:
        input_text = f.read()
    
    data = parse_input(input_text)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
```

## Utility Functions

The `utils.py` module provides common helper functions:

- `read_input(day, filename)` - Read input file for a specific day
- `read_lines(text)` - Split text into lines
- `read_numbers(text)` - Parse lines of numbers
- `read_grid(text)` - Parse text into a 2D grid
- `manhattan_distance(p1, p2)` - Calculate Manhattan distance
- `get_neighbors_4(x, y)` - Get 4 adjacent neighbors
- `get_neighbors_8(x, y)` - Get 8 adjacent neighbors (including diagonals)

## Progress

- [ ] Day 1
- [ ] Day 2
- [ ] Day 3
- [ ] Day 4
- [ ] Day 5
- [ ] Day 6
- [ ] Day 7
- [ ] Day 8
- [ ] Day 9
- [ ] Day 10
- [ ] Day 11
- [ ] Day 12

## License

This project is for educational purposes. Advent of Code is created by [Eric Wastl](http://was.tl/).
