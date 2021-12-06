import emplyClass as Employee
import csv
from csv import reader
import datetime

def readCSV(fileName):
    test = []
    with open(fileName, 'r') as csv_file:
        csv_reader = reader(csv_file)
        next(csv_reader, None)  # skip the headers
        list_of_rows = list(csv_reader)
        print(len(list_of_rows))
        for i in range (len(list_of_rows)):
            test.append(Employee.Employee(list_of_rows[i][0], list_of_rows[i][1],list_of_rows[i][2],
            list_of_rows[i][3], list_of_rows[i][4], list_of_rows[i][5],list_of_rows[i][6], list_of_rows[i][7]))
    return test                

def writeCSV(file,test):
    with open ('sample_data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        header = ['employee_id', 'full_name', "address", "ssn","date_of_birth","start_date",
                   "end_date", "job_title"]
        writer.writerow(header)
        for i in range(len(test)):
            full_name = test[i].getFull_name()
            employee_id= test[i].getEmployee_id()
            address=  test[i].getAddress()
            ssn=  test[i].getSsn()
            date_of_birth=  test[i].getDate_of_birth()
            start_date=  test[i].getStart_date()
            end_date=  test[i].getEnd_date()
            job_title=  test[i].getJob_title()
            var = [employee_id, full_name,address,ssn,
                  date_of_birth, start_date ,end_date ,job_title]
            writer.writerow(var)

#print annual review report
# I need to adjust annual review date to it implements below rule:
# if the emp hire year = this year do not add that empl to this year review report
def annualDatePrinter(empArray):
    print("Name  EndDate")
    for i in range(len(empArray)):
        name = empArray[i].getFull_name()
        if empArray[i].annualReview()!= 0:
            print(name, " ",empArray[i].annualReview())

# print employees left last month          
def employeesLeft(empArray):
    print("Name  EndDate")
    for i in range(len(empArray)):
        if empArray[i].empConvertToDate(2) !=0:
            name = empArray[i].getFull_name()
            print(name, " ",empArray[i].empConvertToDate(2))
    
 # add employee
def validate():
    try:
        x = input("Enter emp date : ")
        datetime.datetime.strptime(x, '%m/%d/%Y')
        return x
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        print("Incorrect data format, should be YYYY-MM-DD")
        return  validate()  
def addEmp(empArray): 
    id = input("Enter emp Id : ")
    name = input("Enter emp Name: ")
    address = input("Enter emp Address: ")
    ssn = input("Enter emp ssn: ")
    db= validate()
    # date format m/date/year
    startDate = validate()
    job_title= input("Enter emp job title: ")
    newEmp= Employee.Employee(id,name,address,ssn,db,startDate,end_date=None,job_title=job_title)
    empArray.append(newEmp)       
         
  

#print employee left last month


def main():
    fileName= 'sample_data.csv'
    empArray = readCSV(fileName)
    print("Annual Review Dates")
    annualDatePrinter(empArray)
    #emp left
    print("Former Employees")
    employeesLeft(empArray)
    addEmp(empArray)
    writeCSV(fileName, empArray)
    # 1 add an employee record
    # 2 adjust an employee record
    # 3 print employee informations
    # 4 get an employee info
        # by id
        # by name
       
main()                      