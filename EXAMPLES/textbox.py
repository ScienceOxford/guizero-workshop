from guizero import App, Text, PushButton, Slider, Picture, Window, error, TextBox

app = App(title="Sarah's App with input")
app.bg = "white"
app.text_color = "black"
app.width = 500
app.height = 250

def background_yellow():
    app.bg = "yellow"
    
def background_green():
    app.bg = "green"

# NEW CODE STARTS
def add_text():                                                         # creates a command called 'add_text'
    new_text = Text(app, text=input_box.value)                          # which creates a Text widget that uses the value of
                                                                        # the TextBox widget, created below, as the text
# NEW CODE ENDS

text = Text(app, text="This is my app, including input!", size=20)
button_1 = PushButton(app, text="Make it yellow!", command=background_yellow)
button_2 = PushButton(app, text="Make it green!", command=background_green)

# NEW CODE STARTS
input_box = TextBox(app, width=app.width)                               # creates a TextBox widget, called 'input_box'
button_3 = PushButton(app, text="Display the input", command=add_text)  # creates a PushButton widget, which calles the new command above
# NEW CODE ENDS
