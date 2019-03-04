from guizero import App, Text, PushButton, Slider, Picture, Window, error, TextBox

app = App(title="Sarah's App with picture")
app.bg = "white"
app.text_color = "black"
app.width = 500
app.height = 250

def background_yellow():
    app.bg = "yellow"
    
def background_green():
    app.bg = "green"

text = Text(app, text="This is my app, including cat!", size=20)
button_1 = PushButton(app, text="Make it yellow!", command=background_yellow)
button_2 = PushButton(app, text="Make it green!", command=background_green)

# NEW CODE STARTS
cat = Picture(app, image="cat.png")
cat.width = cat.width//2
cat.height = cat.height//2
# NEW CODE ENDS

app.display()
