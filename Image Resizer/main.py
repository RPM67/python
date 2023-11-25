import time
import cv2
from roboSpeaker import commandSpeaker
print("Welcome to image resizer software by RPM")
commandSpeaker("Welcome to image resizer software by RPM")

def image_resizer():
    commandSpeaker("Enter the file name or file location of the image which you want to resize below")
    src = input("Enter the location of image or name of image which you want to resize : ")

    def scale_percent_input():
        try:
            commandSpeaker("Enter the scale of image to which you wanna resize the image below")
            scale_percent = int(input("Enter the new scale of image : "))
            if scale_percent<0:
                raise ValueError
            return scale_percent
        except ValueError:
            commandSpeaker("oops, Invalid value entered, please try again")
            print("Invalid Input. Please enter a valid value of  scale to resize the image correctly")
            return scale_percent_input()

    def format_input():
        commandSpeaker("enter the format in which you want your image like jpg, png, etc")
        formats = input("Enter the format in which you want to save the file(jpg/png/jpeg) : ").lower()
        if formats == 'jpg' or formats == 'png' or formats == 'jpeg':
            return formats
        else:
            commandSpeaker("oops, Invalid format entered, please try again")
            print("Invalid format. please try again")
            return format_input()

    try:
        image = cv2.imread(src, cv2.IMREAD_UNCHANGED)
        if image is None:
            raise FileNotFoundError


        # cv2.imshow('photo', image)
        # the first argument 'photo' will be title of image displayed in output of program

        # cv2.waitKey(0)
        # as soon as the image gets opened by cv2.imshow() fun., the program will terminate. so we will use cv2.waitKey() function, which will hold the program and keep program running until any button from keyboard is pressed by user which will make program end. due to this in output the image will keep displayed.

        destination = f'resized-image.{format_input()}'

        scale_percents = scale_percent_input()
        new_height = int(image.shape[0] * (scale_percents / 100))  # shape[0] represents height of image
        new_width = int(image.shape[1] * (scale_percents / 100))  # shape[1] represents width of image

        output = cv2.resize(image, (new_height, new_width))  # output variable will store the resized image given by cv2.resize() function. cv2.resize() function will assign the new height and width to the image

        cv2.imwrite(destination, output)  # cv2.write() function will write or store the resize image stored in output to destination which contains the new file name in which we want to store image
        print("Resizing image to given scale.......")
        commandSpeaker("resizing your image")
        time.sleep(2)
        print(f"Image Resized Successfully. The resized image has been saved with name '{destination}'. please check your image.")
        commandSpeaker(f"image resized successfully. your image has been saved with name {destination}")
        time.sleep(2)
        commandSpeaker("Thank you for using our service. Please come again")
        print("Thank you for using our service. Please come again")

    except FileNotFoundError:
        commandSpeaker("sorry, file not found at given destination. please try again")
        print("wrong file destination or file name. check file path or file name and try again\n")
        image_resizer()
    except cv2.error as e:
        commandSpeaker("oops, some error occurred in input image. please check your input image")
        print(f"OpenCV error: {e}. Please check the input image.")
    except Exception as e:
        commandSpeaker("Some unwanted error occurred. please try again")
        print(f"Some unwanted error occurred as {e}. please try again")



image_resizer()
# modified_image = cv2.imread(destination, cv2.IMREAD_UNCHANGED)
# cv2.imshow('title', modified_image)
# cv2.waitKey(0)
