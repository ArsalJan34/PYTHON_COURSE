attendance_records = {
    "Ali": ["P", "A", "P", "P", "P", "A", "P"],
    "Sara": ["P", "P", "P", "P", "P", "P", "P"],
    "Usman": ["A", "A", "P", "A", "P", "A", "P"],
    "Hina": ["P", "P", "A", "P", "A", "P", "P"]
}

for student in attendance_records:
    records = attendance_records[student]
    total_days = len(records)
    present_days = records.count("P")

    percentage = (present_days / total_days) * 100

    if percentage >= 90:
        status = "Excellent"
    elif percentage >= 75:
        status = "Good"
    elif percentage >= 50:
        status = "Average"
    else:
        status = "Poor"

    print(student, "-", round(percentage, 2), "%", "-", status)
