# basicSalary = 20000

# so we have to calculate the 
# HRA of basicSalary = 20%
# TA of  basicSalary = 30%
# DA of basicSalary = 45%

# Calculate GrossSalary = ?
basicSalary = int(input('Enter Basic Salary: '))
hra = basicSalary*20/100
ta = basicSalary*30/100
da = basicSalary*45/100

GrossSalary = hra+ta+da+basicSalary
print("GrossSalary",GrossSalary)

