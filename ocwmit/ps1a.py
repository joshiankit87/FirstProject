annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_saving = 0.0
monthly_salary = annual_salary / 12
monthly_contribution = monthly_salary * portion_saved
months = 0
while 1:
    if current_saving >= total_cost * portion_down_payment:
        print("Number of months:%d" % months)
        break
    else:
        current_saving += current_saving * 0.04 / 12
        current_saving += monthly_contribution
        months += 1
