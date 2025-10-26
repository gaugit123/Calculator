from tkinter import *
root = Tk()

first_num = operator = second_num = None

def get_digit(digit):
    current = text_label['text']
    new = current + str(digit)
    text_label.config(text=new)

def clear():
    text_label.config(text="")

def operators(opt):
    global first_num, operator
    operator = opt
    global new_text
    new_text = text_label["text"] + operator # for printing the operator to the text
    text_label.config(text=new_text) #updating the text with operator
    global opt_index
    opt_index = new_text.find(operator)
    if new_text.find('.'):
        first_num = float(new_text[0:opt_index])
    else:
        first_num = int(new_text[0:opt_index])
    

def get_result():
   global second_num, opt_index, new_text, operator,first_num
   new_text = text_label['text'] #updating the text
   if new_text.find('.'):
        second_num = float(new_text[opt_index+1:])
   else:
        second_num = int(new_text[opt_index+1:])

   if operator == '+':
        sum = str(first_num+second_num)
        text_label.config(text=sum)
   elif operator == '-':
       sub = str(first_num-second_num)
       text_label.config(text=sub)
   elif operator == 'x':
       mul = str(first_num*second_num)
       text_label.config(text=mul)
   elif operator == '÷':
       div = str(first_num/second_num)
       text_label.config(text=div)
   elif operator == '%':
       mod = str(first_num%second_num)
       text_label.config(text=mod)

def delete():
    del_text = text_label['text']
    next_text = del_text[:len(del_text)-1]
    text_label.config(text=next_text)

def dot(dt):
    point = dt
    updated_text = text_label["text"] + point
    text_label.config(text=updated_text)
    

root.title("Calculator")
root.geometry("343x440")
root.resizable(0,0)#makes the size of claculator fixed
root.configure(background="black")
# root.iconbitmap('download.png')
#pack and grid are geometry manager i.e interior designer
text_label = Label(root, text='', bg='black' ,fg = 'white')
text_label.grid(row=0, column=0,columnspan=5, pady=(40,40),sticky='W')
text_label.config(font=("verdana", 25, 'bold'))

btn_clr = Button(root, text='C',fg = "black", width=3, height=2, command=lambda: clear())
btn_clr.grid(row=1, column=0,padx=(3,3))
btn_clr.config(font=("verdana",20, "bold"))

btn_del = Button(root, text='DEL',width=3, height=2, command=lambda:delete())
btn_del.grid(row=1, column=1, padx=(0,3))
btn_del.config(font=("verdana",20, "bold"))

btn_mod = Button(root, text='%',width=3, height=2, command=lambda:operators('%'))
btn_mod.grid(row=1, column=2, padx=(0,3))
btn_mod.config(font=("verdana",20, "bold"))

btn_div = Button(root, text='÷',width=3, height=2,command=lambda:operators('÷'))
btn_div.grid(row=1, column=3, padx=(0,3))
btn_div.config(font=("verdana",20, "bold"))

btn_7 = Button(root, text='7',width=3, height=2, command=lambda :get_digit(7))
btn_7.grid(row=2, column=0, pady=(3,3),padx=(3,3))
btn_7.config(font=("verdana",20, "bold"))

btn_8 = Button(root, text='8',width=3, height=2,command=lambda :get_digit(8))
btn_8.grid(row=2, column=1, pady=(3,3),padx=(0,3))
btn_8.config(font=("verdana",20, "bold"))

btn_9 = Button(root, text='9',width=3, height=2,command=lambda :get_digit(9))
btn_9.grid(row=2, column=2, pady=(3,3),padx=(0,3))
btn_9.config(font=("verdana",20, "bold"))

btn_mul = Button(root, text='x',width=3, height=2,command=lambda:operators('x'))
btn_mul.grid(row=2, column=3, pady=(3,3),padx=(0,3))
btn_mul.config(font=("verdana",20, "bold"))

btn_4 = Button(root, text='4',width=3, height=2,command=lambda :get_digit(4))
btn_4.grid(row=3, column=0, pady=(0,3),padx=(0,3))
btn_4.config(font=("verdana",20, "bold"))

btn_5 = Button(root, text='5',width=3, height=2,command=lambda :get_digit(5))
btn_5.grid(row=3, column=1, pady=(0,3),padx=(0,3))
btn_5.config(font=("verdana",20, "bold"))

btn_6 = Button(root, text='6',width=3, height=2,command=lambda :get_digit(6))
btn_6.grid(row=3, column=2, pady=(0,3),padx=(0,3))
btn_6.config(font=("verdana",20, "bold"))

btn_sub = Button(root, text='-',width=3, height=2,command=lambda:operators('-'))
btn_sub.grid(row=3, column=3, pady=(0,3),padx=(0,3))
btn_sub.config(font=("verdana",20, "bold"))

btn_1 = Button(root, text='1',width=3, height=2,command=lambda :get_digit(1))
btn_1.grid(row=4, column=0, pady=(0,3),padx=(3,3))
btn_1.config(font=("verdana",20, "bold"))

btn_2 = Button(root, text='2',width=3, height=2,command=lambda :get_digit(2))
btn_2.grid(row=4, column=1, pady=(0,3),padx=(0,3))
btn_2.config(font=("verdana",20, "bold"))

btn_3 = Button(root, text='3',width=3, height=2,command=lambda :get_digit(3))
btn_3.grid(row=4, column=2, pady=(0,3),padx=(0,3))
btn_3.config(font=("verdana",20, "bold"))

btn_plus = Button(root, text='+',width=3, height=2, command=lambda:operators('+'))
btn_plus.grid(row=4, column=3, pady=(0,3),padx=(0,3))
btn_plus.config(font=("verdana",20, "bold"))

btn_0 = Button(root, text='0',width=3, height=2,command=lambda :get_digit(0))
btn_0.grid(row=5, column=0, pady=(0,3),padx=(3,3))
btn_0.config(font=("verdana",20, "bold"))

btn_dot = Button(root, text='.',width=3, height=2, command=lambda:dot("."))
btn_dot.grid(row=5, column=1, pady=(0,3),padx=(0,3))
btn_dot.config(font=("verdana",20, "bold"))

btn_res = Button(root, text='=',width=9 ,height=2,command=lambda:get_result())
btn_res.grid(row=5, column=2, columnspan=2, pady=(0,3),padx=(0,3))
btn_res.config(font=("verdana",20, "bold"))


root.mainloop()