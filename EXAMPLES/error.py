from guizero import App, Text, PushButton, Slider, Picture, Window, error, TextBox

app = App(title="Sarah's App with error")
app.bg = "white"
app.text_color = "black"
app.width = 500
app.height = 250

def background_yellow():
    app.bg = "yellow"
    
def background_green():
    app.bg = "green"
    
# NEW CODE STARTS
def clicked():
    error('Error!', 'You cannnot click here...')
# NEW CODE ENDS

text = Text(app, text="This is my app, including error!", size=20)
button_1 = PushButton(app, text="Make it yellow!", command=background_yellow)
button_2 = PushButton(app, text="Make it green!", command=background_green)

# NEW CODE STARTS
button_3 = PushButton(app, text="Click me!", command=clicked)
# NEW CODE ENDS
