employee_sales = {
    "Ali": 120000,
    "Sara": 68000,
    "Usman": 45000,
    "Hina": 30000,
    "Bilal": 98000
}

employee_performance={}
for employees in employee_sales:
   salary = employee_sales[employees]
   if salary >= 100000:
      employee_performance[employees] = "Excellent"
   elif salary >= 70000:
      employee_performance[employees] = "Good"
   elif salary >= 50000:
      employee_performance[employees] = "Average"
   else:
      employee_performance[employees] = "Poor"
print(employee_performance)
