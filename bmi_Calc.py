
weight=float(input("enter your weight :: "))
unit=input("enter the unit kg or lbs :: ")
height=float(input("enter your height in cm's :: "))
par=((height/100)**2)
par2=(height*0.394)**2
if ('kg' in unit):
    kgs=weight
    print("weight in kgs is ",kgs)
    bmi=kgs/par
    print("***** body mass index *****")
    print("        ",bmi)
    if(0<bmi<18.5):
        print("you are underweight")
    elif(18.5<bmi<25):
        print("you are normal weight and healthy")
    elif(25<bmi<=30):
        print("you are overweight,you need to work on weightloss")
    else:
        print("you are obese and need to loose weight to live longer")


elif('lbs'in unit):
    lbs=weight
    print("weight in lbs is ",lbs)
    bmi=(lbs/par2)*703
    print("***** body mass index *****")
    print("            ",bmi)
    if(0<bmi<18.5):
        print("you are underweight")
    elif(18.5<bmi<25):
        print("you are normal weight and healthy")
    elif(25<bmi<=30):
        print("you are overweight,you need to work on weightloss")
    else:
        print("you are obese and need to loose weight to live longer")
else:
    print("please mention correct unit")