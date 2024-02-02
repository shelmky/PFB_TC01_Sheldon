from overheads import calculate_overheads
from cash_on_hand import calculate_cash_on_hand
from profit_loss import calculate_net_profit

o = calculate_overheads()
c = calculate_cash_on_hand()
n =calculate_net_profit()

with open('summary_report.txt', 'w', encoding='UTF-8') as file:
    file.write(f"{o}{c}{n}")
