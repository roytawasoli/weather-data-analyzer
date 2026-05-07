# Author: Roy
# GitHub: roytawasoli

# -*- coding: utf-8 -*-

# ==================================================
# Read CSV file and create a 2D list (list of rows)
# ==================================================

# Name of the CSV file (must be in the same folder)
filename = "weather_data.csv"

# Empty list to store all rows (each row will be a list of values)
nested_data = []

# Try to open the file
try:
    # Open with utf-8 encoding (to support Persian/English characters)
    with open(filename, "r", encoding="utf-8") as f:
        # Read all lines into a list of strings
        lines = f.readlines()
except FileNotFoundError:
    # If file not found, show error and exit
    print(f"Error: File '{filename}' not found.")
    exit()

# If file is empty, exit
if not lines:
    print("File is empty.")
    exit()

# First line contains column headers (e.g., Date,City,Temperature_C,...)
# Strip whitespace and split by comma to get list of headers
headers = [h.strip() for h in lines[0].strip().split(",")]

# Process each data line (skip the first line which is headers)
for line in lines[1:]:
    # Remove extra spaces from beginning and end of line
    line = line.strip()
    # Skip empty lines
    if not line:
        continue
    
    # Split line by comma and remove spaces from each part
    parts = [p.strip() for p in line.split(",")]
    
    # If number of parts is less than number of headers (due to empty cells),
    # fill missing parts with empty strings ''
    while len(parts) < len(headers):
        parts.append("")
    
    # Add this row (list of values) to our main 2D list
    nested_data.append(parts)

# ==================================================
# Index constants for each column (makes code readable)
# Each row is a list like: [Date, City, Temp, Rain, Wind]
# ==================================================
IDX_DATE = 0      # Date (e.g., 2026-04-01)
IDX_CITY = 1      # City name (e.g., Tehran)
IDX_TEMP = 2      # Temperature in Celsius (e.g., 18.5)
IDX_RAIN = 3      # Rainfall in mm (e.g., 0.0)
IDX_WIND = 4      # Wind speed in km/h (e.g., 15)

# ==================================================
# Helper functions
# ==================================================

def is_empty(val):
    """Check if value is empty (None, empty string, or only spaces)"""
    return val is None or str(val).strip() == ''

def to_float(val):
    """Convert string to float. Return None if empty or not a number."""
    if is_empty(val):
        return None
    try:
        return float(val)
    except:
        return None

# ==================================================
# Part 2: Detect broken sensors (missing data)
# ==================================================
def part2_check_broken_sensors():
    print("\n--- Part 2: Broken sensors (missing data) ---")
    found = False   # Did we find any broken sensor?
    
    # Loop through all rows
    for row in nested_data:
        missing = []   # List of sensors that have no value in this row
        
        # Check thermometer (temperature)
        if is_empty(row[IDX_TEMP]):
            missing.append("thermometer")
        # Check rain gauge (rainfall)
        if is_empty(row[IDX_RAIN]):
            missing.append("rain_gauge")
        # Check anemometer (wind speed)
        if is_empty(row[IDX_WIND]):
            missing.append("anemometer")
        
        # If at least one sensor is broken in this row
        if missing:
            found = True
            sensors = " and ".join(missing)
            print(f"⚠️ On {row[IDX_DATE]} in {row[IDX_CITY]}: {sensors} recorded no value.")
            # Print specific message for each broken sensor
            if "thermometer" in missing:
                print("    → Thermometer is broken.")
            if "rain_gauge" in missing:
                print("    → Rain gauge is broken.")
            if "anemometer" in missing:
                print("    → Anemometer is broken.")
            print()   # Empty line for readability
    
    # If no broken sensors found in any row
    if not found:
        print("✅ All sensors are working fine.\n")

# ==================================================
# Create a list of rows that have valid temperature (not empty)
# This will be used in parts 3, 5, and 6
# ==================================================
valid_temp_rows = []   # Empty list
for row in nested_data:
    if to_float(row[IDX_TEMP]) is not None:
        valid_temp_rows.append(row)

# ==================================================
# Part 3: Maximum temperature and average wind speed
# ==================================================
def part3_max_temp_avg_wind():
    print("\n--- Part 3: Max temperature & average wind speed ---")
    # If there are no rows with valid temperature
    if not valid_temp_rows:
        print("No valid temperature data.")
        return
    
    # List of all valid temperatures
    temps = [to_float(row[IDX_TEMP]) for row in valid_temp_rows]
    max_temp = max(temps)   # Highest temperature
    
    # List of all valid wind speeds (from all rows, even those with missing temp)
    wind_vals = [to_float(row[IDX_WIND]) for row in nested_data if to_float(row[IDX_WIND]) is not None]
    # Calculate average wind speed (if list not empty)
    avg_wind = sum(wind_vals) / len(wind_vals) if wind_vals else 0
    
    print(f"Highest temperature: {max_temp} °C")
    print(f"Average wind speed: {avg_wind:.2f} km/h")

