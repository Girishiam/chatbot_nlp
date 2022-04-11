from tkinter import *
from tkinter import font

from click import command
from chat import get_response, bot_name


BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication():
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("ChatBot")
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # head_label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome Bots!", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text_widget
        self.text_widget = Text(self.window, width=20,
                                height=2, bg=BG_COLOR, font=FONT, fg=TEXT_COLOR, padx=5, pady=5)

        self.text_widget.place(relwidth=1, relheight=0.745, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scroll bar
        scrollBar = Scrollbar(self.text_widget)
        scrollBar.place(relheight=1, relx=0.974)
        scrollBar.configure(command=self.text_widget.yview)

        # bottom label

        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message
        self.msg_entry = Entry(bottom_label, bg="#2C3E50",
                               fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, rely=0.008,
                             relx=0.011, relheight=0.06)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_passed)

        # send button

        send_buttob = Button(bottom_label, text="Send",
                             font="FONT_BOLD", width=30, bg=BG_GRAY, command=lambda: self._on_enter_passed(None))
        send_buttob.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_passed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender} : {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name} : {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
