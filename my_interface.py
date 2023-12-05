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

form_check_password()