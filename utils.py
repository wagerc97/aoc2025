"""
Utility functions for Advent of Code 2025
Common helper functions that can be used across multiple days.
"""
from typing import List, Tuple, Set, Dict, Any
from pathlib import Path


def read_input(day: int, filename: str = 'input.txt') -> str:
    """
    Read input file for a specific day.
    
    Args:
        day: The day number (1-12)
        filename: The name of the input file (default: 'input.txt')
        
    Returns:
        The content of the input file as a string
    """
    day_dir = Path(__file__).parent / f"day{day:02d}"
    input_path = day_dir / filename
    with open(input_path, 'r') as f:
        return f.read()


def read_lines(text: str, strip: bool = True) -> List[str]:
    """
    Split text into lines.
    
    Args:
        text: The input text
        strip: Whether to strip whitespace from each line
        
    Returns:
        List of lines
    """
    lines = text.strip().split('\n')
    if strip:
        lines = [line.strip() for line in lines]
    return lines


def read_numbers(text: str) -> List[int]:
    """
    Parse lines of numbers into a list of integers.
    
    Args:
        text: The input text with one number per line
        
    Returns:
        List of integers
    """
    return [int(line.strip()) for line in text.strip().split('\n') if line.strip()]


def read_grid(text: str) -> List[List[str]]:
    """
    Parse text into a 2D grid.
    
    Args:
        text: The input text
        
    Returns:
        2D list representing the grid
    """
    return [list(line) for line in text.strip().split('\n')]


def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """
    Calculate Manhattan distance between two points.
    
    Args:
        p1: First point (x, y)
        p2: Second point (x, y)
        
    Returns:
        Manhattan distance
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def _filter_neighbors(neighbors: List[Tuple[int, int]], max_x: int = None, max_y: int = None) -> List[Tuple[int, int]]:
    """
    Filter neighbors by bounds.
    
    Args:
        neighbors: List of neighbor coordinates
        max_x: Maximum x value (optional, for bounds checking)
        max_y: Maximum y value (optional, for bounds checking)
        
    Returns:
        Filtered list of neighbor coordinates
    """
    if max_x is not None and max_y is not None:
        return [(nx, ny) for nx, ny in neighbors 
                if 0 <= nx < max_x and 0 <= ny < max_y]
    return neighbors


def get_neighbors_4(x: int, y: int, max_x: int = None, max_y: int = None) -> List[Tuple[int, int]]:
    """
    Get 4 adjacent neighbors (up, down, left, right).
    
    Args:
        x: X coordinate
        y: Y coordinate
        max_x: Maximum x value (optional, for bounds checking)
        max_y: Maximum y value (optional, for bounds checking)
        
    Returns:
        List of neighbor coordinates
    """
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return _filter_neighbors(neighbors, max_x, max_y)


def get_neighbors_8(x: int, y: int, max_x: int = None, max_y: int = None) -> List[Tuple[int, int]]:
    """
    Get 8 adjacent neighbors (including diagonals).
    
    Args:
        x: X coordinate
        y: Y coordinate
        max_x: Maximum x value (optional, for bounds checking)
        max_y: Maximum y value (optional, for bounds checking)
        
    Returns:
        List of neighbor coordinates
    """
    neighbors = [
        (x+1, y), (x-1, y), (x, y+1), (x, y-1),
        (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)
    ]
    return _filter_neighbors(neighbors, max_x, max_y)
