from tkinter import *
import sqlite3
import random
import time
import datetime
connection = sqlite3.connect("Information.db")

#Define information
def SelectEmployee():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM EmployeeTBL")

    employeelist = cursor.fetchall()
    for e in employeelist:

        print(" ",e[0]," ",e[1]," ",e[2]," ",e[3]," ",e[4]," ",e[5]," ",e[6]," ",e[7]," ")
    connection.close()  

#name app and parameters
payroll = Tk()
payroll.geometry =("1350x650+0+0")
#add title
payroll.title("Actually working payroll system")

#variables
EmployeeName = StringVar()
Address = StringVar()
Reference = StringVar()
EmployerName = StringVar()
CityWeighting = StringVar()
BasicSalary = StringVar()
OverTime = StringVar()
GrossPay = StringVar()
NetPay = StringVar()
Tax= StringVar()
Contact = StringVar()
Pension = StringVar()
StudentLoan = StringVar()
NIPayment = StringVar()
Deductions = StringVar()
PostCode = StringVar()
Gender = StringVar()
PayDate = StringVar()
TaxPeriod = StringVar()
NICode = StringVar()
TaxablePay = StringVar()
PensionablePay = StringVar()
OtherPayments = StringVar()

#Select employee================
def callback(*event):    

    EmployeeNo1=LstEmployeeNo.get(LstEmployeeNo.curselection())

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM EmployeeTBL WHERE EmployeeNo = '" + EmployeeNo1[0] + "'")

    selectedEmployeeDetails = cursor.fetchall();
    
    #print(EmployeeNo1)
    #print(selectedEmployeeDetails[0][2])
    #print(selectedEmployeeDetails[0][3])

#import info from database=============================
    txtNICode.delete(0, END)
    txtNICode.insert(0, selectedEmployeeDetails[0][1])

    txtEmployeeName.delete(0, END)    
    txtEmployeeName.insert(0, selectedEmployeeDetails[0][2] + " " + selectedEmployeeDetails[0][3])

    txtAddress.delete(0, END)
    txtAddress.insert(0, selectedEmployeeDetails[0][4])

    txtPostCode.delete(0, END)
    txtPostCode.insert(0, selectedEmployeeDetails[0][5])

    txtGender.delete(0, END)
    txtGender.insert(0, selectedEmployeeDetails[0][6])

    txtContact.delete(0, END)
    txtContact.insert(0, selectedEmployeeDetails[0][9])

def save():
    if txtEmployeeName == txtEmployeeName:      
        print("No Changes Made")
    #else:
        #txtEmployeeName.update(selectedEmployeeDetails[0][2])
        

#Reset Button Def=============================================

def reset():
    EmployeeName.set("")
    Address.set("")
    Reference.set("")
    EmployerName.set("")
    Contact.set("")
    BasicSalary.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    Tax.set("")
    Pension.set("")
    StudentLoan.set("")
    NIPayment.set("")
    Deductions.set("")
    PostCode.set("")
    Gender.set("")
    PayDate.set("")
    TaxPeriod.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionablePay.set("")
    OtherPayments.set("")

#Exit Button Def=======================================

def exit():
    payroll.destroy()

#main frame
Tops=Frame(payroll, width=1350, height=50, bd=16, relief="raise")
Tops.pack(side=TOP)

#left and right frame
LF=Frame(payroll, width=700, height=650, bd=16, relief="raise")
LF.pack(side=LEFT)
RF=Frame(payroll, width=600, height=650, bd=16, relief="raise")
RF.pack(side=RIGHT)

#title to mainframe
lableinfo =Label(Tops,font=("arial",50,"bold"),text="     Actually Working Payroll System       ",fg="Steel Blue",bd=1)
lableinfo.grid(row=0,column=0)

#inner frame to left
LeftInsideLF=Frame(LF,width=700, height=100, bd=8, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF,width=325, height=400, bd=8, relief="raise")
LeftInsideLFLF.pack(side=LEFT)
LeftInsideRFRF=Frame(LF,width=325, height=400, bd=8, relief="raise")
LeftInsideRFRF.pack(side=RIGHT)

