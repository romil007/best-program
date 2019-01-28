from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
def sendtoemp(emailid,subject,message):
    msg=MIMEMultipart()    
    msg['From'] = "roojay0000@gmail.com"
    password='Aptech@123'
    msg['To']=emailid
    msg['Subject'] = subject    
    msg.attach(MIMEText(message, 'plain'))    
    server = smtplib.SMTP('smtp.gmail.com: 587') 
    server.starttls()    
    server.login(msg['From'], password)   
    server.sendmail(msg['From'], emailid ,msg.as_string()) 
    server.quit() 
    print ("successfully sent email to %s." % emailid)
class Employee:
    NEWID=0
    def __init__(self,name,dept,email,p):
        Employee.NEWID=Employee.NEWID+1
        self.Id=Employee.NEWID
        self.Name=name
        self.Dept=dept
        self.EmailId=email
        self.PassCode=str(p)
    def ShowDetails(self):
        print('ID:',self.Id)
        print('Name:',self.Name)
        print('Department:',self.Dept)
        print('EmailID:',self.EmailId)
    def GetName(self):
        return self.Name
    def GetEmailId(self):
        return self.EmailId
    def GetDept(self):
        return self.Dept
    def GetId(self):
        return self.Id
    def SetName(self,name):
        self.Name=name
    def SetEmailId(self, email):
        self.EmailId=email
    def SetDept(self, dept):
        self.Dept=dept
    def GetPassCode(self):
        return self.PassCode
    def SetPassCode(self,passcode):
        self.PassCode=passcode
        
class HR(Employee):
    
    def AddEmployee(self,employee):
        EMP.append(employee)
        print('Employee Added')
        message='Dear '+employee.GetName()+' Registered Successfuly.'+'Your Temp Password is :'+str(employee.GetPassCode())
        subject='Congratulations!'
        sendtoemp(employee.GetEmailId(),subject,message)
    def GetAllEmployees(self):
        for e in HR.EMP:
            e.ShowDetails()
        else:
            print('End of Employee List..')

EMP=[Employee('Kuldeep','Com','kuldeep.singh@develearn.in','kul001')]
def matchidpass(eid,passc):
    emp=None
    for e in EMP:
        if e.GetEmailId()==eid and e.GetPassCode()==passc:
            emp=e    
    return emp
    

def loginUser(emailid,passcode):
    r=random.Random()
    otp=r.randint(1000,9999)    
    message='Your OTP is:'+str(otp)
    emp=matchidpass(emailid,passcode)
    if emp!=None:
        sendtoemp(emailid,'OTP',message)
        attemp=0
        mat=False
        while(attemp<3):
            otpuser=int(input('Enter OTP:'))
            attemp+=1
            if otp==otpuser:
                mat=True
                break
        if(mat):
            c=int(input('1:add employee\t2:get detaile.\t3:show all'))
            h=HR('Kuldeep','Com','kuldeep.singh@develearn.in','kul001')
        
            if c==1:
                name=input('Name:')
                dept=input('Department:')
                email=input('EmailId:')
                pc=r.randint(1000,9999)
                h.AddEmployee(Employee(name,dept,email,pc))
            elif c==2:
                emp.ShowDetails()
            else:
                h.GetAllEmployees()
        else:
            print('Invalid OTP')
    else:
        print('Invalid ID or Password')

