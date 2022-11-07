#   Jeffrey Woosley
#   CIS261
#   Project Phase 2
def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname

# Get Employee's Start Date and End Date   
def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter End Date (mm/dd/yyyy): ")
    return fromdate, todate

# Get Total Hours Worked By an Employee
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked: '))
    return hours

# Get Hourly Rate of an Employee
def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

# Get Employee's Tax Rate
def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate

# Calculate Tax and Net Pay 
def CalcTaxAndNetPay(hours,hourlyrate,taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

# Print Employee Details
def printinfo(EmpDetailList):
    
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    
    for EmpList in EmpDetailList:
        
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}",f"{grosspay:,.2f}",f"{taxrate:,.1%}",f"{incometax:,.2f}",f"{netpay:,.2f}")
        
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        
    EmpTotals["TotEmp"] = TotEmployees
    EmpTotals["TotHrs"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay


# Print Total Employee Information
def PrintTotals(EmpTotals):
    
    print()
    print(f"Total Number of Employees: {EmpTotals['TotEmp']}")
    print(f"Total Hours Worked: {EmpTotals['TotHrs']}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total Income Tax: {EmpTotals['TotTax']:,.2f}")
    print(f"Total Net Pay: {EmpTotals['TotNetPay']:,.2f}")





if __name__ == "__main__":
    #create empty list and dictionary
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        print()
    
        # append information to the file
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
    
    print()
    print()
    fromdate = GetDatesWorked()
  
    
    print()
    printinfo(EmpDetailList)
    
    print()
    PrintTotals(EmpTotals)