# ==================================================
# Part 4: Strong wind warning (wind speed > 20 km/h)
# Print full rows as they appear in the original file
# ==================================================
def part4_wind_warning():
    print("\n--- Part 4: Strong wind warning (speed > 20 km/h) ---")
    warned = False   # Did we print at least one warning?
    
    for row in nested_data:
        w = to_float(row[IDX_WIND])
        if w is not None and w > 20:
            # Print the whole row in CSV format (comma separated)
            print(f"{row[IDX_DATE]},{row[IDX_CITY]},{row[IDX_TEMP]},{row[IDX_RAIN]},{row[IDX_WIND]}")
            warned = True
    
    if not warned:
        print("No wind speed above 20 km/h.")

# ==================================================
# Part 5: Three coldest records (based on valid temperature)
# ==================================================
def part5_coldest_three():
    print("\n--- Part 5: Three coldest records ---")
    # If less than 3 rows have valid temperature
    if len(valid_temp_rows) < 3:
        print("Less than 3 records with valid temperature.")
        # Print whatever we have
        for row in valid_temp_rows:
            print(f"{row[IDX_DATE]},{row[IDX_CITY]},{row[IDX_TEMP]},{row[IDX_RAIN]},{row[IDX_WIND]}")
        return
    
    # Sort rows from coldest (lowest temperature) to warmest (highest)
    # Key: the temperature value (float) of each row
    sorted_rows = sorted(valid_temp_rows, key=lambda r: to_float(r[IDX_TEMP]))
    # Print first 3 rows
    for i in range(3):
        r = sorted_rows[i]
        print(f"{r[IDX_DATE]},{r[IDX_CITY]},{r[IDX_TEMP]},{r[IDX_RAIN]},{r[IDX_WIND]}")

# ==================================================
# Part 6: Add Fahrenheit column and show first 5 rows (with headers)
# ==================================================
def part6_add_fahrenheit():
    print("\n--- Part 6: Add Fahrenheit column & first 5 rows ---")
    new_rows = []   # List to store rows with Fahrenheit added
    
    for row in valid_temp_rows:
        c = to_float(row[IDX_TEMP])           # Celsius temperature
        f = round(c * 1.8 + 32, 1)            # Fahrenheit formula, round to 1 decimal
        new_row = row.copy()                  # Copy the original row
        new_row.append(f)                     # Append Fahrenheit to the end
        new_rows.append(new_row)
    
    # Print headers (original columns + new column)
    print("Date,City,Temperature_C,Rainfall_mm,WindSpeed_kmh,Temperature_F")
    # Print first 5 rows (if less than 5, print all)
    for i in range(min(5, len(new_rows))):
        r = new_rows[i]
        # Index 0-4 are original, index 5 is Fahrenheit
        print(f"{r[0]},{r[1]},{r[2]},{r[3]},{r[4]},{r[5]}")

# ==================================================
# Main menu function (with detailed comments)
# ==================================================
def main_menu():
    """
    This function displays a menu to the user and runs the selected part.
    It loops until the user enters 0 (exit).
    """
    while True:   # Infinite loop until 'break'
        print("\n" + "=" * 40)   # Separator line
        print("Menu:")
        print("1 - Check broken sensors (Part 2)")
        print("2 - Max temp & average wind (Part 3)")
        print("3 - Strong wind warning (Part 4)")
        print("4 - Three coldest records (Part 5)")
        print("5 - Add Fahrenheit & show first 5 rows (Part 6)")
        print("0 - Exit")
        
        choice = input("Please enter a number: ")
        
        # Call the appropriate function based on user input
        if choice == "1":
            part2_check_broken_sensors()
        elif choice == "2":
            part3_max_temp_avg_wind()
        elif choice == "3":
            part4_wind_warning()
        elif choice == "4":
            part5_coldest_three()
        elif choice == "5":
            part6_add_fahrenheit()
        elif choice == "0":
            print("Goodbye!")
            break   # Exit the loop and end the program
        else:
            print("Invalid input. Enter 0-5.")

# ==================================================
# Program entry point: run the menu only if this script is executed directly
# ==================================================
if __name__ == "__main__":
    main_menu()
