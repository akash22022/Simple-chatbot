from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *

bot = ChatBot('My Bot')

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

main = Tk()
main.geometry('500x650')

main.title('My Chat bot')
img = PhotoImage(file='bot.png')

photoL = Label(main, image=img)
photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, 'you : '+ query)
    msgs.insert(END, 'Groot : ' + str(answer_from_bot))
    textF.delete(0, END)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=15)
sc.pack(side=RIGHT, fill = Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

textF = Entry(main, font=('Verdana', 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text='Ask me',font=('verdana', 20),command=ask_from_bot )
btn.pack()

main.mainloop()