A custom HashMap implementation built from scratch in Python 

## Features

- Insert key-value pairs ( int or str )
- Retrieve values using keys
- Remove keys
- Update existing keys
- Collision handling using separate chaining
- Automatic resizing with rehashing
- Supports integer and string keys
- Custom implementation without using Python's built-in dictionary

## How It Works

The HashMap uses a list in another list to simulate buckets.

Each bucket contains a list of key-value pairs:
