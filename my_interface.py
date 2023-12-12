import tkinter as tk
from hash_generator import create_has_sha1


def check(tb_1, tb_2, saida):
    password_original = str(tb_1.get())
    password_to_check = str(tb_2.get())

    has_password_original = create_has_sha1(password_original)
    has_to_check = create_has_sha1(password_to_check)

    if has_to_check == has_password_original:
        saida.config(text=str('Password valid'))
    else:
        saida.config(text=str('Password invalid'))


def form_check_password():
    janela = tk.Tk()

    tb_1 = tk.Entry(janela)
    tb_2 = tk.Entry(janela)

    botao = tk.Button(janela, text="Check", command=lambda: check(tb_1, tb_2, saida))

    saida = tk.Label(janela)
    v1 = tk.Label(janela, text='Password original: ')
    v2 = tk.Label(janela, text='Password to compare: ', padx=10)

    v1.grid(row=0, column=0)
    tb_1.grid(row=0, column=1)
    v2.grid(row=1, column=0)
    tb_2.grid(row=1, column=1)
    botao.grid(row=2, column=0, columnspan=2)
    saida.grid(row=3, column=0, columnspan=2)

    janela.mainloop()


def form_main(bt1, bt2, bt3, bt4):
    janela = tk.Tk()
    janela.title('Password Manager')
    janela.geometry('370x380')
    janela.configure(background='#123')
    intro = tk.Label(janela, text='Select the tool', background='#808080', font=22)
    intro.place(x=10, y=20, width=350, height=50)
    bt_f1 = tk.Button(janela, text='Password Generator', command=bt1)
    bt_f1.place(x=10, y=90, width=350, height=50)
    bt_f2 = tk.Button(janela, text='Hash generator', command=bt2)
    bt_f2.place(x=10, y=160, width=350, height=50)
    bt_f3 = tk.Button(janela, text='Hash generator by password', command=bt3)
    bt_f3.place(x=10, y=230, width=350, height=50)
    bt_f4 = tk.Button(janela, text='Check password', command=form_check_password)
    bt_f4.place(x=10, y=300, width=350, height=50)
    janela.mainloop()


def form_password_generator():
    janela = tk.Tk()
    global aux
    janela.title('Password Generator')
    janela.geometry('370x500')
    janela.configure(background='#123')
    num_of_char = tk.Label(janela, text='Size of password')
    num_of_char.place(x=10, y=20, width=170, height=50)
    tb_1 = tk.Entry(janela, font=18)
    tb_1.place(x=190, y=20, width=170, height=50)
    intro = tk.Label(janela, text='Select a password type', background='#808080', font=22)
    intro.place(x=10, y=90, width=350, height=50)
    bt_f1 = tk.Button(janela, text='Number', command=pass_gen_define_value('1'))
    bt_f1.place(x=10, y=160, width=350, height=50)
    bt_f2 = tk.Button(janela, text='Special Characters', command=pass_gen_define_value('2'))
    bt_f2.place(x=10, y=230, width=350, height=50)
    bt_f3 = tk.Button(janela, text='Any Characters', command=pass_gen_define_value('3'))
    bt_f3.place(x=10, y=300, width=350, height=50)
    bt_f4 = tk.Button(janela, text='Letters', command=pass_gen_define_value('4'))
    bt_f4.place(x=10, y=370, width=350, height=50)
    pass_gererated = tk.Label(janela, text='Password Generated', background='#6666FF', font=18)
    pass_gererated.place(x=10, y=440, width=350, height=50)
    janela.mainloop()


def pass_gen_define_value(value):
    global aux
    aux = value



form_password_generator()