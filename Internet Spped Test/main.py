from tkinter import *
import speedtest

def internet_speed_test():
    lab_msg.config(text="Calculating your Internet Speed.....")
    sp.after(100, perform_speed_test)  # due to some error in tkinter classes,we run perform_speed_test() run after 1 second so that it update the GUI first that we manipulated by updating the lab_msg box above after when check speed button is clicked and then run the actual speedtest procedure after updating lab_msg box

def perform_speed_test():
    try:
        lab_msg.config(text="calculating your Internet Speed.....")
        st = speedtest.Speedtest()
        st.get_servers()
        down = str(round(st.download() / (10 ** 6), 3)) + " Mbps"
        up = str(round(st.upload() / (10 ** 6), 3)) + " Mbps"
        lab_msg.config(text="your Internet Speed is")
        lab_down.config(text=down)
        lab_up.config(text=up)
    except Exception as e:
        lab_msg.config(text=f"Error: {str(e)}")

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="Black")

lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 42, "bold"), bg="black", fg="yellow")
lab.place(x=8, y=10, height=90, width=480)


lab = Label(sp, text="Download Speed", font=("Time New Roman", 32, "bold"), bg="black", fg="white")
lab.place(x=40, y=150, height=60, width=400)
lab_down = Label(sp, text="00", font=("Time New Roman", 32, "bold"), bg="black", fg="white")
lab_down.place(x=40, y=220, height=40, width=400)

lab = Label(sp, text="Upload Speed", font=("Time New Roman", 32, "bold"), bg="black", fg="white")
lab.place(x=40, y=300, height=60, width=400)
lab_up = Label(sp, text="00", font=("Time New Roman", 32, "bold"), bg="black", fg="white")
lab_up.place(x=40, y=360, height=60, width=400)

lab_msg = Label(sp, text="", font=("Time New Roman", 18, "bold"), bg="black", fg="yellow")
lab_msg.place(x=8, y=100, height=40, width=480)

button = Button(sp, text="Check Speed", font=("Time New Roman", 31, "bold"), bg="red", fg="black", relief=RAISED, cursor="hand2", command=internet_speed_test)
button.place(x=80, y=470, height=70, width=320)

sp.mainloop()
