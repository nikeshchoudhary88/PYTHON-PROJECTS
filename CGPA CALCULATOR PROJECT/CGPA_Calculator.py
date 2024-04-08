import time

def credit(m : float) ->int:
    if m >= 90:
        return 10
    elif m >= 80:
        return 9
    elif m >= 70:
        return 8
    elif m >= 60:
        return 7
    elif m >= 50:
        return 6
    elif m >= 40:
        return 5
    elif m >= 30:
        return 4
    elif m >= 20:
        return 3
    elif m >= 10:
        return 2
    elif m > 0:
        return 1
def sgpa(c : list,m : list) ->float:
    n1 = 0.0
    for i in range(len(c)):
        n1 += (c[i] * m[i])
    d = sum(c)
    return n1 / d

while 1:
    a = int(input("Enter the semester till which you want to calculate the CGPA="))

    r = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

    for n in range(1, a+1):
        print("Semester=", n)
        if n == 1:
            c = [4,4,3,3,3,1,1,1]
            m = [0,0,0,0,0,0,0,0]

            m[0] = float(input("Enter the marks of 18MAT11="))
            m[1] = float(input("Enter the marks of 18CHE12="))
            m[2] = float(input("Enter the marks of 18CPS13="))
            m[3] = float(input("Enter the marks of 18ELN14="))
            m[4] = float(input("Enter the marks of 18ME15="))
            m[5] = float(input("Enter the marks of 18CHEL16="))
            m[6] = float(input("Enter the marks of 18CPL17="))
            m[7] = float(input("Enter the marks of 18EGH18="))            
            
            for i in range(len(m)):
                m[i] = credit(m[i])

            r[0]= sgpa(c,m)
            print("")
            print("SGPA for First Semester = ", r[0])
        if n == 2:
            c = [4,4,3,3,3,1,1,1]
            m = [0,0,0,0,0,0,0,0]

            m[0] = float(input("Enter the marks of 18MAT21="))
            m[1] = float(input("Enter the marks of 18PHY22="))
            m[2] = float(input("Enter the marks of 18ELE23="))
            m[3] = float(input("Enter the marks of 18CIV24="))
            m[4] = float(input("Enter the marks of 18EGDL25="))
            m[5] = float(input("Enter the marks of 18PHYL26="))
            m[6] = float(input("Enter the marks of 18ELEL27="))
            m[7] = float(input("Enter the marks of 18EGH28="))            
            
            for i in range(len(m)):
                m[i] = credit(m[i])

            r[1]= sgpa(c,m)
            print("")
            print("SGPA for Second Semester=", r[1])
        if n == 3:
            c = [3,4,3,3,3,3,2,2,1]
            m = [0,0,0,0,0,0,0,0,0]

            m[0] = float(input("Enter the marks of 18MAT31="))
            m[1] = float(input("Enter the marks of 18EC32="))
            m[2] = float(input("Enter the marks of 18EC33="))
            m[3] = float(input("Enter the marks of 18EC34="))
            m[4] = float(input("Enter the marks of 18EC35="))
            m[5] = float(input("Enter the marks of 18EC36="))
            m[6] = float(input("Enter the marks of 18ECL37="))
            m[7] = float(input("Enter the marks of 18ECL38="))
            m[8] = float(input("Enter the marks of 18KAK39="))    
            
            for i in range(len(m)):
                m[i] = credit(m[i])

            r[2]= sgpa(c,m)
            print("")
            print("SGPA for Third Semester=", r[2])
        if n == 4:
            c = [3,4,3,3,3,3,2,2,1]
            m = [0,0,0,0,0,0,0,0,0]

            m[0] = float(input("Enter the marks of 18MAT41="))
            m[1] = float(input("Enter the marks of 18EC42="))
            m[2] = float(input("Enter the marks of 18EC43="))
            m[3] = float(input("Enter the marks of 18EC44="))
            m[4] = float(input("Enter the marks of 18EC45="))
            m[5] = float(input("Enter the marks of 18EC46="))
            m[6] = float(input("Enter the marks of 18ECL47="))
            m[7] = float(input("Enter the marks of 18ECL48="))
            m[8] = float(input("Enter the marks of 18CPC49="))           
            
            for i in range(len(m)):
                m[i] = credit(m[i])

            r[3]= sgpa(c,m)
            print("")
            print("CGPA for Fourth Semester=", r[3])
        if n == 5:
            c = [3,4,4,3,3,3,2,2,1]
            m = [0,0,0,0,0,0,0,0,0]

            m[0] = float(input("Enter the marks of 18ES51="))
            m[1] = float(input("Enter the marks of 18EC52="))
            m[2] = float(input("Enter the marks of 18EC53="))
            m[3] = float(input("Enter the marks of 18EC54="))
            m[4] = float(input("Enter the marks of 18EC55="))
            m[5] = float(input("Enter the marks of 18EC56="))
            m[6] = float(input("Enter the marks of 18ECL57="))
            m[7] = float(input("Enter the marks of 18ECL58="))
            m[8] = float(input("Enter the marks of 18CIV59="))          
            
            for i in range(len(m)):
                m[i] = credit(m[i])

            r[4]= sgpa(c,m)
            print("")
            print("SGPA for Fifth Semester=", r[4])
        if n == 6:
            c = [4,4,4,3,3,2,2,2]
            m = [0,0,0,0,0,0,0,0]

            m[0] = float(input("Enter the marks of 18EC61="))
            m[1] = float(input("Enter the marks of 18EC62="))
            m[2] = float(input("Enter the marks of 18EC63="))
            m[3] = float(input("Enter the marks of 18EC646="))
            m[4] = float(input("Enter the marks of 18XX65X="))
            m[5] = float(input("Enter the marks of 18ECL66="))
            m[6] = float(input("Enter the marks of 18ECL67="))
            m[7] = float(input("Enter the marks of 18ECMP68="))           
            
            for i in range(len(m)):
                m[i] = credit(m[i])

            r[5]= sgpa(c,m)
            print("")
            print("SGPA for Sixth Semester=", r[5])
        if n == 7:
            c = [3,3,3,3,3,2,2,1]
            m = [0,0,0,0,0,0,0,0]

            m[0] = float(input("Enter the marks of 18EC71="))
            m[1] = float(input("Enter the marks of 18EC72="))
            m[2] = float(input("Enter the marks of 18EC733="))
            m[3] = float(input("Enter the marks of 18EC741="))
            m[4] = float(input("Enter the marks of 18XX75X="))
            m[5] = float(input("Enter the marks of 18ECL76="))
            m[6] = float(input("Enter the marks of 18ECL77="))
            m[7] = float(input("Enter the marks of 18ECP78="))          
            
            for i in range(len(m)):
                m[i] = credit(m[i])

            r[6]= sgpa(c,m)
            print("")
            print("SGPA for Seventh Semester=", r[6])
        if n == 8:
            c = [3,3,8,1,3]
            m = [0,0,0,0,0]

            m[0] = float(input("Enter the marks of 18EC81="))
            m[1] = float(input("Enter the marks of 18XX82X="))
            m[2] = float(input("Enter the marks of 18ECP83="))
            m[3] = float(input("Enter the marks of 18ECS84="))
            m[4] = float(input("Enter the marks of 18ECI85="))       
            
            for i in range(len(m)):
                m[i] = credit(m[i])

            r[7]= sgpa(c,m)
            print("")
            print("SGPA for Eighth Semester=", r[7])
        print("")
        time.sleep(1)
    result: float = sum(r)/a
    print("CGPA = ", result)
    print("")
    time.sleep(1)
