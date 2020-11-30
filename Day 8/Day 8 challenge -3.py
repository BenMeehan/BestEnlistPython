try:
    # print(a)
    raise Exception("Another erro")
except NameError:
    print("Undefined variable! Name error")
except:
    print("Some other error")
