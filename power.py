#!/usr/bin/python

#----------------------------------------------------------------------
#
#   Lunar Analog Telemetry Test Emulator (LATTE), Rev. 1
#   3/3/2021
#   Power Supply Page
#
#----------------------------------------------------------------------


# LIBRARIES
#----------------------------------------------------------------------
import tkinter as tk

import main
import style

# CLASSES
#----------------------------------------------------------------------

# Class for the first page
class PowerSupplies(tk.Frame):

    # Initialize
    def __init__(self, master):

        # Create the new frame
        tk.Frame.__init__(self, master)
        tk.Frame.configure( self, width = style.s_f_width, height = style.s_f_height, bg = style.c_background )

        # Create label
        tk.Label( self, text="Power Supplies", bg = style.c_background, fg = style.c_text, height = 2, width = 20 ).pack( side = "top", fill = "x", pady = 5 )

        # Create button
        tk.Button(self, text="Menu", bg = style.c_button, fg = style.c_text, borderwidth = 0, height = 2, width = 20, command=lambda: master.switch_frame(main.StartPage)).pack()



#----------------------------------------------------------------------
# END OF CODE
