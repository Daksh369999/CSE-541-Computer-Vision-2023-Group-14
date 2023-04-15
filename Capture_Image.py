import csv
import cv2
import os
import os.path


# Check if the given string is a number
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(string)
        return True
    except (TypeError, ValueError):
        pass

    return False


# Take image function
def takeImages():
    # Ask for user input
    user_id = input("Enter Your Id: ")
    user_name = input("Enter Your Name: ")

    # Check if the user input is valid
    if is_number(user_id) and user_name.isalpha():
        # Initialize camera
        cam = cv2.VideoCapture(0)
        harcascade_path = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascade_path)
        sample_num = 0

        while True:
            # Read the camera frame
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                # Increment sample number
                sample_num += 1
                # Save the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep + user_name + "." + user_id + '.' +
                            str(sample_num) + ".jpg", gray[y:y+h, x:x+w])
                # Display the frame
                cv2.imshow('frame', img)
            # Wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # Break if the sample number is more than 100
            elif sample_num > 150:
                break
        cam.release()
        cv2.destroyAllWindows()
        print("Images Saved for ID : " + user_id + " Name : " + user_name)
        header = ["Id", "Name"]
        row = [user_id, user_name]
        # Check if the csv file exists
        if os.path.isfile("StudentDetails"+os.sep+"StudentDetails.csv"):
            with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(j for j in row)
            csv_file.close()
        else:
            with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(i for i in header)
                writer.writerow(j for j in row)
            csv_file.close()
    else:
        if is_number(user_id):
            print("Enter Alphabetical Name")
        if user_name.isalpha():
            print("Enter Numeric ID")