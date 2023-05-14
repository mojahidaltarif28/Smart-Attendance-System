from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Smart Attendance System")

        img=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        img2=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\abcd.jpg")
        img2=img2.resize((590,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=560,height=130)

        img3=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\bg.png")
        img3=img3.resize((1560,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1540,height=700)

        title_lbl=Label(bg_img,text="SMART ATTENDANCE SYSTEM",font=("times new roman",25,"bold"),bg="#222222",fg="#00c3e3")
        title_lbl.place(x=-15,y=0,width=1530,height=40)
    #student btn
        img4=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\smart-attendance.jpg")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",12,"bold"),bg="#222222",fg="#00c3e3")
        b1_1.place(x=200,y=240,width=150,height=35)
    #Detect face btn
        img5=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\facedetector.jpg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=400,y=100,width=150,height=150)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",12,"bold"),bg="#222222",fg="#00c3e3")
        b2_1.place(x=400,y=240,width=150,height=35)
     #Attendance btn
        img6=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\report.jpg")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=600,y=100,width=150,height=150)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",12,"bold"),bg="#222222",fg="#00c3e3")
        b3_1.place(x=600,y=240,width=150,height=35)
    #Train btn
        img7=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\Train.jpg")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=800,y=100,width=150,height=150)

        b4_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",12,"bold"),bg="#222222",fg="#00c3e3")
        b4_1.place(x=800,y=240,width=150,height=35)
    #Photos btn
        img8=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\Photos.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=1000,y=100,width=150,height=150)

        b5_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",12,"bold"),bg="#222222",fg="#00c3e3")
        b5_1.place(x=1000,y=240,width=150,height=35)
     #exit btn
        img9=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\exit.jpg")
        img9=img9.resize((100,100),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=1045,y=300,width=100,height=100)

        b6_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",12,"bold"),bg="#222222",fg="#00c3e3")
        b6_1.place(x=1045,y=390,width=100,height=30)



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

