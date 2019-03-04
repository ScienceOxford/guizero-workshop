from guizero import App, Text, PushButton, Slider, Picture, Window, error, TextBox

app = App(title="Sarah's App with window")
app.bg = "white"
app.text_color = "black"
app.width = 500
app.height = 250

text = Text(app, text="This is my app, including window!", size=20)

# NEW CODE STARTS
window = Window(app, title="2nd window")
window.hide()

def open_window():
    window.show()
    
def close_window():
    window.hide()

open_button = PushButton(app, text="Open", command=open_window)
close_button = PushButton(window, text="Close", command=close_window)
# NEW CODE ENDS
