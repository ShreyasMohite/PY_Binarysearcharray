from tkinter import *
import tkinter.messagebox

class binary:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x300")
        self.root.title("Binary Search")
        self.root.resizable(0,0)

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()

        Array1=IntVar()
        Array2=IntVar()
        Array3=IntVar()
        Array4=IntVar()
        Array5=IntVar()
        Array6=IntVar()
        Array7=IntVar()
        Array8=IntVar()
        search_number=IntVar()

        #==================================
        def openA():
            if(var1.get()==1):
                Ent_A.config(state="normal")
                Array1.set("")
            else:
                Ent_A.config(state="disable")

        def openB():
            if(var2.get()==1):
                Ent_B.config(state="normal")
                Array2.set("")
            else:
                Ent_B.config(state="disable")


        def openC():
            if(var3.get()==1):
                Ent_C.config(state="normal")
                Array3.set("")
            else:
                Ent_C.config(state="disable")

        def openD():
            if(var4.get()==1):
                Ent_D.config(state="normal")
                Array4.set("")
            else:
                Ent_D.config(state="disable")

        def openE():
            if(var5.get()==1):
                Ent_E.config(state="normal")
                Array5.set("")
            else:
                Ent_E.config(state="disable")

        def openF():
            if(var6.get()==1):
                Ent_F.config(state="normal")
                Array6.set("")
            else:
                Ent_F.config(state="disable")

        def openG():
            if(var7.get()==1):
                Ent_G.config(state="normal")
                Array7.set("")
            else:
                Ent_G.config(state="disable")

        def openH():
            if(var8.get()==1):
                Ent_H.config(state="normal")
                Array8.set("")
            else:
                Ent_H.config(state="disable")

        def on_enter(e):
            But_Search['background']="black"
            But_Search['foreground']="cyan"
               
               

        def on_leave(e):
            But_Search['background']="SystemButtonFace"
            But_Search['foreground']="SystemButtonText"
        
        def on_enter1(e):
            But_Res['background']="black"
            But_Res['foreground']="cyan"
               
               

        def on_leave2(e):
            But_Res['background']="SystemButtonFace"
            But_Res['foreground']="SystemButtonText"


        def reset():
            Array1.set(0)
            Array2.set(0)
            Array3.set(0)
            Array4.set(0)
            Array5.set(0)
            Array6.set(0)
            Array7.set(0)
            Ent_A.config(state="disable")
            Ent_B.config(state="disable")
            Ent_C.config(state="disable")
            Ent_D.config(state="disable")
            Ent_E.config(state="disable")
            Ent_F.config(state="disable")
            Ent_G.config(state="disable")
            Ent_H.config(state="disable")
            TXT.delete("1.0",END)
            search_number.set("")

        
        def search():
            try:
                arr=[Array1.get(),Array2.get(),Array3.get(),Array4.get(),Array5.get(),Array6.get(),Array7.get(),Array8.get()]
                n=search_number.get()
                for i in range(len(arr)):
                    if arr[i]==n:
                        found=1
                        pos=i
                        break
                if found==1:
                    #print("the number is present in pos=",pos)
                    TXT.delete('1.0',END)
                    TXT.insert(END,"The number  ")
                    TXT.insert(END,search_number.get())
                    TXT.insert(END,"  is present in Array position = ") 
                    TXT.insert(END,pos)
                else:
                    tkinter.messagebox.showerror("not found")
            except:
                tkinter.messagebox.askretrycancel("Information","Number not Found/Somthing went Wrong",icon="info")






        #====================Frame============================
        Main_Frame=Frame(self.root,bd=3,relief=RIDGE,width=500,height=300)
        Main_Frame.place(x=0,y=0)

        Frame_top=Frame(Main_Frame,width=495,height=200,relief=RIDGE,bd=3,bg="cyan")
        Frame_top.place(x=0,y=0)

        Frame_bottom=Frame(Main_Frame,width=495,height=95,relief=RIDGE,bd=3,bg="#163481")
        Frame_bottom.place(x=0,y=200)
        #===================Frame_top==========================
        Lab_Top=LabelFrame(Frame_top,width=490,height=195,font=('times new roman',12,'bold'),text="Insert The Array Element",bg="#66c1a8",fg="#010a0c")
        Lab_Top.place(x=0,y=0)
        #==============Txt========================================
        TXT=Text(Frame_bottom,width=60,height=4,font=('times new roman',12,'bold'))
        TXT.place(x=3,y=3)
        #==========================================================
        chk_A=Checkbutton(Lab_Top,text="A",bg="#66c1a8",variable=var1,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openA)
        chk_A.place(x=20,y=60)

        Ent_A=Entry(Lab_Top,width=3,font=('times new roman',12,'bold'),textvariable=Array1,state="disable")
        Ent_A.place(x=20,y=20)

        chk_B=Checkbutton(Lab_Top,text="B",bg="#66c1a8",variable=var2,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openB)
        chk_B.place(x=80,y=60)

        Ent_B=Entry(Lab_Top,width=3,font=('times new roman',12,'bold'),textvariable=Array2,state="disable")
        Ent_B.place(x=80,y=20)

        chk_C=Checkbutton(Lab_Top,text="C",bg="#66c1a8",variable=var3,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openC)
        chk_C.place(x=140,y=60)

        Ent_C=Entry(Lab_Top,width=3,font=('times new roman',12,'bold'),textvariable=Array3,state="disable")
        Ent_C.place(x=140,y=20)

        chk_D=Checkbutton(Lab_Top,text="D",bg="#66c1a8",variable=var4,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openD)
        chk_D.place(x=200,y=60)

        Ent_D=Entry(Lab_Top,width=3,font=('times new roman',12,'bold'),textvariable=Array4,state="disable")
        Ent_D.place(x=200,y=20)

        chk_E=Checkbutton(Lab_Top,text="E",bg="#66c1a8",variable=var5,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openE)
        chk_E.place(x=260,y=60)

        Ent_E=Entry(Lab_Top,width=3,font=('times new roman',12,'bold'),textvariable=Array5,state="disable")
        Ent_E.place(x=260,y=20)

        chk_F=Checkbutton(Lab_Top,text="F",bg="#66c1a8",variable=var6,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openF)
        chk_F.place(x=320,y=60)

        Ent_F=Entry(Lab_Top,width=3,font=('times new roman',12,'bold'),textvariable=Array6,state="disable")
        Ent_F.place(x=320,y=20)

        chk_G=Checkbutton(Lab_Top,text="G",bg="#66c1a8",variable=var7,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openG)
        chk_G.place(x=380,y=60)

        Ent_G=Entry(Lab_Top,width=3,font=('times new roman',12,'bold'),textvariable=Array7,state="disable")
        Ent_G.place(x=380,y=20)

        chk_H=Checkbutton(Lab_Top,text="H",bg="#66c1a8",variable=var8,onvalue=1,offvalue=0,font=('times new roman',12,'bold'),command=openH)
        chk_H.place(x=440,y=60)

        Ent_H=Entry(Lab_Top,width=3,font=('times new roman',12,'bold'),textvariable=Array8,state="disable")
        Ent_H.place(x=440,y=20)

        lab_search=Label(Lab_Top,text="Search :",bg="#66c1a8",font=('times new roman',11,'bold'))
        lab_search.place(x=10,y=130)

        Ent_search=Entry(Lab_Top,width=10,font=('times new roman',12,'bold'),textvariable=search_number,bd=3)
        Ent_search.place(x=70,y=130)

        But_Search=Button(Lab_Top,text="Search",font=('times new roman',12,'bold'),cursor="hand2",command=search)
        But_Search.place(x=180,y=130)
        But_Search.bind("<Enter>",on_enter)
        But_Search.bind("<Leave>",on_leave)

        
        But_Res=Button(Lab_Top,text="RESET",font=('times new roman',11,'bold'),command=reset,cursor="hand2")
        But_Res.place(x=400,y=130)
        But_Res.bind("<Enter>",on_enter1)
        But_Res.bind("<Leave>",on_leave2)






if __name__ == "__main__":
    root=Tk()
    app=binary(root)
    root.mainloop()
