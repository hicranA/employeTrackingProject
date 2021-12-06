# Creates the Employee class and saves employee  information

import csv
from csv import reader
import datetime

class Employee:
    empCount =0
    ids_list = set()

    ############ consturactor method #########################   
                  
    def __init__(self, employee_id, full_name,address,ssn, date_of_birth, 
                start_date, end_date, job_title):
        self.__employee_id =  employee_id
        self.__full_name = full_name
        self.__address= address
        self.__ssn= ssn
        self.__date_of_birth= date_of_birth
        self.__start_date= start_date
        self.__end_date= end_date
        self.__job_title= job_title
        self.__emp_status = None
        #self.__annual_review= None
        Employee.empCount += 1
    

            
            
    @property
    def empSta(self):
        var = self.__end_date
        if len(var):
            self.__emp_status= "Not active"
        else:
            self.__emp_status= "Active" 
        return    self.__emp_status
     

                
       
    ############### settters ################################
    #1 set employee_id 
    def setEmployee_id (self,employee_id):
        self.__employee_id  = employee_id 
    #2 set full_name
    def setFull_name(self,full_name):
        self.__full_name = full_name
    #3 set address
    def setAddress(self, address):
        self.__address= address
    #4 set ssn
    def setSsn(self, ssn):
        self.__ssn= ssn
    #5 set date_of_birth
    def setDate_of_birth(self, date_of_birth):
        self.__date_of_birth= date_of_birth   
    # 6  start_date
    def setStart_date(self, start_date):
        self.__start_date= start_date
     # 7 end_date
    def setEnd_date(self, end_date):
        self.__end_date= end_date
    # 8  job_title
    def setJob_title(self,job_title ):
        self.__job_title= job_title
    ################################# setters ends ##########################          

    ######################### accessors methods #############################
    #1 get employee_id 
    def getEmployee_id (self):
        return self.__employee_id 
    #2 get full_name
    def getFull_name(self):
       return self.__full_name
    #3 get address
    def getAddress(self):
        return self.__address
    #4 get set ssn
    def getSsn(self):
        return self.__ssn
    #5 get date_of_birth
    def getDate_of_birth(self):
        return self.__date_of_birth
    # 6  get start_date
    def getStart_date(self):
        return self.__start_date
     # 7 get end_date
    def getEnd_date(self):
        return  self.__end_date
    # 8  get job_title
    def getJob_title(self ):
       return self.__job_title
    # 9 emp status
    def getEmp_status(self):
        return self.emp_status

    ################################### accessor methods ends ##########################   
    ###################### printers######################
    # print funct
    def __str__(self):
        result = "Name: " + self.getFull_name() + "\n" + \
                "ID number: " + str(self.getEmployee_id())
        return result
    ## special methods###
    ### emp annual review date
    def annualReview(self):
        if self.empSta  == "Active":
            today= tday = datetime.date.today()
            empdate = datetime.datetime.strptime(self.__start_date,'%m/%d/%Y').date() 
            tdelta= datetime.timedelta(days=1)
            modHireDate = empdate- tdelta
            x = modHireDate.replace(year=tday.year)
            return x
        else:
            y=int(0)
            return y  
  
        
    ### emp last month left tracker 

    def empConvertToDate(self,select):   
        if select == 1:
            startDate = self.__start_date
            return  datetime.datetime.strptime(startDate,'%m/%d/%Y').date() 
        if select == 2 :
            if  self.empSta == "Not active":
                endDate = self.__end_date
                return  datetime.datetime.strptime(endDate,'%m/%d/%Y').date()
            else:
                return 0      
               

        

            