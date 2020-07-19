"""B. Create a console application for an IT Academy with the
following features:
a) The academy program should have a fixed course of study.(frontend,python-django,php-laravel,Cloud Computing,Data Science)
b) If a new student is interested in the academy program the student can
inquiry about the course of study.(inquiry detail on asking)
c) Student Registration with Rs. 20000 (deposit). Students are allowed to
pay in two installments with Rs. 10000 each.(total costs=20000 at two installement rs10000)
d) Display all the student’s information from the academy with their payments(name subscibed course payments)
and remaining payments.(student information)
e) Update the student information if needed.
f) Delete the student information if he/she left the program.
g) Return the deposit amount (Rs. 20000) to the students after the
successful completion of the course and check the balance.
Remember it should be a full feature CONSOLE APP. You can store
the course of study and the student’s detail in your preferred file
format (.csv, .txt, etc).
Ignore the permissions for now. Anyone who runs the script is allowed to
access all the features. Develop the app with OOP Approach."""
import json
import os


def ITAcademy(path):
    """
    !!!!!!!!!!!! CONSOLE ITACADEMY !!!!!!!!!!!!!!!!!!!
    course_status number meaning
    1= 1st installement payed
    2= 2nd installement payed
    3= course completed
    if course completed teacher can update student profile 
    """
    if not os.path.exists(path):
        fa = open(
            path, 'w')
        content = {
            "courses": {
                "Python": "==========Python==========\nBegginer to Advance\n3 month course\nCourse Subscipition: Rs 20000",
                "PHP": "==========PHP==========\nBegginer to Advance\n3 month course\nCourse Subscipition: Rs 20000",
                "CloudComputing": "==========CloudComputing==========\nBegginer to Advance\n3 month course\nCourse Subscipition: Rs 20000",
                "DataScience": "==========DataScience==========\nBegginer to Advance\n3 month course\nCourse Subscipition: Rs 20000",
                "FrontEnd": "==========FrontEnd==========\nBegginer to Advance\n3 month course\nCourse Subscipition: Rs 20000"
            },
            "student": {
                "1": {
                    "name": "Prerit Bhandari",
                    "payment": 10000,
                    "returned": "",
                    "course": "Python",
                    "course_status": 2
                },
                "2": {
                    "name": "Will Smith",
                    "payment": 10000,
                    "returned": "",
                    "course": "DataScience",
                    "course_status": 1
                },
                "3": {
                    "name": "James Bond",
                    "payment": 10000,
                    "returned": "",
                    "course": "CloudComputing",
                    "course_status": 2
                }
            }
        }

        json.dump(content, fa, indent=4)
        fa.close()
    i = 1
    while (i != 0):
        print('================================ Welcome to IT Academy ================================')
        print(
            '1.Course Enquiry\n2.Student Payment related information\n3.Enrolled into course\n4.Update Student info\n5.Delete Student info\n6.Money Return on course completion\n0.Exit Application')
        num = input('Press any number above to continue: ')
        if num == '':
            num = 1
        num = int(num)
        if (num == 1):
            print('Course Enquiry')
            fo = open(
                path, 'r')
            file_info = json.load(fo).get('courses')
            print(file_info['Python'])
            print(file_info['PHP'])
            print(file_info['CloudComputing'])
            print(file_info['DataScience'])
            print(file_info['FrontEnd'])
            fo.close()
            print(
                '==========================================================================================')

            continue
        if (num == 2):
            print(
                '================================ Student Payment related information ================================')

            fo = open(
                path, 'r')
            std_id = input('please enter your student id: ')
            file_info = json.load(fo).get('student')
            if std_id in list(file_info.keys()):
                std_info = file_info.get(std_id)
                print(
                    f'Student Name:{std_info["name"]}\nCourse Enrolled: {std_info["course"]}\nPayment Made: Rs {std_info["payment"]}')
            else:
                print("you are not enrolled")
                fo.close()
            print(
                '==========================================================================================')
            continue
        elif (num == 3):
            print('================================ Enroll into course information ================================')
            course = {"1": "Python", "2": "PHP", "3": "CloudComputing",
                      "4": "DataScience", "5": "FrontEnd"}
            for i, j in course.items():
                print(i, ".", j)
            course_num = input('Enter above course you want to register: ')
            print(course.get(course_num))
            if course.get(course_num):
                fo = open(
                    path, 'r')

                file = json.load(fo)
                # print(file)
                std_file = file['student']

                name = input('please enter your name')
                std_amt = int(input(
                    'Pay the amount 20000 in two installement\nyou can pay 1st installment 10000:'))
                if std_amt == 10000 or std_amt == 20000:
                    new_id = max([int(i) for i in std_file.keys()])
                    print(new_id)
                    new_id = new_id + 1
                    std_file[str(new_id)] = {"name": name,
                                             "payment": std_amt,
                                             "returned": 0,
                                             "course": course.get(course_num),
                                             "course_status": [1 if std_amt == 10000 else 2][0]}
                    print(std_file)
                    file['student'] = std_file
                    fa = open(
                        path, 'w')
                    json.dump(file, fa, indent=4)
                    fa.close()
                    fo.close()
                    print(
                        '==========================================================================================')
                    continue
                else:
                    print(
                        'please pay and move forward!!!\n Payment must not greater than 20000')
                    print(
                        '==========================================================================================')
                    continue
        elif (num == 4):
            print(
                '================================ Update Student information ================================')

            fo = open(
                path, 'r')
            file = json.load(fo)
            file_info = file.get('student')
            print('All student_id', list(file_info.keys()))
            std_id = input('please enter your student id: ')

            if std_id in list(file_info.keys()):
                std_info = file_info.get(std_id)
                print(
                    f'Student Name:{std_info["name"]}\nCourse Enrolled: {std_info["course"]}\nPayment Made: Rs {std_info["payment"]}')
                print('please enter change: you want to made otherwise leave it blank:')
                name = input('please enter name: ')
                payment = input('please enter payment: ')
                course = input('please enter course: ')
                returned = input('please enter returned: ')
                course_status = input('please enter course_status: ')
                std_info["name"] = [name if bool(
                    name) else std_info["name"]][0]
                std_info["payment"] = [int(payment) if bool(
                    payment) else std_info["payment"]][0]
                std_info["course"] = [course if bool(
                    course) else std_info["course"]][0]
                std_info["returned"] = [returned if bool(
                    returned) else std_info["returned"]][0]
                prev_status = std_info["course_status"]
                std_info["course_status"] = [int(course_status) if bool(course_status) else std_info["course_status"]][
                    0]
                std_info["course_status"] = [std_info["course_status"] if (
                    3 >= std_info["course_status"] >= 1) else prev_status][0]

                print(std_info)

                file_info[std_id] = std_info
                file['student'] = file_info
                print(file)
                fa = open(
                    path, 'w')
                json.dump(file, fa, indent=4)
                fo.close()
                fa.close()
                print(
                    '==========================================================================================')
                continue
            else:
                print(
                    'Please enter correct student id!!!')
                print(
                    '==========================================================================================')
                continue
        elif (num == 5):
            print(
                '================================ Delete Student information ================================')

            fo = open(
                path, 'r')
            file = json.load(fo)
            file_info = file.get('student')
            print('All student_id', list(file_info.keys()))
            std_id = input('please enter your student id: ')

            if std_id in list(file_info.keys()):
                if file_info[std_id]['payment'] == 20000:
                    file_info.pop(std_id)

                    print(file_info)

                    file['student'] = file_info
                    print(file)
                    fa = open(
                        path, 'w')
                    json.dump(file, fa, indent=4)
                    fo.close()
                    fa.close()
                    print(
                        '==========================================================================================')
                    continue
                else:
                    print('this student haven\'t paid complete amount')
                    print(
                        '==========================================================================================')
                    continue
            else:
                print(
                    'Please enter correct student id!!!')
                print(
                    '==========================================================================================')
                continue
        elif (num == 6):
            print(
                '================================ Reward on completion information ================================')

            fo = open(
                path, 'r')
            file = json.load(fo)
            file_info = file.get('student')
            print('All student_id', list(file_info.keys()))
            std_id = input('please enter your student id: ')

            if std_id in list(file_info.keys()):
                if file_info[std_id]['course_status'] == 3:
                    file_info[std_id]['returned'] = '20000'
                    print(
                        "****************** Great you complete the course ************")
                    print(
                        "****************** Your amount has returned. Please check in student info ************")
                    print("****************** Best of luck for future ************")
                    print(file_info)

                    file['student'] = file_info
                    print(file)
                    fa = open(
                        path, 'w')
                    json.dump(file, fa, indent=4)
                    fo.close()
                    fa.close()
                    print(
                        '==========================================================================================')
                    continue
                else:
                    print('this student haven\'t paid complete amount')
                    print(
                        '==========================================================================================')
                    continue
            else:
                print(
                    '==========================================================================================')
                print(
                    'Please enter correct student id!!!')
                print(
                    '==========================================================================================')
                continue
        elif (num == 0):
            i = num
            print('Thank u for using our service')
            print(
                '==========================================================================================')
            return


if __name__ == "__main__":
    path = os.path.join(os.getcwd(), 'database.json')
    print('Your database is create on following location: ', path)
    ITAcademy(path)
