"""
Salary calculator
Ask the user for the number of hours they worked last month and their hourly rate (both numbers should be floats). Use the following prompts:

How many hours did you work last month? << add a space at the end of this prompt
What is your hourly rate? << add a space at the end of this prompt

Then, show the following message with the calculated salary:

Last month, you earned {hours * hourly_rate} dollars
"""

hours = input('How many hours did you work last month? ')
hourly_rate = input('What is your hourly rate? ')
hours = float(hours)
hourly_rate = float(hourly_rate)
print('Last month, you earned', hours*hourly_rate,'dollars')