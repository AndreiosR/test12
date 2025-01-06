### GUI imports
from guizero import *
from main import *

### GUI functions
def my_first_gui_function():
    text_welcome.value = "Zdravím"
    try:
        weight=float(txtbox_weight.value)
        cmlrounded=prepocet_CML()
    except:
        text_cml.value = "Vlož číslo, prosím"
        return
    activityfactor=float(txtbox_af.value)
    text_cml.value = "Tvé denní výdaje:"
    text_cml.value = cmlrounded
    prepocet_CML()

### GUI App
app = App(title="My App", width=770, height=640)

## Window 1
window1 = Box(app, visible=True)

# Welcome text
text_welcome = Text(window1, text=(f"Zdravím"))

# Input activity factor
text_af = Text(
    window1,
    text=(
        "        Jak moc jsi cvičil(a)"
    )
)
txtbox_af = TextBox(window1)

# Input weight
text_weight = Text(
    window1,
    text=(f"Kolik vážíš? (kg):")
)
txtbox_weight = TextBox(window1)

# Output calorie maintenance level
text_cml = Text(window1, text ="")

# tlačítečko
button = PushButton(window1, command=my_first_gui_function)

# Display an image
image_widget = Picture(
    window1,
    image="resources/camera-icon.png",
    width=680,
    height=480,
    align="bottom"
)
