from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Smart Attendance System")

        # variables
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_batch=StringVar()
        self.var_semsester=StringVar()
        self.var_teacher=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()

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

        main_fram=Frame(bg_img,bd=2,bg="#222222")
        main_fram.place(x=19,y=55,width=1470,height=560)

        #left label fram
        Left_fram=LabelFrame(main_fram,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="#222222",fg="#00c3e3")
        Left_fram.place(x=10,y=10,width=760,height=530)

        img_left=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\gettyimages-1022573162.jpg")
        img_left=img_left.resize((740,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_fram,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=740,height=140)
        #current course
        Current_course_fram=LabelFrame(Left_fram,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"),bg="black",fg="#00c3e3")
        Current_course_fram.place(x=5,y=130,width=740,height=140)
        #Department
        dep_label=Label(Current_course_fram,text="Department:",font=("times new roman",12,"bold"),bg="black",fg="#00c3e3")
        dep_label.grid(row=0,column=0,padx=8,sticky=E)
        dep_combo=ttk.Combobox(Current_course_fram,textvariable=self.var_dept,font=("times new roman",10,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select department","CSE","EEE","Pharmacy")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,pady=8,padx=2,sticky=W)
        #Course
        course_label=Label(Current_course_fram,text="Course:",font=("times new roman",12,"bold"),bg="black",fg="#00c3e3")
        course_label.grid(row=0,column=2,padx=8,sticky=E)
       
        dep_combo=ttk.Combobox(Current_course_fram,textvariable=self.var_course,font=("times new roman",10,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select Course","Artificial Intelligence","Artificial Intelligence Lab","Digital Image Processing","Computer Graphics And Animation","Data Mining And Data Warehousung","Criptography And Information Security")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,pady=8,padx=2,sticky=W)
        #Batch
        course_label=Label(Current_course_fram,text="Batch:",font=("times new roman",12,"bold"),bg="black",fg="#00c3e3")
        course_label.grid(row=1,column=0,padx=8,sticky=E)
       
        dep_combo=ttk.Combobox(Current_course_fram,textvariable=self.var_batch,font=("times new roman",10,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select Batch","10th","11th","12th","13th")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,pady=8,padx=2,sticky=W)
        #Semester
        course_label=Label(Current_course_fram,text="Semester:",font=("times new roman",12,"bold"),bg="black",fg="#00c3e3")
        course_label.grid(row=1,column=2,padx=8,sticky=E)
       
        dep_combo=ttk.Combobox(Current_course_fram,textvariable=self.var_semsester,font=("times new roman",10,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select Semester","1st year 1st semester","1st year 2nd semester","2nd year 1st semester","2nd year 2nd semester","3rd year 1st semester","3rd year 2nd semester","4th year 1st semester","4th year 2nd semester")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,pady=8,padx=2,sticky=W)

        #course teacher
        course_tearcher=Label(Current_course_fram,text="Course Teacher:",font=("times new roman",12,"bold"),bg="black",fg="#00c3e3")
        course_tearcher.grid(row=2,column=0,padx=8,sticky=E)

        StudentID_entry=ttk.Entry(Current_course_fram,textvariable=self.var_teacher,width=25,font=("times new roman",11,"bold"))
        StudentID_entry.grid(row=2,column=1,columnspan=3,padx=0,pady=8,sticky=W)

        #class student info
        Class_student_fram=LabelFrame(Left_fram,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"),bg="black",fg="#00c3e3")
        Class_student_fram.place(x=5,y=290,width=740,height=210)
       
        student_id_label=Label(Class_student_fram,text="Student ID:",font=("times new roman",12,"bold"),bg="black",fg="#00c3e3")
        student_id_label.grid(row=0,column=0,padx=8,sticky=E)

        StudentID_entry=ttk.Entry(Class_student_fram,textvariable=self.var_std_id,width=20,font=("times new roman",11,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=0,pady=10,sticky=W)

        student_name_label=Label(Class_student_fram,text="Student Name:",font=("times new roman",12,"bold"),bg="black",fg="#00c3e3")
        student_name_label.grid(row=0,column=2,padx=15,sticky=E)

        Student_Name_entry=ttk.Entry(Class_student_fram,textvariable=self.var_std_name,width=30,font=("times new roman",11,"bold"))
        Student_Name_entry.grid(row=0,column=3,padx=0,pady=10,sticky=W)

        #Radio buttons
        self.var_radio1=StringVar()
        radiobtn1=Radiobutton(Class_student_fram,variable=self.var_radio1,text="Take Photo Sample",bg="black",fg="#00c3e3",font=("times new roman",12,"bold"),value="YES")
        radiobtn1.grid(row=1,column=0,columnspan=2,padx=20,pady=0,sticky=E)
        
        self.var_radio2=StringVar()
        radiobtn2=Radiobutton(Class_student_fram,variable=self.var_radio1,text="No Photo Sample",bg="black",fg="#00c3e3",font=("times new roman",12,"bold"),value="NO")
        radiobtn2.grid(row=1,column=2,padx=8,pady=0,sticky=E)

        btn_fram=Frame(Left_fram,bd=2,relief=RIDGE,bg="#222222")
        btn_fram.place(x=20,y=400,width=701,height=86)

        #save button
        save_btn=Button(btn_fram,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0,sticky=W,pady=3,padx=2)
        #update button
        update_btn=Button(btn_fram,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="#1164B4",fg="white")
        update_btn.grid(row=0,column=1,sticky=W,pady=3,padx=2)
        #delete button
        delete_btn=Button(btn_fram,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="#8b0000",fg="white")
        delete_btn.grid(row=0,column=2,sticky=W,pady=3,padx=2)
        #Reset button
        Reset_btn=Button(btn_fram,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="#0059b3",fg="white")
        Reset_btn.grid(row=0,column=3,sticky=W,pady=3,padx=2)

        #Take photo button
        Take_photo_btn=Button(btn_fram,text="Take Photo Sample",command=self.generate_dataset,width=33,font=("times new roman",13,"bold"),bg="#0059b3",fg="white")
        Take_photo_btn.grid(row=1,column=0,columnspan=2,sticky=W,pady=3,padx=4)
        #update photo button
        Update_photo_btn=Button(btn_fram,text="Update Photo Sample",width=33,font=("times new roman",13,"bold"),bg="#0059b3",fg="white")
        Update_photo_btn.grid(row=1,column=2,columnspan=2,sticky=W,pady=3,padx=3)

        #Right label fram
        Right_fram=LabelFrame(main_fram,bd=2,relief=RIDGE,text="Search Student Details",font=("times new roman",12,"bold"),bg="#222222",fg="#00c3e3")
        Right_fram.place(x=790,y=10,width=660,height=530)
       
        img_right=Image.open(r"F:\7 semester\Artificial Intelligence\Project\Smart Attendance System\college_images\smart-attendance.jpg")
        img_right=img_right.resize((640,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_fram,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=640,height=140)

        # Search Frame
        Search_fram=LabelFrame(Right_fram,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),bg="black",fg="#00c3e3")
        Search_fram.place(x=5,y=130,width=640,height=90)
       
        Search_label=Label(Search_fram,text="Student ID:",font=("times new roman",12,"bold"),fg="#00c3e3",bg="black")
        Search_label.grid(row=0,column=0,padx=8,sticky=E)

        Search_ID_entry=ttk.Entry(Search_fram,width=20,font=("times new roman",11,"bold"))
        Search_ID_entry.grid(row=0,column=1,padx=0,pady=20,sticky=W)
        
        Search_btn=Button(Search_fram,text="Search",width=16,font=("times new roman",9,"bold"),bg="#0059b3",fg="white")
        Search_btn.grid(row=0,column=2,sticky=W,pady=3,padx=10)
       
        show_all_btn=Button(Search_fram,text="Show All",width=16,font=("times new roman",9,"bold"),bg="#0059b3",fg="white")
        show_all_btn.grid(row=0,column=3,sticky=W,pady=3,padx=2)

        #Table frame
        Table_fram=Frame(Right_fram,bd=2,relief=RIDGE,bg="black")
        Table_fram.place(x=5,y=230,width=640,height=280)

        scroll_x=ttk.Scrollbar(Table_fram,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_fram,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_fram,column=("Department","Course","Batch","Semester","Teacher","Student ID","Name","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Batch",text="Batch")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Teacher",text="Course Teacher")
        self.student_table.heading("Student ID",text="Student ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

       
        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Batch",width=50)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Teacher",width=200)
        self.student_table.column("Student ID",width=80)
        self.student_table.column("Name",width=200)
        self.student_table.column("Photo",width=200)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # function 
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="smart_attendance_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_batch.get(),
                    self.var_semsester.get(),
                    self.var_teacher.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Successfully Saved")
            except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="smart_attendance_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from students")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        

    #  get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_batch.set(data[2]),
        self.var_semsester.set(data[3]),
        self.var_teacher.set(data[4]),
        self.var_std_id.set(data[5]),
        self.var_std_name.set(data[6]),
        self.var_radio1.set(data[7])
    # Update function
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update data!",parent=self.root)
                if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="smart_attendance_system")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update students set department=%s,course=%s,batch=%s,semester=%s,course_teacher=%s,std_id=%s,std_name=%s,photo_sample=%s where std_id=%s",(
                            self.var_dept.get(),
                            self.var_course.get(),
                            self.var_batch.get(),
                            self.var_semsester.get(),
                            self.var_teacher.get(),
                            self.var_std_id.get(),
                            self.var_std_name.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get() 
                     ))
                else:
                    if  not Update:
                        return
                messagebox.showinfo("success","Successfully Update",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Id Fields are required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Do you want to Delete data!",parent=self.root)
                if Delete>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="smart_attendance_system")
                     my_cursor=conn.cursor()
                     my_cursor.execute("delete  from students where std_id=%s",(self.var_std_id.get(),))
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Successfully Delete",parent=self.root)
              
            except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # reset button
    def reset_data(self):
               self.var_std_id.set(""),
               self.var_std_name.set(""),
               self.var_radio1.set("NO"),
               self.var_radio2.set("NO"),
               self.var_std_id.set("") 
    #take photo sample
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="smart_attendance_system")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from students")
                my_result=my_cursor.fetchall()
                id=0 
                for x in my_result:
                    id+=1
                my_cursor.execute("update students set department=%s,course=%s,batch=%s,semester=%s,course_teacher=%s,std_name=%s,photo_sample=%s where std_id=%s",(
                            self.var_dept.get(),
                            self.var_course.get(),
                            self.var_batch.get(),
                            self.var_semsester.get(),
                            self.var_teacher.get(),
                            self.var_std_name.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()==id+1
                     ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets complete!")



            except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