#inner frame to right
RightInsideLF=Frame(RF,width=600, height=200, bd=8, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF,width=300, height=400, bd=8, relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF,width=300, height=400, bd=8, relief="raise")
RightInsideRFRF.pack(side=RIGHT)

#function boxes and labels===============================
#Left Side=================================

#Employee No
lblEmployeeNo = Label (LeftInsideLF, font =('arial', 12,'bold' ), text="Employee Number",fg="Steel Blue", bd=10, anchor='w')
lblEmployeeNo.grid(row=0,column=0)
LstEmployeeNo = Listbox(LeftInsideLF,font=('arial',12,'bold'), bd=10, width=36,bg='powder blue', justify = 'left')
LstEmployeeNo.grid(row=0,column=1)

#Employee Name
lblEmployeeName = Label(LeftInsideLF,font=("arial",12,"bold"),text="Employee Name",fg="Steel Blue",bd=10,anchor="w")
lblEmployeeName.grid(row=1,column=0)
txtEmployeeName = Entry(LeftInsideLF,font=("arial",12,"bold"),bd=10,width=40,bg="powder blue",justify="right", textvariable=EmployeeName)
txtEmployeeName.grid(row=1,column=1)

#Address
lblAddress = Label(LeftInsideLF,font=("arial",12,"bold"),text="Address",fg="Steel Blue",bd=10,anchor="w")
lblAddress.grid(row=2,column=0)
txtAddress = Entry(LeftInsideLF,font=("arial",12,"bold"),bd=10,width=40,bg="powder blue",justify="right", textvariable=Address)
txtAddress.grid(row=2,column=1)

#Contact No.
lblContact = Label(LeftInsideLF,font=("arial",12,"bold"),text="Contact No.",fg="Steel Blue",bd=10,anchor="w")
lblContact.grid(row=3,column=0)
txtContact = Entry(LeftInsideLF,font=("arial",12,"bold"),bd=10,width=40,bg="powder blue",justify="right", textvariable=Contact)
txtContact.grid(row=3,column=1)

#Reference
lblReference = Label(LeftInsideLF,font=("arial",12,"bold"),text="Reference",fg="Steel Blue",bd=10,anchor="w")
lblReference.grid(row=4,column=0)
txtReference = Entry(LeftInsideLF,font=("arial",12,"bold"),bd=10,width=40,bg="powder blue",justify="right", textvariable=Reference)
txtReference.grid(row=4,column=1)

#Employer Name
lblEmployerName = Label(LeftInsideLF,font=("arial",12,"bold"),text="Employer Name",fg="Steel Blue",bd=10,anchor="w")
lblEmployerName.grid(row=5,column=0)
txtEmployerName = Entry(LeftInsideLF,font=("arial",12,"bold"),bd=10,width=40,bg="powder blue",justify="right", textvariable=EmployerName)
txtEmployerName.grid(row=5,column=1)

#Left Inside================================

#Basic Salary
lblBasicSalary = Label(LeftInsideLFLF,font=("arial",12,"bold"),text="Basic Salary",fg="Steel Blue",bd=10,anchor="w")
lblBasicSalary.grid(row=0,column=0)
txtBasicSalary = Entry(LeftInsideLFLF,font=("arial",12,"bold"),bd=14,width=10,bg="powder blue",justify="right", textvariable=BasicSalary)
txtBasicSalary.grid(row=0,column=1)

#OverTime
lblOverTime = Label(LeftInsideLFLF,font=("arial",12,"bold"),text="Over Time",fg="Steel Blue",bd=10,anchor="w")
lblOverTime.grid(row=1,column=0)
txtOverTime = Entry(LeftInsideLFLF,font=("arial",12,"bold"),bd=14,width=10,bg="powder blue",justify="right", textvariable=OverTime)
txtOverTime.grid(row=1,column=1)

