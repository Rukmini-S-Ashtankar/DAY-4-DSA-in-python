salary = int(input('Enter your salary: '))
rating = int(input('Enter your performance appraisal rating: '))
increment = 0
if rating >=1 and rating <=3:
    increment = salary*10/100
elif rating >=3.1 and rating<=4:
    increment = salary*30/100
elif rating >=4.1 and rating<=5:
    increment = salary*40/100
else:
    print('Invalid rating')
print('Increment Salary: ',increment+salary)