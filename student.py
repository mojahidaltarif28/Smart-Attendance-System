from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Smart Attendance System")

        img=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\iStock-182059956_18390_t12.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\face-recognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        img2=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\AdobeStock_303989091.jpeg")
        img2=img2.resize((590,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=560,height=130)

        img3=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\bg.png")
        img3=img3.resize((1560,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1540,height=700)
        title_lbl=Label(bg_img,text="Student Details",font=("times new roman",25,"bold"),bg="#222222",fg="#00c3e3")
        title_lbl.place(x=-15,y=0,width=1530,height=40)

        main_fram=Frame(bg_img,bd=2)
        main_fram.place(x=19,y=55,width=1470,height=560)

        #left label fram
        Left_fram=LabelFrame(main_fram,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_fram.place(x=10,y=10,width=760,height=530)

        #Right label fram
        Right_fram=LabelFrame(main_fram,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_fram.place(x=790,y=10,width=660,height=530)

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
