print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    
def calculate_BMI ():
    height = float(input("Input height in meters : "))
    weight = float(input("Input weight in kg: "))
    print ("Height = " + str(height))
    print ("Weight = " + str(weight) )
    BMI = weight/ height **2
    return BMI
def check_bmi(bmi_value):
    if bmi_value<18.5:
        print ("you are underweight")\
        
    elif bmi_value >18.5 or bmi_value < 25.0:
        print ("you are moderate weight")

    else :
        print ("you are overweight")
        


def main():
    bmi_value = calculate_BMI()
    print ("calculated BMI Value is : " +str(bmi_value))
    check_bmi(bmi_value)
    

if __name__ == "__main__":
    main()