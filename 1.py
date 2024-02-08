from tkinter import*

bomb = 100
score = 0
record = 0
press_return = True

def start(event):
    global record
    global press_return
    global bomb
    global score
    read_record()
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        label.config(text = '')
        update_bomb()
        update_point()
        update_display()
        press_return = False

def update_display():
    global score
    global bomb
    if bomb > 50:
        bomb_label.config(image = normal_photo)
    elif 0 < bomb < 50:
        bomb_label.config(image = no_photo)
    else:
        bomb_label.config(image = bang_photo)
    fuse_label.config(text = 'Fuse: ' + str(bomb))
    score_label.config(text = 'Score: ' + str(score))
    fuse_label.after(100, update_display)
def update_point():
    global score
    score += 1
    if is_alive():
        score_label.after(3000, update_point)

def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(500, update_bomb)

def click():
    global bomb
    if is_alive():
        bomb += 1


def is_alive():
    global bomb
    global press_return
    if bomb <= 0:
        label.config(text='Bang! Bang! Bang!')
        save_record()
        press_return = True
        return False
    else:
        return True
    

def read_record():
    global record 
    try:
         with open('record.txt','r+') as file:
            record = int(file.readline())
            record_label.config(text = 'Record: ' + str(record))
            print(record)
    except:
        record = 0

   

def save_record():
    global record
    global score
    if score > record:
        with open('record.txt', 'w+') as file:
            file.write (str(score))

# read_record()

root = Tk()
root.title('Bang Bang!!!')
root.geometry('500x550')


label = Label(root, text = 'Press [Enter] to start the game', font=('Protest Riot', 12))
label.pack()


fuse_label = Label(root, text='Fuse: ' + str(bomb))
fuse_label.pack()#side=LEFT, anchor='ne', padx=40, pady=20


score_label = Label(root, text='Score: ' + str(score), font=('Protest Riot', 14))
score_label.pack()#side=RIGHT, anchor='nw', padx = 40, pady = 20

record_label = Label(root, text='Record: ' + str(record), font=('Protest Riot', 14))
record_label.pack()#side=RIGHT, anchor='nw', padx = 40, pady = 20


normal_photo = PhotoImage(file="img/bomb_normal.gif")
no_photo = PhotoImage(file="img/bomb_no.gif")
bang_photo = PhotoImage(file="img/pow.gif")

bomb_label = Label(root, image=normal_photo)
bomb_label.pack()

click_button = Button(root,text='Click me', bg='red', command=click, font=('Protest Riot', 14), width=20)
click_button.pack()

# root.bind('<Return>', read_record)
root.bind('<Return>', start)

root.mainloop()