#GrossPay
lblGrossPay = Label(LeftInsideLFLF,font=("arial",12,"bold"),text="Gross Pay",fg="Steel Blue",bd=10,anchor="w")
lblGrossPay.grid(row=2,column=0)
txtGrossPay = Entry(LeftInsideLFLF,font=("arial",12,"bold"),bd=14,width=10,bg="powder blue",justify="right", textvariable=GrossPay)
txtGrossPay.grid(row=2,column=1)

#NetPay
lblNetPay = Label(LeftInsideLFLF,font=("arial",12,"bold"),text="Net Pay",fg="Steel Blue",bd=10,anchor="w")
lblNetPay.grid(row=3,column=0)
txtNetPay = Entry(LeftInsideLFLF,font=("arial",12,"bold"),bd=14,width=10,bg="powder blue",justify="right", textvariable=NetPay)
txtNetPay.grid(row=3,column=1)

#inside left right=================

#Tax
lblTax = Label(LeftInsideRFRF,font=("arial",12,"bold"),text="Tax",fg="Steel Blue",bd=10,anchor="w")
lblTax.grid(row=0,column=2)
txtTax = Entry(LeftInsideRFRF,font=("arial",12,"bold"),bd=14,width=10,bg="powder blue",justify="right", textvariable=Tax)
txtTax.grid(row=0,column=3)

#StudentLoan
lblStudentLoan = Label(LeftInsideRFRF,font=("arial",12,"bold"),text="Student Loan",fg="Steel Blue",bd=10,anchor="w")
lblStudentLoan.grid(row=1,column=2)
txtStudentLoan = Entry(LeftInsideRFRF,font=("arial",12,"bold"),bd=14,width=10,bg="powder blue",justify="right", textvariable=StudentLoan)
txtStudentLoan.grid(row=1,column=3)

#NIPayment
lblNIPayment = Label(LeftInsideRFRF,font=("arial",12,"bold"),text="NI Payment",fg="Steel Blue",bd=10,anchor="w")
lblNIPayment.grid(row=2,column=2)
txtNIPayment = Entry(LeftInsideRFRF,font=("arial",12,"bold"),bd=14,width=10,bg="powder blue",justify="right", textvariable=NIPayment)
txtNIPayment.grid(row=2,column=3)

#Deductions
lblDeductions = Label(LeftInsideRFRF,font=("arial",12,"bold"),text="Deductions",fg="Steel Blue",bd=10,anchor="w")
lblDeductions.grid(row=3,column=2)
txtDeductions = Entry(LeftInsideRFRF,font=("arial",12,"bold"),bd=14,width=10,bg="powder blue",justify="right", textvariable=Deductions)
txtDeductions.grid(row=3,column=3)

#Right Side=============================
#PostCode
lblPostCode = Label(RightInsideLF,font=("arial",12,"bold"),text="Post Code",fg="Steel Blue",bd=10,anchor="w")
lblPostCode.grid(row=0,column=0)
txtPostCode = Entry(RightInsideLF,font=("arial",12,"bold"),bd=20,width=58,bg="powder blue",justify="right", textvariable=PostCode)
txtPostCode.grid(row=0,column=1)

#Gender
lblGender = Label(RightInsideLF,font=("arial",12,"bold"),text="Gender",fg="Steel Blue",bd=10,anchor="w")
lblGender.grid(row=1,column=0)
txtGender = Entry(RightInsideLF,font=("arial",12,"bold"),bd=20,width=58,bg="powder blue",justify="right", textvariable=Gender)
txtGender.grid(row=1,column=1)

#Right Inside==================================

#Pay Date
lblPayDate = Label(RightInsideLFLF,font=("arial",12,"bold"),text="Pay Date",fg="Steel Blue",bd=10,anchor="w")
lblPayDate.grid(row=0,column=0)
txtPayDate = Entry(RightInsideLFLF,font=("arial",12,"bold"),bd=10,width=36,bg="powder blue",justify="left", textvariable=PayDate)
txtPayDate.grid(row=0,column=1)

