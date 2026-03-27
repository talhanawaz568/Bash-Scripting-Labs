from datetime import datetime, timedelta

# 1. You MUST define current_datetime first
current_datetime = datetime.now()

# Calculate yesterday's date
yesterday = current_datetime - timedelta(days=1)

# Calculate next week's date
next_week = current_datetime + timedelta(weeks=1)

# Print yesterday's and next week's date
print("Yesterday's date:", yesterday)
print("Next week's date:", next_week)

formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("Formatted date and time:", formatted_datetime)
