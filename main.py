import os
import Capture_Image
import Train_Image
import Recognize


#Main page
def title_bar():
    os.system('cls')

    # Project Name
    print("\t------Attendance using Face Recognition System------")


# Steps

def mainMenu():
    title_bar()
    print()
    print("[1] Student Registration")
    print("[2] Train Images")
    print("[3] Face Recognization & Take Attendance")
    print("[4] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                CaptureFaces()
                break
            elif choice == 2:
                Trainimages()
                break
            elif choice == 3:
                RecognizeFaces()
                break

                mainMenu()
            elif choice == 4:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-4")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-4\n Try Again")
    exit



# --------------------------------------------------------------
# calling the take image function form capture image.py file

def CaptureFaces():
    Capture_Image.takeImages()
    key = input("Enter any key to return back to main page:")
    mainMenu()


# -----------------------------------------------------------------
# calling the train images from train_images.py file

def Trainimages():
    Train_Image.train_images()
    key = input("Enter any key to return back to main page:")
    mainMenu()


# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file

def RecognizeFaces():
    Recognize.recognize_attendence()
    key = input("Enter any key to return back to main page:")
    mainMenu()


# ---------------main driver ------------------
mainMenu()