#Tax Period
lblTaxPeriod = Label(RightInsideLFLF,font=("arial",12,"bold"),text="Tax Period",fg="Steel Blue",bd=10,anchor="w")
lblTaxPeriod.grid(row=1,column=0)
txtTaxPeriod = Entry(RightInsideLFLF,font=("arial",12,"bold"),bd=10,width=36,bg="powder blue",justify="left", textvariable=TaxPeriod)
txtTaxPeriod.grid(row=1,column=1)

#NI Code
lblNICode = Label(RightInsideLFLF,font=("arial",12,"bold"),text="NI Code",fg="Steel Blue",bd=10,anchor="w")
lblNICode.grid(row=2,column=0)
txtNICode = Entry(RightInsideLFLF,font=("arial",12,"bold"),bd=10,width=36,bg="powder blue",justify="left", textvariable=NICode)
txtNICode.grid(row=2,column=1)

#Taxable Pay
lblTaxablePay = Label(RightInsideLFLF,font=("arial",12,"bold"),text="Taxable Pay",fg="Steel Blue",bd=10,anchor="w")
lblTaxablePay.grid(row=3,column=0)
txtTaxablePay = Entry(RightInsideLFLF,font=("arial",12,"bold"),bd=10,width=36,bg="powder blue",justify="left", textvariable=TaxablePay)
txtTaxablePay.grid(row=3,column=1)

#Pensionable Pay
lblPensionablePay = Label(RightInsideLFLF,font=("arial",12,"bold"),text="Pensionable Pay",fg="Steel Blue",bd=10,anchor="w")
lblPensionablePay.grid(row=4,column=0)
txtPensionablePay = Entry(RightInsideLFLF,font=("arial",12,"bold"),bd=10,width=36,bg="powder blue",justify="left", textvariable=PensionablePay)
txtPensionablePay.grid(row=4,column=1)

#Other Payments
lblOtherPayments = Label(RightInsideLFLF,font=("arial",12,"bold"),text="Other Payments",fg="Steel Blue",bd=10,anchor="w")
lblOtherPayments.grid(row=5,column=0)
txtOtherPayments = Entry(RightInsideLFLF,font=("arial",12,"bold"),bd=10,width=36,bg="powder blue",justify="left", textvariable= OtherPayments)
txtOtherPayments.grid(row=5,column=1)


#Right Hand Buttons=========================================
btnWagePayment=Button(RightInsideRFRF,pady=2,bd=8,fg="black",font=("arial",12,"bold"),width=14,text="Wage Payment",bg="Sky Blue").grid(row=0,column=0)

btnReset=Button(RightInsideRFRF,pady=2,bd=8,fg="black",font=("arial",12,"bold"),width=14,text="Reset System",bg="Sky Blue", command=reset).grid(row=1,column=0)

btnAdd=Button(RightInsideRFRF,pady=2,bd=8,fg="black",font=("arial",12,"bold"),width=14,text="Add",bg="Sky Blue").grid(row=2,column=0)

btnSave=Button(RightInsideRFRF,pady=2,bd=8,fg="black",font=("arial",12,"bold"),width=14,text="Save",bg="Sky Blue", command=save).grid(row=3,column=0)

btnDelete=Button(RightInsideRFRF,pady=2,bd=8,fg="black",font=("arial",12,"bold"),width=14,text="Delete",bg="Sky Blue").grid(row=4,column=0)

btnExit=Button(RightInsideRFRF,pady=2,bd=8,fg="black",font=("arial",12,"bold"),width=14,text="Exit",bg="Sky Blue", command=exit).grid(row=5,column=0)

#retrieve values for list box from db table===================

cursor = connection.cursor()
cursor.execute("SELECT EmployeeNo FROM EmployeeTBL")
result = cursor.fetchall()
for item in result:
    LstEmployeeNo.insert(END, item)
    LstEmployeeNo.bind("<<ListboxSelect>>",callback)


payroll.mainloop()

