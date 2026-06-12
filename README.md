# BookBot

BookBot is a command-line Python project from the [Boot.dev](https://www.boot.dev) backend curriculum.

It analyzes a text file and prints:

- Total word count
- Character frequency counts (sorted from most common to least common)
- Alphabetic characters only in the final character report

## Project Structure

```
python-bookbot/
|- main.py
|- stats.py
|- books/
|  |- frankenstein.txt
|  |- mobydick.txt
|  |- prideandprejudice.txt
```

## How It Works

1. `main.py` reads the book file from a command-line argument.
2. `stats.py` computes:
	- Number of words
	- Number of occurrences for each character (case-insensitive)
3. Results are sorted and printed in a formatted report.

## Requirements

- Python 3.10+ (works on current Python 3 releases)

No third-party packages are required.

## Usage

From the project root, run:

```bash
python3 main.py books/frankenstein.txt
```

If no path is provided (or too many args are given), BookBot shows:

```text
Usage: python3 main.py <path_to_book>
```

## Example Output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
```

## Notes for Boot.dev

This project is intentionally simple and focused on core Python fundamentals:

- File I/O
- Dictionaries and lists
- Sorting with custom keys
- Command-line arguments
- Basic program structure across modules
