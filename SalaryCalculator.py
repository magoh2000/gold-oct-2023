"""
Salary calculator
Ask the user for the number of hours they worked last month and their hourly rate (both numbers should be floats). Use the following prompts:

How many hours did you work last month? << add a space at the end of this prompt
What is your hourly rate? << add a space at the end of this prompt

Then, show the following message with the calculated salary:

Last month, you earned {hours * hourly_rate} dollars
"""

# Prompt the user for the number of hours worked last month.
hours = input('How many hours did you work last month? ')

# Prompt the user for the hourly rate.
hourly_rate = input('What is your hourly rate? ')

# Convert the user inputs to floating-point numbers for calculations.
hours = float(hours)
hourly_rate = float(hourly_rate)

# Calculate the earnings by multiplying the hours worked by the hourly rate.
earnings = hours * hourly_rate

# Display the calculated earnings to the user.
print('Last month, you earned', earnings, 'dollars')
