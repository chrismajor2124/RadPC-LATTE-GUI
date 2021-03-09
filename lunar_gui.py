#!/usr/bin/python

#----------------------------------------------------------------------
#
#   Lunar Analog Telemetry Test Emulator (LATTE), Rev. 1
#   3/3/2021
#   RadPC Lunar Page
#
#----------------------------------------------------------------------


# LIBRARIES
#----------------------------------------------------------------------
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

import main
import style

# CLASSES
#----------------------------------------------------------------------

# Class for the first page
class RadPCLunar(Frame):

    # Initialize
    def __init__(self, master):

        # Create the new frame
        Frame.__init__(self, master)
        Frame.configure( self, width = style.s_f_width, height = style.s_f_height, bg = style.c_background )

        # Create button
        Button(self, text="Menu", bg = style.c_button, fg = style.c_text, borderwidth = 0, height = 2, width = 20, command=lambda: master.switch_frame(main.StartPage)).pack()

        # MAIN FRAME
        #------------
        self.f_main = Frame( self, width = style.s_f_width, height = style.s_f_height, background = style.c_background )
        self.f_main.pack()
        self.f_main.grid_propagate(0)


        # Large Serial Frame
        #------------
        self.f_ser = Frame( self.f_main, width = ( style.s_f_width - (2 * style.p_padding) ), height = ( 180 - (2 * style.p_padding) ), background = style.c_button, highlightthickness = 0, highlightbackground = style.c_text )
        self.f_ser.grid( row = 0, column = 0, columnspan = 3, padx = style.p_padding, pady = style.p_padding )
        self.f_ser.pack_propagate(0)

        self.s_serial = scrolledtext.ScrolledText( self.f_ser, background = style.c_button, state = "disabled", foreground = style.c_green, height = ( 300 - (2 * style.p_padding) ), relief = "solid", wrap = WORD )
        self.s_serial.vbar.config( troughcolor = style.c_button, background = style.c_button )
        self.s_serial.pack( fill = BOTH )
        self.s_serial.insert( INSERT, "SEM" )


        # Tiles Frame
        #-------------
        self.f_tiles = Frame( self.f_main, width = ( 200 ), height = ( 200 ), background = style.c_button, highlightthickness = 0, highlightbackground = style.c_text )
        self.f_tiles.grid_propagate(0)
        self.f_tiles.grid( row = 1, column = 0, padx = style.p_padding, pady = style.p_padding )

        # Tiles
        self.f_tile_0 = Frame( self.f_tiles, width = 80, height = 80, highlightthickness = 1, highlightbackground = style.c_text)
        self.l_tile_0 = Label( self.f_tile_0, text = "0000", foreground = style.c_blue, background = style.c_background )
        self.f_tile_0.grid(row = 0, column = 0, padx =10, pady=10)
        self.l_tile_0.pack( expand = TRUE, fill = BOTH )
        self.f_tile_0.grid_propagate(0)
        self.f_tile_0.pack_propagate(0)

        self.f_tile_1 = Frame( self.f_tiles, width = 80, height = 80, highlightthickness = 1, highlightbackground = style.c_text)
        self.l_tile_1 = Label( self.f_tile_1, text = "0001", foreground = style.c_blue, background = style.c_background )
        self.f_tile_1.grid(row = 0, column = 1, padx =10, pady=10)
        self.l_tile_1.pack( expand = TRUE, fill = BOTH )
        self.f_tile_1.grid_propagate(0)
        self.f_tile_1.pack_propagate(0)

        self.f_tile_2 = Frame( self.f_tiles, width = 80, height = 80, highlightthickness = 1, highlightbackground = style.c_text)
        self.l_tile_2 = Label( self.f_tile_2, text = "0002", foreground = style.c_blue, background = style.c_background )
        self.f_tile_2.grid(row = 1, column = 0, padx =10, pady=10)
        self.l_tile_2.pack( expand = TRUE, fill = BOTH )
        self.f_tile_2.grid_propagate(0)
        self.f_tile_2.pack_propagate(0)

        self.f_tile_3 = Frame( self.f_tiles, width = 80, height = 80, highlightthickness = 1, highlightbackground = style.c_text)
        self.l_tile_3 = Label( self.f_tile_3, text = "0003", foreground = style.c_blue, background = style.c_background )
        self.f_tile_3.grid(row = 1, column = 1, padx =10, pady=10)
        self.l_tile_3.pack( expand = TRUE, fill = BOTH )
        self.f_tile_3.grid_propagate(0)
        self.f_tile_3.pack_propagate(0)


        # SEM FRAME
        #----------
        self.tabControl = ttk.Notebook(self.f_main, width = ( 540 - (2 * style.p_padding) ), height = ( 220 - (2 * style.p_padding) ))#, background = c_frame, highlightthickness = 1, highlightbackground = c_high)

        self.tab1 = Frame(self.tabControl, width = ( 300 - (2 * style.p_padding) ), height = ( 200 - (2 * style.p_padding) ), background = style.c_button, highlightthickness = 1, highlightbackground = style.c_text )
        self.tab2 = Frame(self.tabControl, width = ( 300 - (2 * style.p_padding) ), height = ( 200 - (2 * style.p_padding) ), background = style.c_button, highlightthickness = 1, highlightbackground = style.c_text )
        self.tab3 = Frame(self.tabControl, width = ( 300 - (2 * style.p_padding) ), height = ( 200 - (2 * style.p_padding) ), background = style.c_button, highlightthickness = 1, highlightbackground = style.c_text )
        self.tab4 = Frame(self.tabControl, width = ( 300 - (2 * style.p_padding) ), height = ( 200 - (2 * style.p_padding) ), background = style.c_button, highlightthickness = 1, highlightbackground = style.c_text )

        self.tabControl.add(self.tab1, text ='Config')
        self.tabControl.add(self.tab2, text ='Packet')
        self.tabControl.add(self.tab3, text ='Inject Error')
        self.tabControl.add(self.tab4, text ='Bitstream')
        self.tabControl.pack_propagate(0)
        self.tabControl.grid( row = 1, column = 1, padx = style.p_padding, pady = style.p_padding )

#----------------------------------------------------------------------
# END OF CODE
