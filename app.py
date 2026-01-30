from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

 
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ==========Data frame ========
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=480)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,font=("arial",12,"bold"),text="Prescrption")
        DataframeRight.place(x=990,y=5,width=460,height=350)

        #==============  BUTTON FRAME  ===========
        
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        #==============  DETAILS FORMAT  ===========
        
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #============== DATA FRAME LEFT =============

        lblNameTablet=Label(DataframeLeft,text="Name of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        combobxNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=33)
        combobxNametablet["values"]=("Nice","corona","Acetaminophen","Adderall","Amlodipine","Ativan")
        combobxNametablet.grid(row=0,column=1)





        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFutherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Futher Information:",padx=2)
        lblFutherinfo.grid(row=0,column=2,sticky=W)
        txtFutherinfo=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFutherinfo.grid(row=0,column=3)

        lblDrivingMachine=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblDrivingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=35)  
        txtDrivingMachine.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medicine",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMedication,width=35) 
        txtMedicine.grid(row=3,column=3,sticky=W)

        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="PatientId:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NhsNumber:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="DateOfBirth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddess=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddess.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)

        #======================== DATA FRAME RIGHT ===========================

        self.txtPrescrption=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescrption.grid(row=0,column=0)

        #======================== BUTTON ===========================
        
        btnprescription = Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial", 12, "bold"),width=23,height=2,padx=2,pady=6)
        btnprescription.grid(row=0, column=0)

        btnprescriptionData = Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("arial", 12, "bold"),width=23,height=2,padx=2,pady=6)
        btnprescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial", 12, "bold"),width=23,height=2,padx=2,pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial", 12, "bold"),width=23,height=2,padx=2,pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial", 12, "bold"),width=23,height=2,padx=2,pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial", 12, "bold"),width=23,height=2,padx=2,pady=6)
        btnExit.grid(row=0, column=5)

        #======================== TABLE ===========================

        #======================== SCROLL BAR ===========================

        Scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","nooftablet","lot","issuedate","expdate","dailydose"
                                                               ,"storage","nhsnumber","pname","dob","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        Scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("nameoftable", text="Name Of Table")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablet", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablet", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1 )
        self.fatch_data()

        #==================== DATABASE FUNCTIONALITY DECLEARATION ===============
        def iprescriptionDate(self):
            if self.Nameoftablets.get() == "" or self.ref.get() == "":
                messagebox.showerror("Error", "All fields are required")
                return

        conn = mysql.connector.connect(
            host="localhost",
            user="hospital_user",
            password="JAISHREERAM",
            database="Mydata"
        )
        my_cursor = conn.cursor()

        query = """
        INSERT INTO hospital
        (nameoftable, ref, dose, nooftablet, lot, issuedate, expdate,
        dailydose, storage, nhsnumber, pname, dob, address)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            self.Nameoftablets.get(),
            self.ref.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get()
        )

        my_cursor.execute(query, values)
        conn.commit()
        conn.close()

        self.fatch_data()
        messagebox.showinfo("Success", "Record inserted successfully")


    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost",user="hospital_user",password="JAISHREERAM",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


conn = mysql.connector.connect(host="localhost",user="hospital_user",password="JAISHREERAM",database="Mydata")
    

root=Tk()
ob=Hospital(root)
root.mainloop()
 
    #======================== TABLE ===========================

        #======================== SCROLL BAR ===========================

        Scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","nooftablet","lot","issuedate","expdate","dailydose"
                                                               ,"storage","nhsnumber","pname","dob","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        Scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("nameoftable", text="Name Of Table")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablet", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablet", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1 )
        self.fatch_data()

        #==================== DATABASE FUNCTIONALITY DECLEARATION ===============
        def iprescriptionDate(self):
            if self.Nameoftablets.get() == "" or self.ref.get() == "":
                messagebox.showerror("Error", "All fields are required")
                return

        conn = mysql.connector.connect(
            host="localhost",
            user="hospital_user",
            password="JAISHREERAM",
            database="Mydata"
        )
        my_cursor = conn.cursor()

        query = """
        INSERT INTO hospital
        (nameoftable, ref, dose, nooftablet, lot, issuedate, expdate,
        dailydose, storage, nhsnumber, pname, dob, address)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            self.Nameoftablets.get(),
            self.ref.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get()
        )

        my_cursor.execute(query, values)
        conn.commit()
        conn.close()

        self.fatch_data()
        messagebox.showinfo("Success", "Record inserted successfully")


    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost",user="hospital_user",password="JAISHREERAM",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


conn = mysql.connector.connect(host="localhost",user="hospital_user",password="JAISHREERAM",database="Mydata")
    

root=Tk()
ob=Hospital(root)
root.mainloop()
 