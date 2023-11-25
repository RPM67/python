import time
import cv2

print("Welcome to image resizer software by RPM")


def get_valid_scale_percent():
    while True:
        try:
            scale_percent = int(input("Enter the new scale of the image (, 50 for 50%): "))
            if 1 <= scale_percent <= 100:
                return scale_percent
            else:
                print("Invalid input. Please enter a value between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_valid_format():
    while True:
        formats = input("Enter the format in which you want to save the file (jpg/png/jpeg): ").lower()
        if formats in ['jpg', 'png', 'jpeg']:
            return formats
        else:
            print("Invalid format. Please try again.")


def image_resizer():
    src = input("Enter the location of the image you want to resize: ")

    try:
        image = cv2.imread(src, cv2.IMREAD_UNCHANGED)
        if image is None:
            raise FileNotFoundError

        scale_percent = get_valid_scale_percent()
        new_height = int(image.shape[0] * (scale_percent / 100))
        new_width = int(image.shape[1] * (scale_percent / 100))

        destination_format = get_valid_format()
        destination = f'resized-image.{destination_format}'

        output = cv2.resize(image, (new_width, new_height))
        cv2.imwrite(destination, output)

        print("Resizing image to the given scale...")
        time.sleep(2)
        print(f"Image resized successfully. The resized image has been saved as '{destination}'.")
        time.sleep(3)
        print("Thank you for using our service. Please come again")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except cv2.error as e:
        print(f"OpenCV error: {e}. Please check the input image.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")


image_resizer()
