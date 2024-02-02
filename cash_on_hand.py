from pathlib import Path
import csv
def calculate_cash_on_hand():
    file_path = Path.cwd() / "project_group" / "csv_reports" / "Cash-On-Hand.csv"
    
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skips the header

        coh = []

        for row in reader:
            coh.append([int(row[0]), int(row[1])])
    
    coh_diff_list = []

    # Calculate difference in cash on hand
    for i in range(len(coh) - 1):
        day = int(coh[i + 1][0])
        diff = int(coh[i + 1][1]) - int(coh[i][1])
        coh_diff_list.append((day, diff))

    # Identify if cash-on-hand is always increasing, decreasing, or fluctuating
    increasing = True
    for diff in coh_diff_list:
        if diff[1] <= 0:
            increasing = False
            break

    decreasing = True
    for diff in coh_diff_list:
        if diff[1] >= 0:
            decreasing = False
            break

    fluctuating = not increasing and not decreasing

    result = ""  # Initialize an empty string

    if increasing:
        max_increment_day = 0
        max_increment_amount = 0
        for day, diff in coh_diff_list:
            if diff > max_increment_amount:
                max_increment_day = day
                max_increment_amount = diff
        result += "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n"
        result += f"[HIGHEST CASH SURPLUS] DAY: {max_increment_day}, AMOUNT: {max_increment_amount}\n"

    elif decreasing:
        max_decrement_day = 0
        max_decrement_amount = 0
        for day, diff in coh_diff_list:
            if diff < max_decrement_amount:
                max_decrement_day = day
                max_decrement_amount = diff
        result += "[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY\n"
        result += f"[HIGHEST CASH DEFICIT] DAY: {max_decrement_day}, AMOUNT: {max_decrement_amount}\n"

    elif fluctuating:
        coh_deficit = []
    
        for day, diff in coh_diff_list:
            if diff < 0:
                coh_deficit.append((day, -diff))

        for day, amount in coh_deficit:
            result += f"[CASH DEFICIT] DAY: {day}, AMOUNT: {amount}\n"

        def sort_coh(item):
            return item[1]

        coh_deficit.sort(key=sort_coh, reverse=True)
        for i, (day, amount) in enumerate(coh_deficit[:3], start=1):
            if i == 1:
                deficit_rank = "HIGHEST" 

            elif i == 2:
                deficit_rank = '2ND HIGHEST'

            elif i == 3:
                deficit_rank = '3RD HIGHEST'

            result += f"[{deficit_rank} CASH DEFICIT] DAY: {day}, AMOUNT: {amount}\n"

    return result  # Return the final result string
