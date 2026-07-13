from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Game XO 5x5")
clicked = True
count = 0


def disableButtons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
    button10.config(state=DISABLED)
    button11.config(state=DISABLED)
    button12.config(state=DISABLED)
    button13.config(state=DISABLED)
    button14.config(state=DISABLED)
    button15.config(state=DISABLED)
    button16.config(state=DISABLED)
    button17.config(state=DISABLED)
    button18.config(state=DISABLED)
    button19.config(state=DISABLED)
    button20.config(state=DISABLED)
    button21.config(state=DISABLED)
    button22.config(state=DISABLED)
    button23.config(state=DISABLED)
    button24.config(state=DISABLED)
    button25.config(state=DISABLED)


def checkWinner():
    global win
    win = False
    if (
        button1["text"] == "X"
        and button2["text"] == "X"
        and button3["text"] == "X"
        and button4["text"] == "X"
        and button5["text"] == "X"
    ):
        button1.config(bg="#80ffaa")
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button6["text"] == "X"
        and button7["text"] == "X"
        and button8["text"] == "X"
        and button9["text"] == "X"
        and button10["text"] == "X"
    ):
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button11["text"] == "X"
        and button12["text"] == "X"
        and button13["text"] == "X"
        and button14["text"] == "X"
        and button15["text"] == "X"
    ):
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button16["text"] == "X"
        and button17["text"] == "X"
        and button18["text"] == "X"
        and button19["text"] == "X"
        and button20["text"] == "X"
    ):
        button16.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button21["text"] == "X"
        and button22["text"] == "X"
        and button23["text"] == "X"
        and button24["text"] == "X"
        and button25["text"] == "X"
    ):
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button1["text"] == "X"
        and button6["text"] == "X"
        and button11["text"] == "X"
        and button16["text"] == "X"
        and button21["text"] == "X"
    ):
        button1.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button2["text"] == "X"
        and button7["text"] == "X"
        and button12["text"] == "X"
        and button17["text"] == "X"
        and button22["text"] == "X"
    ):
        button2.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button3["text"] == "X"
        and button8["text"] == "X"
        and button13["text"] == "X"
        and button18["text"] == "X"
        and button23["text"] == "X"
    ):
        button3.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button4["text"] == "X"
        and button9["text"] == "X"
        and button14["text"] == "X"
        and button19["text"] == "X"
        and button24["text"] == "X"
    ):
        button4.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button5["text"] == "X"
        and button10["text"] == "X"
        and button15["text"] == "X"
        and button20["text"] == "X"
        and button25["text"] == "X"
    ):
        button1.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button1["text"] == "X"
        and button7["text"] == "X"
        and button13["text"] == "X"
        and button19["text"] == "X"
        and button25["text"] == "X"
    ):
        button1.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button5["text"] == "X"
        and button9["text"] == "X"
        and button13["text"] == "X"
        and button17["text"] == "X"
        and button21["text"] == "X"
    ):
        button5.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()

    if (
        button1["text"] == "O"
        and button2["text"] == "O"
        and button3["text"] == "O"
        and button4["text"] == "O"
        and button5["text"] == "O"
    ):
        button1.config(bg="#80ffaa")
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif (
        button6["text"] == "O"
        and button7["text"] == "O"
        and button8["text"] == "O"
        and button9["text"] == "O"
        and button10["text"] == "O"
    ):
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif (
        button11["text"] == "O"
        and button12["text"] == "O"
        and button13["text"] == "O"
        and button14["text"] == "O"
        and button15["text"] == "O"
    ):
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif (
        button16["text"] == "O"
        and button17["text"] == "O"
        and button18["text"] == "O"
        and button19["text"] == "O"
        and button20["text"] == "O"
    ):
        button16.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif (
        button21["text"] == "O"
        and button22["text"] == "O"
        and button23["text"] == "O"
        and button24["text"] == "O"
        and button25["text"] == "O"
    ):
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif (
        button1["text"] == "O"
        and button6["text"] == "O"
        and button11["text"] == "O"
        and button16["text"] == "O"
        and button21["text"] == "O"
    ):
        button1.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif (
        button2["text"] == "O"
        and button7["text"] == "O"
        and button12["text"] == "O"
        and button17["text"] == "O"
        and button22["text"] == "O"
    ):
        button2.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif (
        button3["text"] == "O"
        and button8["text"] == "O"
        and button13["text"] == "O"
        and button18["text"] == "O"
        and button23["text"] == "O"
    ):
        button3.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif (
        button4["text"] == "O"
        and button9["text"] == "O"
        and button14["text"] == "O"
        and button19["text"] == "O"
        and button24["text"] == "O"
    ):
        button4.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif (
        button5["text"] == "O"
        and button10["text"] == "O"
        and button15["text"] == "O"
        and button20["text"] == "O"
        and button25["text"] == "O"
    ):
        button1.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()
    elif (
        button1["text"] == "O"
        and button7["text"] == "O"
        and button13["text"] == "O"
        and button19["text"] == "O"
        and button25["text"] == "O"
    ):
        button1.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()
        start()
    elif (
        button5["text"] == "O"
        and button9["text"] == "O"
        and button13["text"] == "O"
        and button17["text"] == "O"
        and button21["text"] == "O"
    ):
        button5.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()
        start()


def checkDraw():
    global count, win
    if count == 25 and win == False:
        messagebox.showerror("OX Game", "DRAW!!")
        start()


def buttonClicked(button):
    global clicked, count
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
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button20, button21, button22, button23, button24, button25
    global clicked, count

    clicked = True
    count = 0
    button1 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button1),
    )
    button2 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button2),
    )
    button3 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button3),
    )
    button4 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button4),
    )
    button5 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button5),
    )
    button6 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button6),
    )
    button7 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button7),
    )
    button8 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button8),
    )
    button9 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button9),
    )
    button10 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button10),
    )
    button11 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button11),
    )
    button12 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button12),
    )
    button13 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button13),
    )
    button14 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button14),
    )
    button15 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button15),
    )
    button16 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button16),
    )
    button17 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button17),
    )
    button18 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button18),
    )
    button19 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button19),
    )
    button20 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button20),
    )
    button21 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button21),
    )
    button22 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button22),
    )
    button23 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button23),
    )
    button24 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button24),
    )
    button25 = Button(
        root,
        text=" ",
        font=("Cambria, 20"),
        height=3,
        width=7,
        bg="SystemButtonFace",
        command=lambda: buttonClicked(button25),
    )

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=0, column=4)
    button6.grid(row=1, column=0)
    button7.grid(row=1, column=1)
    button8.grid(row=1, column=2)
    button9.grid(row=1, column=3)
    button10.grid(row=1, column=4)
    button11.grid(row=2, column=0)
    button12.grid(row=2, column=1)
    button13.grid(row=2, column=2)
    button14.grid(row=2, column=3)
    button15.grid(row=2, column=4)
    button16.grid(row=3, column=0)
    button17.grid(row=3, column=1)
    button18.grid(row=3, column=2)
    button19.grid(row=3, column=3)
    button20.grid(row=3, column=4)
    button21.grid(row=4, column=0)
    button22.grid(row=4, column=1)
    button23.grid(row=4, column=2)
    button24.grid(row=4, column=3)
    button25.grid(row=4, column=4)


gameMenu = Menu(root)
root.config(menu=gameMenu)
optionMenu = Menu(gameMenu, tearoff=False)
gameMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Restart Game", command=start)
start()
root.mainloop()
