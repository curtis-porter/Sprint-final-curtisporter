#Comment like a pro
#Authour:curtis porter
#date:dec17,2021

import datetime
f = open("OSICDef.dat", "r")
Policynumber = int(f.readline())
Base = float(f.readline())
Cardis = float(f.readline())
liabilty = float(f.readline())
Glassrate = float(f.readline())
Loanrate = float(f.readline())
Hstrate = float(f.readline())
Processfee = float(f.readline())
f.close()

#inputs
Custfirstname = input("EnterCustomer first name:")
Custlastname = input("Enter Customer last name:")
CustAddress = input("Enter Customer address:")
Custcity = input("Enter cutomer city")
CustProvince = input("Enter Province:")
Custpostal = input("Enter postal code:")
CustPhonenum = input("Enter Phonenumber:")
Carnumber = int(input("Enter number of cars being insured"))
Carliability = input("Liability fo car up to 1,000,000 Y/N")
Glasscov = input("glass coverage?Y/N")
Loancov = input("loan coverage?Y/N")
Payment = input("monthly or full payment?F/M")

Custfirstname = Custfirstname.title()
Custlastname = Custlastname.title()
CustAddress = CustAddress.title()
Custcity = Custcity.title()
CustProvince = CustProvince.upper()
Custpostal = Custpostal.upper()
Carliability = Carliability.upper()
Glasscov = Glasscov.upper()
Loancov = Loancov.upper()
Payment = Payment.upper()

#prosess

if Carnumber == 1:
    totalcost = Base
else:
    totalcost = ((Base * Cardis) + Base) * Carnumber

if Carliability == "Y":
    totalcost = totalcost + liabilty

if Glasscov == "Y":
   totalcost = totalcost + Glassrate

if Loancov == "Y":
    totalcost = totalcost + Loanrate

#values
Taxammount = totalcost * Hstrate
totalwithtax = totalcost + Taxammount
totalextras = liabilty + Glassrate + Loanrate

#Recipt
print()
print("One Stop Insurance Company")
print()
print("Customer info:")
print("Policy Number:",                  (Policynumber))
print("Customer First Name:",            (Custfirstname))
print("Customer Last  Name:",            (Custlastname))
print("Customer PhoneNumber:",           (CustPhonenum))
print("Customer Address:",               (CustAddress))
print("City:",                           (Custcity))
print("Province:",                       (CustProvince))
print("Postal:",                         (Custpostal))
print()
print("purchase info:")
print("Number of cars:",                        (Carnumber))
if Carliability == "Y":
    print("Liability fee:",                      (Carliability))
else:
    print("Liability fee:                                     N/A")
if Glasscov == "Y":
    print("Glass coverage:",                            (Glassrate))
else:
    print("Glass coverage:                                    N/A")
if Loancov == "Y":
  print("Loaner coverage:",                             (Loanrate))
else:
    print("Loaner coverage                                     N/A")
print("Extra charges",                                  (totalextras))
print()
print("Purchase info:")
print("Policy fee:",                                     (Base))
print("Tax fee:",                                        (totalwithtax))
print("Total Cost:",                                     (totalcost))
print()



#update policy file
Policynumber += 1

f = open("Polices.dat","a")
f.write("{}{}{},".format(Policynumber,Custfirstname,Custlastname))
f.write("{}{},".format(Custfirstname,Custlastname))
f.write("{},".format(CustAddress))
f.write("{},".format(Custcity))
f.write("{},".format(CustProvince))
f.write("{},".format(Custpostal))
f.write("{},".format(CustPhonenum))
f.write("{},".format(Loancov))
f.write("{},".format(totalextras))
f.write("{},".format(totalcost))
f.write("{}\n" .format(totalwithtax))

#OSICdef.dat update
f = open("OSICDef.dat","a")
f.write("{}\n".format(str(Policynumber)
f.write("{}\n".format(str(Base)
f.write("{}\n".format(str(Carnumber)
f.write("{}\n".format(str(totalextras)
f.write("{}\n".format(str(Glassrate)
f.write("{}\n".format(str(Loanrate)
f.write("{}\n".format(str(Hstrate)
f.write("{}\n".format(str(Processfee)
f.close()

#Report 1
print("ONE STOP INSURANCE COMPANY")
print("POLICY LISTING AS OF ", (curDate.strftime(%m%d%y))
print("POLICY    CUSTOMER       INSURANCE      EXTRA      TOTAL")
print("NUMBER      NAME          PREMIUM       COST      PREMIUM")
print("===========================================================")

policyCtr = 0
Base = 0
totalextras = 0
totalwithtax = 0


f = open("polices.dat". "r")

for  policyDatLine in f:
     policyDat = policyDatline.split(",")
     reportPolicyNumber = policyDat[0].strip()
     reportCustName = policyDat[1].strip()
     reportBase =  policydat[13].strip()
     reporttotalextras = policydat[12].strip()
     reporttotalwithtax = policydat[13].strip()


     print({reportPolicyNum:<7}        {reportCustName:<15}     {reportBase:<7}    {report:<7}     {reporttotalwithtax}   )



    policyCtr +=1
    f.close()
    print("Total Policies: {policyCtr}")
    print()