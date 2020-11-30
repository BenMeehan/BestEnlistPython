try:
    inp = input("Enter some text : ")
    raise Exception()
except:
    print("From except block")
    print("The string you entered : "+inp)
finally:
    print("The finally block")
