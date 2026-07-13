from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Game XO 8x8")

clicked = True
count = 0
win = False
buttons = []


def disableButtons():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)


def checkWinner():
    global win

    lines = []

    for r in range(8):
        lines.append([buttons[r][c] for c in range(8)])

    for c in range(8):
        lines.append([buttons[r][c] for r in range(8)])

    lines.append([buttons[i][i] for i in range(8)])
    lines.append([buttons[i][7 - i] for i in range(8)])

    for line in lines:
        if all(button["text"] == "X" for button in line):
            for button in line:
                button.config(bg="#80ffaa")
            win = True
            messagebox.showinfo("OX Game", "Player 1 WINNER!!")
            disableButtons()
            return

        if all(button["text"] == "O" for button in line):
            for button in line:
                button.config(bg="#80ffaa")
            win = True
            messagebox.showinfo("OX Game", "Player 2 WINNER!!")
            disableButtons()
            return


def checkDraw():
    if count == 64 and win == False:
        messagebox.showerror("OX Game", "DRAW!!")


def buttonClicked(button):
    global clicked, count

    if button["text"] == " ":
        if clicked == True:
            button["text"] = "X"
            clicked = False
        else:
            button["text"] = "O"
            clicked = True

        count += 1
        checkWinner()
        checkDraw()
    else:
        messagebox.showerror("OX Game", "LỖI!! Vui lòng chọn lại")


def start():
    global buttons, clicked, count, win

    clicked = True
    count = 0
    win = False

    for row in buttons:
        for button in row:
            button.destroy()

    buttons = []

    for r in range(8):
        row_buttons = []

        for c in range(8):
            button = Button(
                root,
                text=" ",
                font=("Cambria", 14),
                height=2,
                width=5,
                bg="SystemButtonFace",
            )

            button.config(command=lambda b=button: buttonClicked(b))
            button.grid(row=r, column=c)

            row_buttons.append(button)

        buttons.append(row_buttons)


gameMenu = Menu(root)
root.config(menu=gameMenu)

optionMenu = Menu(gameMenu, tearoff=False)
gameMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Restart Game", command=start)

start()
root.mainloop()