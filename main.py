#!/usr/bin/python

#----------------------------------------------------------------------
#
#   Lunar Analog Telemetry Test Emulator (LATTE), Rev. 1
#   3/3/2021
#   Main Python program to open the LATTE Device GUIs
#
#----------------------------------------------------------------------


# LIBRARIES
#----------------------------------------------------------------------

# Python Libraries
try:
    import Tkinter as tk
except:
    import tkinter as tk

from PIL import Image, ImageTk

# Local Files
import style
import lunar_gui
import power


# CLASSES
#----------------------------------------------------------------------

# Create the Main App
class Application(tk.Tk):

    # Initialize a GUI window with TKinter
    def __init__(self):
        tk.Tk.__init__(self)

        self._frame = None
        self.title( "LATTE 1.0" )
        self.attributes( '-fullscreen', False ) # CHANGE ON PI

        geom = str( style.s_f_width ) + "x" + str( style.s_f_height )
        self.geometry( geom )
        self.resizable(0, 0)

        self.switch_frame(StartPage)


    # Function to switch the current frame
    def switch_frame(self, frame_class):

        # Assign new frame
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()

        # Assign the frame
        self._frame = new_frame

        # Pack the frame
        self._frame.pack()
        self._frame.pack_propagate(0)

    # Function to close the GUI
    def close_gui( self ):
        self.destroy()

# Create the Start Page class
class StartPage(tk.Frame):

    # Initialize
    def __init__(self, master):

        # Initialize main frame
        tk.Frame.__init__( self, master )
        tk.Frame.configure( self, width = style.s_f_width, height = style.s_f_height, bg = style.c_background )

        # Create a frame for the buttons
        btn_frm = tk.Frame( self, bg = style.c_button)
        btn_frm.pack( side = "left", fill = "y" )

        # Add logo
        lgo = tk.Canvas( btn_frm, width = 100, height = 100, bg = style.c_button, bd=0, highlightthickness=0, relief='ridge' )
        lgo.pack( padx = 10, pady = 10)
        self.img = ImageTk.PhotoImage(Image.open( style.i_logo))
        lgo.create_image(50, 50, image = self.img)

        # Create buttons
        tk.Button(btn_frm, text="Power Supplies", bg = style.c_button, fg = style.c_text, borderwidth = 0, height = 2, width = 20, command=lambda: master.switch_frame(power.PowerSupplies)).pack()
        tk.Button(btn_frm, text="RadPC Lunar", bg = style.c_button, fg = style.c_text, borderwidth = 0, height = 2, width = 20, command=lambda: master.switch_frame(lunar_gui.RadPCLunar)).pack()
        tk.Button(btn_frm, text="Exit", bg = style.c_button, fg = style.c_text, borderwidth = 0, height = 2, width = 20, command=lambda: master.close_gui()).pack()


        # Create a label
        tk.Label( self, text="Start", bg = style.c_background, fg = style.c_text, height = 2, width = 20 ).pack( side = "left", fill = "x", pady = 5 )

# MAIN PROGRAM
#----------------------------------------------------------------------

if __name__ == "__main__":

    # Print a starting message
    print( "Starting GUI ..." )

    app = Application()
    app.mainloop()


#----------------------------------------------------------------------
# END OF CODE
