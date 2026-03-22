class GenericFunctionsClass():
    
        def Subfields():
            message = "Sub-fields in AI are: \n" + "Machine Learning \n" + "Neural Networks \n"+ "Vision \n"+ "Robotics \n" + "Speech Processing \n" + "Natural Language Processing"
            print(message)
            return message

        def OddEven():
            num = int(input("Enter a number:"))
            if(num%2==0):
                message = str(num)+" is Even number"
                print( message)
            else:
                message = str(num)+" is Odd number"
                print( message)
            return message
            
        def Eligible():
            gender=input("Your Gender:")
            age=int(input("Your Age:"))
            if (gender=='Male' and age<21):
                message = 'NOT ELIGIBLE'
                print(message)
            elif (gender=='Female' and age<18):
                message = 'NOT ELIGIBLE'
                print(message)
            else:
                message = "Eligible"
                print(message)
            return message

        def percentage():
            subject1=int(input("Subject1="))
            subject2=int(input("Subject2="))
            subject3=int(input("Subject3="))
            subject4=int(input("Subject4="))
            subject5=int(input("Subject5="))
            total = subject1+subject2+subject3+subject4+subject5
            print("Total :",total)
            percent = total/5
            print(f"Percentage : {percent:.14f}")
            return percent

        def triangle():
            height=int(input("Height:"))
            breadth=int(input("Breadth:"))
            print("Area formula: (Height*Breadth)/2")
            area= (height*breadth)/2
            print("Area of Triangle:", area)
            height1=int(input("Height1:"))
            height2=int(input("Height2:"))
            breadth1=int(input("Breadth:"))
            perimeter=height1+height2+breadth1
            print("Perimeter formula: Height1 + Height2 + Breadth")
            print("Perimeter of Triangle:" + str(perimeter))
            return perimeter
      