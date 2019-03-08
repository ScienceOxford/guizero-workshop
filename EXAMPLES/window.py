from guizero import App, Text, PushButton, Slider, Picture, Window, error, TextBox

app = App(title="Sarah's App with window")
app.bg = "white"
app.text_color = "black"
app.width = 500
app.height = 250

text = Text(app, text="This is my app, including window!", size=20)

# NEW CODE STARTS
window = Window(app, title="2nd window")                                # creates a Window widget, called 'window'
window.hide()                                                           # hides the new widget, so it's not there when the program starts

def open_window():                                                      # creates a new command called 'open_window'
    window.show()                                                       # that shows the window we created above
    
def close_window():                                                     # creates a new command called 'close_window'
    window.hide()                                                       # that hides the window we created above

open_button = PushButton(app, text="Open", command=open_window)         # creates a PushButton widget, in the main app
                                                                        # that calls the 'open_window' command created above
close_button = PushButton(window, text="Close", command=close_window)   # creates a PushButton widget, in the *new window*
                                                                        # that calls the 'close_window' command created above
# NEW CODE ENDS
