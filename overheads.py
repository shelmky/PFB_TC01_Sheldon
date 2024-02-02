from pathlib import Path
import csv

def calculate_overheads():
    file_path = Path.cwd() / "csv_reports" / "Overheads.csv"
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skips the header

        overheads = []

        for row in reader:
            overheads.append([row[0], float(row[1])])  # Convert the overhead value to float

        # Find the highest overhead category
        def sort_overheads(item):
            return item[1]
        
        overheads.sort(key=sort_overheads, reverse=True)
        highest_overhead = overheads[0]
        result = f"[HIGHEST OVERHEAD] {highest_overhead[0].upper()}: {highest_overhead[1]}%\n"

    return result

    
