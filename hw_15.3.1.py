import xml.etree.ElementTree as ET


tree = ET.parse('employees.xml')
root = tree.getroot()

total_employees = 0
total_salary = 0

for employee in root.findall('employee'):
    total_employees += 1
    total_salary += int(employee.find('salary').text)

print(f'Всего сотрудников: {total_employees}')
print(f'Суммарная зарплата: {total_salary}')
