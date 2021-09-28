import random
a=['манки', 'вал ран+рол', 'тиктак в акур', 'манки с выходом на акуроси', 'манки+рол', 'прокрутка возле перипятствия на 360', 'сальто с земли на ноги', 'ревёрс, двайной манки', 'вал ран в акур', 'манки на кетлип', 'сальто с трубы на картоны', 'акуроси', 'вал ап на акураси', 'лач на манки', 'тик-так', 'вал ап', 'вал ран', 'кеш', 'конг']
import tkinter as tk

def tu_ran():
    na = random.choice(a)
    label.config(text=na)

win = tk.Tk()
win['bg'] = 'yellow'
win.resizable(width=False, height=False)
win.geometry(f"500x90+100+200")
win.title('Random')

c1 = tk.Button(win, text='Ran', command=tu_ran)
c1.place(x=207, y=45, width=85, height=33)

label = tk.Label(win, text='Click', bg='green', )
label.config(font=('Verdana', 25))
label.pack()
win.mainloop()
