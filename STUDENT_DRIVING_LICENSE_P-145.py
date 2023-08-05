# Basic tkinter template

from tkinter import *
root = Tk()
root.title("Driving License Card")
root.geometry("300x400")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")



label_id = Label(root)
label_name = Label(root)
label_dob = Label(root)
label_pin = Label(root)
label_address = Label(root)
label_vehicle_type = Label(root)



def myDrivingLicense():
    driving_license_id = 1920345910
    print(type(driving_license_id))
    driving_liscense_name = "Shreshth Shukla"
    print(type(driving_liscense_name))
    driving_license_dob = "21 August 1937"
    print(type(driving_license_dob))
    pincode = 205031
    print(type(pincode))
    address = "E-02 Type 3 New Campus Saifai Etawah"
    print(type(address))
    type_of_vehicle = "Four Weeler"
    print(type(type_of_vehicle))
    
    label_id["text"] = driving_license_id
    label_name["text"] = driving_liscense_name
    label_dob["text"] = driving_license_dob
    label_pin["text"] = pincode
    label_address["text"] = address
    label_vehicle_type["text"] = type_of_vehicle
    

button1 = Button(root, text="Show my driving License", command=myDrivingLicense())

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

# tkinter basic template end statement
root.mainloop()
