import pyttsx3
import json
engine = pyttsx3.init()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
print("Hello")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


admNo = [2840, 7068, 2253, 7056, 2857, 2880]
bStu = ["Sherwin Richard Ranjith", "Edwin Benny",
        "Reghupathi A", "Vishal D", "Vinnuban", "Harish Siddartha"]
stuDetails = {
    "Sherwin Richard Ranjith": {
        "Adm No": 2840,
        "Class": 11,
        "Section": "B",
        "Roll No": 35,
        "Studying intensity": "Insane",
    },
    "Edwin Benny": {
        "Adm No": 7068,
        "Class": 11,
        "Section": "B",
        "Roll No": "E",
        "Studying intensity": "Pro",
    },
    "Reghupathi A": {
        "Adm No": 2253,
        "Class": 11,
        "Section": "B",
        "Roll No": "R",
        "Studying intensity": "Max",
    },
    "Vishal D": {
        "Adm No": 7056,
        "Class": 11,
        "Section": "B",
        "Roll No": 40,
        "Studying intensity": "Duper Nice",
    },
    "Vinnuban": {
        "Adm No": 2857,
        "Class": 11,
        "Section": "B",
        "Roll No": 39,
        "Studying intensity": "Pro max",
    },
    "Harish Siddartha": {
        "Adm No": 2880,
        "Class": 11,
        "Section": "B",
        "Roll No": 19,
        "Studying intensity": "Insane Pro",
    }
}


speak("This is custom Search By Team 12! Just type the numbers that are visible on screen.")

speak("You can type at 3.... 2.... 1.... GO! ")

print("Enter 1 to check bio of class 11-B Students")
print("Enter 2 for Bio of Class 11-B Teachers")
print("Enter 3 to exit.")


def run():
    while True:
        try:
            x = int(input("Enter the number: "))
            if x == 1:
                speak("You have selected Class 11-B Students")
                print("Enter the adm no of the student you want to check.")
                print("The Adm no of the students are: ", admNo)
                while True:
                    try:
                        y = int(input("Enter the adm no: "))
                        if y in admNo:
                            speak("The name of the student is: " +
                                  bStu[admNo.index(y)])
                            print("The name of the student is: " +
                                  bStu[admNo.index(y)])
                            details = json.dumps(
                                stuDetails[bStu[admNo.index(y)]])
                            print(details)
                            x = input("Do you want to exit? (y/n)")
                            if x == "y":
                                break
                        else:
                            print("The adm no you entered is not in the list.")
                            speak("The adm no you entered is not in the list.")
                    except ValueError:
                        print("Please enter a valid number.")
                        speak("Please enter a valid number.")

            elif x == 2:
                speak("You have selected Class 11-B Teachers")
                print("Enter the adm no of the teacher you want to check.")
                print("The Adm no of the teachers are: ", admNo)
                while True:
                    try:
                        y = int(input("Enter the adm no: "))
                        if y in admNo:
                            speak("The name of the teacher is: " +
                                  bStu[admNo.index(y)])
                            print("The name of the teacher is: " +
                                  bStu[admNo.index(y)])
                            exit = input("Do you want to exit? (y/n)")
                        else:
                            print("The adm no you entered is not in the list.")
                            speak("The adm no you entered is not in the list.")
                    except ValueError:
                        print("Please enter a valid number.")
                        speak("Please enter a valid number.")

            elif x == 3:
                break

            else:
                print("Please enter a valid number.")
                speak("Please enter a valid number.")

        except ValueError:
            print("Please enter a valid number.")
            speak("Please enter a valid number.")


run()
# val = int(input("Enter the number to search: "))

# if val == 1:
#     speak("you have selected to check the bio of class 11 students")

# if val == 2:
#     speak("you have selected to check the bio of class 11 B Teachers")

# if val == 1:
#     speak("Bio Of Class 11-B Students")
#     print("-----Bio of Class 11-B Students-----")

# if val == 1:
#     speak("Enter student's admin number")
#     name1 = int(input("Enter student's admission Number:"))

# if name1 == admNo[0]:
#     speak("Full name: Sherwin Richard Ranjith \n Age: 16")

#     speak("Do you Want to continue? If Yes Type 10 And If No Type 20")
#     fill = ("Enter the number: ")

# elif name1 == admNo[1]:
#     speak("Full name: Edwin Benny \n Age: 16")

#     speak("Do you Want to continue? If Yes Type 10 And If No Type 20")
#     fill = ("Enter the number: ")

# elif name1 == admNo[2]:
#     speak("Full name: Reghupathi A \n Age: 16")

#     speak("Do you Want to continue? If Yes Type 10 And If No Type 20")
#     fill = ("Enter the number: ")

# elif name1 == admNo[3]:
#     speak("Full name: Vishal D \n Age: 16")

#     speak("Do you Want to continue? If Yes Type 10 And If No Type 20")
#     fill = ("Enter the number: ")

# elif name1 == admNo[4]:
#     speak("Full name: Vinnuban \n Age: 16")

#     speak("Do you Want to continue? If Yes Type 10 And If No Type 20")
#     fill = ("Enter the number: ")

# elif name1 == admNo[5]:
#     speak("Full name: Harish Siddartha \n Age: 16")

#     speak("Do you Want to continue? If Yes Type 10 And If No Type 20")
#     fill = ("Enter the number: ")
