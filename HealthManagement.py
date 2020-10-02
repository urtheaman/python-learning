print("Hi, Your Health Management System Is Here")
name = (input("Enter Your Name : ")).lower()
usr_name_food = "food_" + name + ".txt"
usr_name_exr = "exr_" + name + ".txt"

def getdate():
    import datetime
    return datetime.datetime.now()

while True:
    print("What Do You Want To Do ?\n1.Press 1 For Logging\n2.Press 2 for Retrieving\n")
    task = int(input("Enter Your Input : "))
    if task == 1:
        print("Started To Log Values...")
    elif task == 2:
        print("Started To Retrieve Values...")
    else:
        print("You Have Selected The wrong Input! Please Choose Right Input!\n")
        continue
    print("Select One Of These -\n1.Press 1 For Food\n2.Press 2 for Exercise\n")
    fun = int(input("Enter Your Input : "))
    if fun == 1 and task == 1:
        print("which food have you taken now ?")
        taken_food = input("Enter What You Ate : ")
        food = f"Time : [{str(getdate())}]  Food : {taken_food}\n"
        with open(usr_name_food, "a") as fd:
            fd.write(food)
        print("Successfully Added!\n")
    elif fun == 1 and task == 2:
        try:
            with open(usr_name_food) as fd:
                print(fd.read())
        except Exception as e:
            print(e)
    elif fun == 2 and task == 1:
        done_exercise = input("Enter Which Exercise You Performed : ")
        exercise = f"Time : [{str(getdate())}]  Exercise : {done_exercise}\n"
        with open(usr_name_exr, "a") as ex:
            ex.write(exercise)
        print("Successfully Added!\n")
    elif fun == 2 and task == 2:
        try:
            with open(usr_name_exr) as ex:
                print(ex.read())
        except Exception as e:
            print(e)
    else:
        print("You Have Selected The wrong Input! Please Choose Right Input!\n")


