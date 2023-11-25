from tkinter import *
import speedtest

def internet_speed_test():
    lab_msg.config(text="Calculating your Internet Speed.....")
    sp.after(100, perform_speed_test)

def perform_speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_servers()
        down = f"{round(st.download() / (10 ** 6), 3)} Mbps"
        up = f"{round(st.upload() / (10 ** 6), 3)} Mbps"
        lab_msg.config(text="Your Internet Speed is:")
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

button = Button(sp, text="Check Speed", font=("Time New Roman", 31, "bold"), bg="red", fg="black", relief=RAISED, command=internet_speed_test, cursor="hand2")
button.place(x=80, y=470, height=70, width=320)

sp.mainloop()
