#!/usr/bin/env python3
"""
Main runner script for Advent of Code 2025
Run solutions for specific days or all days.
"""
import sys
import importlib
import time
from pathlib import Path


def run_day(day: int):
    """
    Run the solution for a specific day.
    
    Args:
        day: Day number (1-12)
    """
    day_str = f"{day:02d}"
    day_dir = Path(__file__).parent / f"day{day_str}"
    
    if not day_dir.exists():
        print(f"Day {day} does not exist!")
        return False
    
    # Check if solution file exists
    solution_file = day_dir / "solution.py"
    if not solution_file.exists():
        print(f"Solution file for day {day} does not exist!")
        return False
    
    # Import the solution module
    try:
        # Add the day directory to the path temporarily
        sys.path.insert(0, str(day_dir))
        solution = importlib.import_module('solution')
        
        print(f"\n{'='*50}")
        print(f"Running Day {day}")
        print(f"{'='*50}")
        
        start_time = time.time()
        solution.main()
        end_time = time.time()
        
        print(f"\nTime: {end_time - start_time:.4f} seconds")
        print(f"{'='*50}\n")
        
        # Remove the day directory from path
        sys.path.pop(0)
        return True
        
    except FileNotFoundError as e:
        if 'input.txt' in str(e):
            print(f"Input file for day {day} not found. Please add your puzzle input.")
        else:
            print(f"Error running day {day}: {e}")
        sys.path.pop(0)
        return False
    except Exception as e:
        print(f"Error running day {day}: {e}")
        import traceback
        traceback.print_exc()
        sys.path.pop(0)
        return False


def run_all_days():
    """Run solutions for all days."""
    total_start = time.time()
    success_count = 0
    
    for day in range(1, 13):
        if run_day(day):
            success_count += 1
    
    total_end = time.time()
    
    print(f"\n{'='*50}")
    print(f"Completed {success_count}/12 days")
    print(f"Total time: {total_end - total_start:.4f} seconds")
    print(f"{'='*50}")


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == 'all':
            run_all_days()
        else:
            try:
                day = int(arg)
                if 1 <= day <= 12:
                    run_day(day)
                else:
                    print("Day must be between 1 and 12")
                    sys.exit(1)
            except ValueError:
                print("Usage: python run.py [day_number|all]")
                print("Example: python run.py 1")
                print("Example: python run.py all")
                sys.exit(1)
    else:
        print("Usage: python run.py [day_number|all]")
        print("Example: python run.py 1")
        print("Example: python run.py all")
        sys.exit(1)


if __name__ == "__main__":
    main()
