# Energy Over Time Visualization

This program reads simulation data from text files and visualizes the total energy over time for various conditions. The focus is on different relaxation steps with a fixed Δt value and without sub-stepping.

## Features

- Read data from external text files containing length errors and total energy values.
- Generate a plot that showcases total energy over time for three conditions: 1, 10, and 100 relaxation steps.
- Includes labels, legends, and gridlines for better visualization.

## Usage

1. Ensure you have the necessary data files (`condition_1.txt`, `condition_10.txt`, and `condition_100.txt`) in the same directory as the script.
2. Run the script using Python. Ensure you have `matplotlib` installed:

   `pip install matplotlib`

   And then:

   `python main.py`

3. The script will read the data and display the plot showing the energy over time for each condition.

## Data File Format

The expected format for the data files is:

``

## Dependencies

- `matplotlib`
