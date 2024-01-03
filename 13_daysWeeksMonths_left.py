#WAP to find out how many days, weeks, months we have left so that we can live until
#90 years old.
# Input: Your current age.
# O/P:
# You have a days, b weeks and c months left.
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months
current_age =int( input('Enter your current age: '))
death_age = 90
years_left = 90 - current_age
print(f'You have {365 * years_left} days, {52 * years_left} weeks and {12 * years_left} months left.')