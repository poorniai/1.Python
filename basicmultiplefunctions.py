class multipleFunctions():
    def OddEven():
        num=int(input("Enter Number"))
        if(num%2==0):
            print("Event Event")
            message="Event Number"
        elif(num%2==1):
            print("Odd Number")
            message="Odd number"
        return message
        
    def BMI():
        BMI=int(input("Enter the BMI Index:"))
        if(BMI<18.5):
            print("Underweight")
            message="Underweight"
        elif(BMI<24.9):
            print("Normal")
            message="Normal"
        elif(BMI<29.9):
            print("OVerweight")
            message="Over weight"
        else:
            print("Very OVerweight")
            message="OVer weight"
        return message    
    