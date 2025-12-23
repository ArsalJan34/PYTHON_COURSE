bill = float(input("What was the total bill : "))
tip = int(input("What percentage tip would you like to give: "))
People = int(input("How many people to split the bill"))
tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / People
final_amount = round(bill_per_person,2)
print(f"Each person has to pay bill of  : ${final_amount}")
