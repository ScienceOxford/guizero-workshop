from guizero import App, Text, PushButton, Slider, Picture, Window, error, TextBox

app = App(title="Sarah's App")
app.bg = "white"
app.text_color = "black"
app.width = 500
app.height = 250

text = Text(app, text="This is my app!", size=20)
