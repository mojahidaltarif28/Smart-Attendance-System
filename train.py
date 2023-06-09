from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import cv2
from tkinter import messagebox
import mysql.connector
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Smart Attendance System")
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",25,"bold"),bg="#222222",fg="#00c3e3")
        title_lbl.place(x=-15,y=0,width=1540,height=50)

        img_top=Image.open(r"college_images\facialrecognition.png")
        img_top=img_top.resize((1525,210),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1525,height=210)

        img_bottom=Image.open(r"college_images\Photos.jpg")
        img_bottom=img_bottom.resize((1525,350),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=270,width=1525,height=350)
        #   button
        b1_1=Button(self.root,text="Train Data",command=self.Train_Classifier,cursor="hand2",font=("times new roman",16,"bold"),bg="#222222",fg="#00c3e3")
        b1_1.place(x=0,y=260,width=1523,height=45)
    
    def Train_Classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #gray scale convert
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])                                                           

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Trainning Data Set Completed")





if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()