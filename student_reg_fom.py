
students = {}

owner_pass = "Owner@123"

while True:
    print("Welcome to Cyber Success")

    print('1 ) For new student Registration')
    print('2 ) Fess Submission')
    print('3 ) Owner Access')
    print('4 ) Exit')

    i = int(input("Enter your choice: "))

    if i == 1:
        print('Welcome to student registration: ')

        std_name = str(input('Enter a Name :'))
        std_f_name = str(input('Enter a Father Name :'))
        std_m_name = str(input('Enter a Mother Name :'))
        cell_no = str(input('Enter a Phone Number :'))
        std_email = input('Enter a Email :')
        uid = input("Enter unique id: ")

        while True:
            if uid in students:
                uid = input("Id already exists! please enter another id: ")
            else:
                students[uid] = {"name": std_name, "father_name": std_f_name, "Mother_name": std_m_name, "Phone_no": cell_no, "Email": std_email, "Fees": 0}
                print("Created student with id: ",uid)
                break
        print(' Registration is sucessfull')

    elif i == 2:

        uid = input("Enter unique id: ")
        if uid in students:
            fees = int(input(" Enter a Fess :"))
            if fees >= 1000:
                students[uid]["Fees"] = fees
            else:
                print("fess not accepted")
        else:
            print("Id not exists! please enter another id: ")
        print('Thank you for fees')

    elif i == 3:
        upass = input("Enter owner password: ")

        if upass == owner_pass:
            uid = input("Enter the id: ")

            print(students[uid])


    elif i == 4:
        print("Thank you! Bye!")
        break

    else:
        print("Please enter correct choice")
