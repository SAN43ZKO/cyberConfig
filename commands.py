from flet import *

#Console command Text START
    
#Crosshair command
cros_size = Text("cl_crosshair_size", color="#ffffff", weight="bold", size=20)
cros_scale = Text("cl_crosshairscale", color="#ffffff", weight="bold", size=20)
cros_style = Text("cl_crosshairstyle", color="#ffffff", weight="bold", size=20)
cros_color = Text("cl_crosshair_color", color="#ffffff", weight="bold", size=20)
#Console command Text END

#Value commands START

#Crosshair commands value
cros_size_value = TextField(label="Number", width=100, height=50)
cros_scale_value = TextField(label="Number", width=100, height=50)
cros_style_value = TextField(label="Number", width=100, height=50)
cros_color_value = TextField(label="Number", width=100, height=50)
#Value commands END
