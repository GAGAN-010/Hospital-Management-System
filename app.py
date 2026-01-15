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

        combobxNametablet=ttk.Combobox(DataframeLeft,font=("times new roman",12,"bold"),width=33)
        combobxNametablet["values"]=("Nice","corona","Acetaminophen","Adderall","Amlodipine","Ativan")
        combobxNametablet.grid(row=0,column=1)





        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFutherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Futher Information:",padx=2)
        lblFutherinfo.grid(row=0,column=2,sticky=W)
        txtFutherinfo=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtFutherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Bolld Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medicine",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtMedicine.grid(row=3,column=3,sticky=W)

        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="PatientId:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NhsNumber:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="DateOfBirth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddess=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddess.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)

        #======================== DATA FRAME RIGHT ===========================

        self.txtPrescrption=Text(DataframeRight,font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        self.txtPrescrption.grid(row=0,column=0)

root=Tk()
ob=Hospital(root)
root.mainloop()