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
    
# NEW CODE STARTS
def colour_change():                                            # create a new command called 'colour_change'
    app.bg = (red.value, 0, 0)                                  # which changes the background colour of the app
            # the background colour is given as an (r, g, b) value, which means we specify how much red, green and blue makes up the colour
            # the amount of red in this example is controlled by the Slider widget, named 'red'
# NEW CODE ENDS

text = Text(app, text="This is my app, including slider!", size=20)
button_1 = PushButton(app, text="Make it yellow!", command=background_yellow)
button_2 = PushButton(app, text="Make it green!", command=background_green)

# NEW CODE STARTS
red = Slider(app, start=0, end=255, command=colour_change)      # create a Slider widget called red, which slides between 0 and 255,
                                                                # and calls the command created above
# NEW CODE ENDS
