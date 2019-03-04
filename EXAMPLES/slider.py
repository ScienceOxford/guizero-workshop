from guizero import App, Text, PushButton, Slider, Picture, Window, error, TextBox

app = App(title="Sarah's App with slider")
app.bg = "white"
app.text_color = "black"
app.width = 500
app.height = 250

def background_yellow():
    app.bg = "yellow"
    
def background_green():
    app.bg = "green"

text = Text(app, text="This is my app, including slider!", size=20)
button_1 = PushButton(app, text="Make it yellow!", command=background_yellow)
button_2 = PushButton(app, text="Make it green!", command=background_green)

# NEW CODE STARTS
def colour_change():
    app.bg = (red.value, 0, 0)

red = Slider(app, start=0, end=255, command=colour_change)
# NEW CODE ENDS
