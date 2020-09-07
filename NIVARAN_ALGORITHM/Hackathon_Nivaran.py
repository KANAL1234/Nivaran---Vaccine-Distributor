#NIVARAN
#For the below algorithm we are theorising some aspects 
#1)For now we are taking 10 areas namely 1,2,3,4,5,6,7,8,9,10 but later when appropiraite government data is available these can correspond to real life locations
#2)For now we are taking areas 2,3,7,9 as red zones with a high number of covid patients.
#3)For now let there be 3 main covid vaccination centers
#4)For now we are letting Center1 serve areas 1,2,3 ; Center2 serve areas 4,5,6,7 ; Center3 serve areas 8,9,10
#5)For now we are taking two income categories APL and BPL 
import random
import sqlite3

#taking user input
def nivaran():
    conn = sqlite3.connect('nivaran.db')
    c = conn.cursor()
    Name = input('Input Your Name- ')
    Age = int(input('Input Your Age- '))
    MedicalHistory = input('Do You Have A Comorbidity(Chronic Illness/Health Risk)? If Yes then enter y if No then enter n- ')
    IncomeStrata = input('Do You Lie Below The Poverty Line And Have a BPL card? If Yes then enter y if No then enter n- ')
    AadharNo = int(input('Input Your Aadhar Number- '))
    PhoneNo = int(input('Input Your Phone Number- '))
    AreaCode = int(input('Input Area Code based on the area you live in.(enter a value from 1-10)- '))
    RandomID = random.randint(100000000000,999999999999)
    VariableP1 = "empty"
    VariableP2 = "empty"

    #level 1 priority selection 

    if Age <= 18:
        VariableP1 = "Medium Risk";
    elif 18<=Age<=60:
        VariableP1 = "Low Risk";
    elif Age >=60:
        VariableP1 = "High Risk";

    #level 2 priority selection

    if MedicalHistory == "y" and VariableP1 == "High Risk" :
        VariableP1 = "High Risk";
    elif MedicalHistory == "y" and VariableP1 == "Medium Risk" :
        VariableP1 = "High Risk";
    elif MedicalHistory == "y" and VariableP1 == "Low Risk" :
        VariableP1 = "Medium Risk";
    #Area Allocation and priority         
    if AreaCode == 2 :
        VariableP2 = "Center-1 High Priority";
    elif AreaCode == 3 :
        VariableP2 = "Center-1 High Priority";
    elif AreaCode == 7 :
        VariableP2 = "Center-2 High Priority";
    elif AreaCode == 9 :
        VariableP2 = "Center-3 High Priority";
    elif AreaCode == 1 :
        VariableP2 = "Center-1 Low Priority";
    elif AreaCode == 4 :
        VariableP2 = "Center-2 Low Priority";
    elif AreaCode == 5 :
        VariableP2 = "Center-2 Low Priority";
    elif AreaCode == 6 :
        VariableP2 = "Center-2 Low Priority";
    elif AreaCode == 8 :
        VariableP2 = "Center-3 Low Priority";
    elif AreaCode == 10 :
        VariableP2 = "Center-3 Low Priority";

    #level 3 priority selection

    if IncomeStrata == "y" and VariableP1 == "High Risk" :
        VariableP1 = "High Risk";
    elif IncomeStrata == "y" and VariableP1 == "Medium Risk" :
        VariableP1 = "High Risk";
    elif IncomeStrata == "y" and VariableP1 == "Low Risk" :
        VariableP1 = "Medium Risk";
    c.execute("""CREATE TABLE IF NOT EXISTS nivaran(
                ID integer primary key,
                Name text not null,
                Age integer(3) not null,
                MedicalHistory text(1) not null,
                IncomeStrata text(1) not null,
                AadharNo integer(12) not null unique,
                PhoneNo integer(10) not null,
                AreaCode intger(1) not null,
                Risk text,
                Priority text
                )""")
    #c.execute("DELETE FROM nivaran")
    c.execute("INSERT INTO nivaran VALUES(?,?,?,?,?,?,?,?,?,?)",(RandomID,Name,Age,MedicalHistory,IncomeStrata,AadharNo,PhoneNo,AreaCode,VariableP1,VariableP2))
    print("\n","High Risk, High Priority")
    c.execute("""SELECT * FROM nivaran where Risk = "High Risk" and Priority like "%High Priority" """)
    print("\n",c.fetchall(),"\n")
    print("\n","High Risk, Low Priority")
    c.execute("""SELECT * FROM nivaran where Risk = "High Risk" and Priority like "%Low Priority" """)
    print("\n",c.fetchall(),"\n")
    print("\n","Medium Risk, High Priority")
    c.execute("""SELECT * FROM nivaran where Risk = "Medium Risk" and Priority like "%High Priority" """)
    print("\n",c.fetchall(),"\n")
    print("\n","Medium Risk, Low Priority")
    c.execute("""SELECT * FROM nivaran where Risk = "Medium Risk" and Priority like "%Low Priority" """)
    print("\n",c.fetchall(),"\n")
    print("\n","Low Risk, High Priority")
    c.execute("""SELECT * FROM nivaran where Risk = "Low Risk" and Priority like "%High Priority" """)
    print("\n",c.fetchall(),"\n")
    print("\n","Low Risk, Low Priority")
    c.execute("""SELECT * FROM nivaran where Risk = "Low Risk" and Priority like "%Low Priority" """)
    print("\n",c.fetchall(),"\n")
    print("\n")
    conn.commit()
    conn.close()

for i in range (5):
    nivaran()



