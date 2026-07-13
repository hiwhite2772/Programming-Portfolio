from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Game XO 6x6")

SIZE = 6
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

    # Kiểm tra từng người chơi X và O
    for player in ["X", "O"]:
        # Kiểm tra hàng ngang
        for r in range(SIZE):
            if all(buttons[r][c]["text"] == player for c in range(SIZE)):
                highlightWinner([(r, c) for c in range(SIZE)], player)
                return

        # Kiểm tra hàng dọc
        for c in range(SIZE):
            if all(buttons[r][c]["text"] == player for r in range(SIZE)):
                highlightWinner([(r, c) for r in range(SIZE)], player)
                return

        # Kiểm tra đường chéo chính
        if all(buttons[i][i]["text"] == player for i in range(SIZE)):
            highlightWinner([(i, i) for i in range(SIZE)], player)
            return

        # Kiểm tra đường chéo phụ
        if all(buttons[i][SIZE - 1 - i]["text"] == player for i in range(SIZE)):
            highlightWinner([(i, SIZE - 1 - i) for i in range(SIZE)], player)
            return


def highlightWinner(positions, player):
    global win
    win = True

    for r, c in positions:
        buttons[r][c].config(bg="#80ffaa")

    if player == "X":
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
    else:
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")

    disableButtons()


def checkDraw():
    global count, win
    if count == SIZE * SIZE and win == False:
        messagebox.showerror("OX Game", "DRAW!!")


def buttonClicked(row, col):
    global clicked, count

    button = buttons[row][col]

    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkWinner()
        checkDraw()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        checkWinner()
        checkDraw()
    else:
        messagebox.showerror("OX Game", "LỖI!! Vui lòng chọn lại")


def start():
    global clicked, count, win, buttons

    clicked = True
    count = 0
    win = False

    buttons = []

    for r in range(SIZE):
        row_buttons = []
        for c in range(SIZE):
            button = Button(
                root,
                text=" ",
                font=("Cambria", 20),
                height=3,
                width=7,
                bg="SystemButtonFace",
                command=lambda row=r, col=c: buttonClicked(row, col),
            )
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
