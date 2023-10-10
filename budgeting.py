"""
John has a hard time keeping his budget. Write a program to help him analyse his spendings. You are given a list with John's spendings for each month. Go through the list, and count the number of times...

a. the spendings were low (< 1000.0)
b. the spendings were normal (between 1000.0 and 2500.0 inclusive)
c. the spendings were high (> 2500.0)

Then, print the following to the output:

Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.

"""
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
lowspend = 0
normalspend = 0
highspend = 0

# Loop through the list of spendings
for spend in range(len(spendings)):
    if spendings[spend] < 1000:
        lowspend = lowspend + 1

    elif spendings[spend] >= 1000 and spendings[spend] <= 2500:
        normalspend = normalspend + 1

    else:
        highspend = highspend + 1


# Convert the counts to strings
spendlow = str(lowspend)
spendnormal = str(normalspend)
spendhigh = str(highspend)

# Remove spaces (if intended)
spendlow.replace(" ", "")
spendnormal.strip()
spendhigh.strip()



# Print the final result
print('Numbers of months with low spendings: ' + spendlow + ', normal spendings: ' + spendnormal + ', high spendings: ' + spendhigh + '.')
