from pathlib import Path
import csv

def calculate_net_profit():
    file_path = Path.cwd() / "csv_reports" / "Profits_and_Loss.csv"
    
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # Skips the header

        pl = []

        for row in reader:
            pl.append([row[0], row[1], row[2], row[3], row[4]])

    pl_diff_list = []

    # Calculate difference in profit and loss
    for i in range(len(pl) - 1):
        day = int(pl[i + 1][0])
        diff = int(pl[i + 1][4]) - int(pl[i][4])
        pl_diff_list.append((day, diff))

    # Identify if profit and loss is always increasing, decreasing, or fluctuating
    increasing = True
    for diff in pl_diff_list:
        if diff[1] <= 0:
            increasing = False
            break

    decreasing = True
    for diff in pl_diff_list:
        if diff[1] >= 0:
            decreasing = False
            break

    fluctuating = not increasing and not decreasing

    result = ""  # Initialize an empty string

    if increasing:
        max_increment_day = 0
        max_increment_amount = 0
        for day, diff in pl_diff_list:
            if diff > max_increment_amount:
                max_increment_day = day
                max_increment_amount = diff
        result += "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n"
        result += f"[NET PROFIT CASH SURPLUS] DAY: {max_increment_day}, AMOUNT: {max_increment_amount}\n"

    elif decreasing:
        max_decrement_day = 0
        max_decrement_amount = 0
        for day, diff in pl_diff_list:
            if diff < max_decrement_amount:
                max_decrement_day = day
                max_decrement_amount = diff
        result += "[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n"
        result += f"[HIGHEST NET PROFIT DEFICIT] DAY: {max_decrement_day}, AMOUNT: {max_decrement_amount}\n"

    elif fluctuating:
        pl_deficit = []
    
        for day, diff in pl_diff_list:
            if diff < 0:
                pl_deficit.append((day, -diff))

        for day, amount in pl_deficit:
            result += f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: {amount}\n"

        def sort_net_profit(item):
            return item[1]

        pl_deficit.sort(key=sort_net_profit, reverse=True)
        for i, (day, amount) in enumerate(pl_deficit[:3], start=1):
            if i == 1:
                deficit_rank = "HIGHEST" 

            elif i == 2:
                deficit_rank = '2ND HIGHEST'

            elif i == 3:
                deficit_rank = '3RD HIGHEST'

            result += f"[{deficit_rank} NET PROFIT DEFICIT] DAY: {day}, AMOUNT: {amount}\n"

    return result  # Return the final result string
