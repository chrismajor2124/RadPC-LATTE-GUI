#!/usr/bin/python

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   RadPC SEM GUI, Rev. 1
#   Created by Chris Major
#   9/9/2020
#   Main Python program to open the Matoran Generator GUI
#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# LIBRARIES
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk 


# VARIABLES
#--------------------------------------------------------------------------------------------------------------------------------------------

c_test = "#FF8000"

c_back = "#222222"
c_frame = "#111111"
c_tile = "#1F1F1F"

c_high = "#F0F0F0"

c_green = "#31BF5C"
c_red = "#FF0000"
c_blue = "#0066CC"
c_gray = "#7F7F7F"

padding = 10


# CLASSES
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create an Application (App) Object
class App( object ):

    # Initialize
    def __init__( self, master ):

        # Set the GUI title and size
        master.title( "RadPC - Device Monitor Tool" )
        master.geometry( "900x600" )
        master.resizable(0, 0)


        # MAIN FRAME
        #------------
        self.f_main = Frame( master, width = 900, height = 600, background = c_back )
        self.f_main.pack()
        self.f_main.grid_propagate(0)


        # Large Serial Frame
        #------------
        self.f_ser = Frame( self.f_main, width = ( 900 - (2 * padding) ), height = ( 300 - (2 * padding) ), background = c_frame, highlightthickness = 1, highlightbackground = c_high )
        self.f_ser.grid( row = 0, column = 0, columnspan = 3, padx = padding, pady = padding )
        self.f_ser.pack_propagate(0)
        
        self.s_serial = scrolledtext.ScrolledText( self.f_ser, background = c_frame, state = "disabled", foreground = c_green, height = ( 300 - (2 * padding) ), relief = "solid", wrap = WORD ) 
        self.s_serial.vbar.config( troughcolor = c_frame, background = c_frame )
        self.s_serial.pack( fill = BOTH ) 
        self.s_serial.insert( INSERT, "SEM" )

        """
       
        """


        # STATS FRAME
        #------------
        self.f_stats = Frame( self.f_main, width = ( 300 - (2 * padding) ), height = ( 200 - (2 * padding) ), background = c_frame, highlightthickness = 1, highlightbackground = c_high )
        self.f_stats.pack_propagate(0)
        self.f_stats.grid( row = 1, column = 0, padx = padding, pady = padding )

        # Timer
        self.l_time = Label( self.f_stats, text = "TIME: 000:00:00:00", anchor = "w", background = c_frame, foreground = c_high )
        self.l_time.pack( fill = BOTH, padx = 5, pady = 5 ) 

        # AD2 Status
        self.l_AD2 = Label( self.f_stats, text = "Analog Discovery 2 offline", anchor = "w", background = c_frame, foreground = c_gray )
        self.l_AD2.pack( fill = BOTH, padx = 5, pady = 5 ) 

        # AD2 Status
        self.l_XHWS = Label( self.f_stats, text = "HW_SERVER is offline", wraplength = 240, anchor = "w", background = c_frame, foreground = c_gray )
        self.l_XHWS.pack( fill = BOTH, padx = 5, pady = 5 ) 


        # Tiles Frame
        #-------------
        self.f_tiles = Frame( self.f_main, width = ( 240 ), height = ( 240 ), background = c_frame, highlightthickness = 1, highlightbackground = c_high )
        self.f_tiles.grid_propagate(0)
        self.f_tiles.grid( row = 1, column = 1, padx = padding, pady = padding )
        
        # Tiles
        self.f_tile_0 = Frame( self.f_tiles, width = 100, height = 100, highlightthickness = 1, highlightbackground = c_high)
        self.l_tile_0 = Label( self.f_tile_0, text = "0000", foreground = c_blue, background = c_tile )
        self.f_tile_0.grid(row = 0, column = 0, padx =10, pady=10)
        self.l_tile_0.pack( expand = TRUE, fill = BOTH )
        self.f_tile_0.grid_propagate(0)
        self.f_tile_0.pack_propagate(0)
        
        self.f_tile_1 = Frame( self.f_tiles, width = 100, height = 100, highlightthickness = 1, highlightbackground = c_high)
        self.l_tile_1 = Label( self.f_tile_1, text = "0001", foreground = c_blue, background = c_tile )
        self.f_tile_1.grid(row = 0, column = 1, padx =10, pady=10)
        self.l_tile_1.pack( expand = TRUE, fill = BOTH )
        self.f_tile_1.grid_propagate(0)
        self.f_tile_1.pack_propagate(0)

        self.f_tile_2 = Frame( self.f_tiles, width = 100, height = 100, highlightthickness = 1, highlightbackground = c_high)
        self.l_tile_2 = Label( self.f_tile_2, text = "0002", foreground = c_blue, background = c_tile )
        self.f_tile_2.grid(row = 1, column = 0, padx =10, pady=10)
        self.l_tile_2.pack( expand = TRUE, fill = BOTH )
        self.f_tile_2.grid_propagate(0)
        self.f_tile_2.pack_propagate(0)

        self.f_tile_3 = Frame( self.f_tiles, width = 100, height = 100, highlightthickness = 1, highlightbackground = c_high)
        self.l_tile_3 = Label( self.f_tile_3, text = "0003", foreground = c_blue, background = c_tile )
        self.f_tile_3.grid(row = 1, column = 1, padx =10, pady=10)
        self.l_tile_3.pack( expand = TRUE, fill = BOTH )
        self.f_tile_3.grid_propagate(0)
        self.f_tile_3.pack_propagate(0)

        
        
        
        # SEM FRAME
        #----------
        self.tabControl = ttk.Notebook(self.f_main, width = ( 300 - (2 * padding) ), height = ( 200 - (2 * padding) ))#, background = c_frame, highlightthickness = 1, highlightbackground = c_high)
        
        self.tab1 = Frame(self.tabControl, width = ( 300 - (2 * padding) ), height = ( 200 - (2 * padding) ), background = c_frame, highlightthickness = 1, highlightbackground = c_high ) 
        self.tab2 = Frame(self.tabControl, width = ( 300 - (2 * padding) ), height = ( 200 - (2 * padding) ), background = c_frame, highlightthickness = 1, highlightbackground = c_high )
        self.tab3 = Frame(self.tabControl, width = ( 300 - (2 * padding) ), height = ( 200 - (2 * padding) ), background = c_frame, highlightthickness = 1, highlightbackground = c_high )
        self.tab4 = Frame(self.tabControl, width = ( 300 - (2 * padding) ), height = ( 200 - (2 * padding) ), background = c_frame, highlightthickness = 1, highlightbackground = c_high )
  
    
        self.tabControl.add(self.tab1, text ='Config')
        self.tabControl.add(self.tab2, text ='Packet')
        self.tabControl.add(self.tab3, text ='Inject Error')
        self.tabControl.add(self.tab4, text ='Bitstream')
        self.tabControl.pack_propagate(0)
        self.tabControl.grid( row = 1, column = 2, padx = padding, pady = padding )
        
        
        
        #POWER TAB
        #-----------------
        # Heartbeat
        self.b_status = Button( self.tab1, text ="Heartbeat", width = 20) #, command = lambda: send_command('S') )
        self.b_status.config( background = c_frame, foreground = c_high )
        self.b_status.grid(row=0, column = 0, pady = 5, padx = 5 )
        
        #reset MCU
        self.b_rMCU = Button( self.tab1, text ="Reset MCU", width = 20) #, command = lambda: send_command('S') )
        self.b_rMCU.config( background = c_frame, foreground = c_high )
        self.b_rMCU.grid(row=1, column = 0, pady = 5, padx = 5)
        
        #Reset FPGA
        self.b_rFPGA = Button( self.tab1, text ="Reset FPGA", width = 15) #, command = lambda: send_command('S') )
        self.b_rFPGA.config( background = c_frame, foreground = c_high )
        self.b_rFPGA.grid(row=1, column = 1, pady = 5)
        
        #configure fpga
        self.b_cFPGA = Button( self.tab1, text ="Config FPGA", width = 20) #, command = lambda: send_command('R 00') )
        self.b_cFPGA.config( background = c_frame, foreground = c_high )
        self.b_cFPGA.grid(row=2, column = 0, padx = 5, pady = 5 )
        
        #config N
        self.e_cN = Entry(self.tab1, width=17)
        self.e_cN.config( background = c_frame, foreground = c_high )
        self.e_cN.grid(row=2, column = 1, pady = 5 )
        
        self.chk_FPGA_pow = BooleanVar() #this variable will show FPGA power as on or off as a boolean
        self.FPGA_pow_box = Checkbutton(self.tab1, text='28V FPGA',var=self.chk_FPGA_pow, bg = c_frame, fg = c_high, activebackground='black', activeforeground='white',selectcolor="black")
        self.FPGA_pow_box.grid(row = 3, column = 0)

        self.chk_DOS_pow = BooleanVar()
        self.DOS_pow_box = Checkbutton(self.tab1, text='28V DOS',var=self.chk_DOS_pow, bg = c_frame, fg = c_high, activebackground='black', activeforeground='white',selectcolor="black")
        self.DOS_pow_box.grid(row = 3, column = 1)
        
        self.chk_TMS_pow = BooleanVar()
        self.TMS_pow_box = Checkbutton(self.tab1, text='28V TMS',var=self.chk_TMS_pow, bg = c_frame, fg = c_high, activebackground='black', activeforeground='white',selectcolor="black")
        self.TMS_pow_box.grid(row = 4, column = 0)
        
        
        #PACKET TAB
        #----------------------
        # Send current packet
        self.b_sCur = Button( self.tab2, text ="Send Current", width = 20 ) #, command = lambda: send_command('S') )
        self.b_sCur.config( background = c_frame, foreground = c_high )
        self.b_sCur.grid(row=0, column = 0, padx = 5, pady = 5 )
        
        # Store packet
        self.b_store = Button( self.tab2, text ="Store", width = 15) #, command = lambda: send_command('S') )
        self.b_store.config( background = c_frame, foreground = c_high )
        self.b_store.grid(row=0, column = 1, pady = 5 )

        # Send All Packets
        self.b_sAll = Button( self.tab2, text ="Send All", width = 20 ) #, command = lambda: send_command('I') )
        self.b_sAll.config( background = c_frame, foreground = c_high )
        self.b_sAll.grid(row=1, column = 0, padx = 5, pady = 5 )
        
        # Create Fake Packet
        self.b_cFake = Button( self.tab2, text ="Create Fake", width = 15 ) #, command = lambda: send_command('N C0000000010') )
        self.b_cFake.config( background = c_frame, foreground = c_high )
        self.b_cFake.grid(row=1, column = 1, pady = 5 )

        #Send Packet Num
        self.b_sNum = Button( self.tab2, text ="Send Packet Num", width = 20 ) #, command = lambda: send_command('O') )
        self.b_sNum.config( background = c_frame, foreground = c_high )
        self.b_sNum.grid(row=2, column = 0, pady = 5 )
        
        #packet number entry for send packet num
        self.e_sNum = Entry(self.tab2, width=17)
        self.e_sNum.config( background = c_frame, foreground = c_high )
        self.e_sNum.grid(row=2, column = 1, pady = 5 )

        # Send N Packets
        self.b_sNPac = Button( self.tab2, text ="Send N", width = 20) #, command = lambda: send_command('R 00') )
        self.b_sNPac.config( background = c_frame, foreground = c_high )
        self.b_sNPac.grid(row=3, column = 0, padx = 5, pady = 5 )
        
        #number of packets entry for send N packet
        self.e_sNPac = Entry(self.tab2, width=17)
        self.e_sNPac.config( background = c_frame, foreground = c_high )
        self.e_sNPac.grid(row=3, column = 1, pady = 5 )
        
        # Send New Packets
        self.b_sNew = Button( self.tab2, text ="Send New", width = 20) #, command = lambda: send_command('R 00') )
        self.b_sNew.config( background = c_frame, foreground = c_high )
        self.b_sNew.grid(row=4, column = 0, padx = 5, pady = 5 )
        
        #toggle packet storage
        self.toggle_packet_storage = BooleanVar()
        self.toggle_packet_storage = Checkbutton(self.tab2, text='Toggle Storage',var=self.chk_TMS_pow, bg = c_frame, fg = c_high, activebackground='black', activeforeground='white',selectcolor="black")
        self.toggle_packet_storage.grid(row=4, column = 1)
        
        #INJECT ERROR TAB
        #-----------
        #Inject Tile Error 
        self.b_sNum = Button( self.tab3, text ="Inject Tile Error", width = 20 ) #, command = lambda: send_command('O') )
        self.b_sNum.config( background = c_frame, foreground = c_high )
        self.b_sNum.grid(row=0, column = 0, pady = 5 )
        
        #combobox for selection of which tile
        self.FPGA_Tile_Err = ttk.Combobox(self.tab3, width=15)
        self.FPGA_Tile_Err['values']=[0,1,2,3]
        self.FPGA_Tile_Err.current(0)
        #self.FPGA_Tile_Err.config(background = c_frame, foreground = c_high ) having problems with changing color here
        self.FPGA_Tile_Err.grid(row=0, column = 1, pady = 5 )

        # Inject SEM Error
        self.b_sNPac = Button( self.tab3, text ="Inject SEM Error", width = 20) #, command = lambda: send_command('R 00') )
        self.b_sNPac.config( background = c_frame, foreground = c_high )
        self.b_sNPac.grid(row=1, column = 0, padx = 5, pady = 5 )
    
        
        
        
        #BITSTREAM TAB
        #----------------
        
        # Load Bitstream
        self.b_lBs = Button( self.tab4, text ="Load Bitsream" ) #, command = lambda: send_command('S') )
        self.b_lBs.config( background = c_frame, foreground = c_high )
        self.b_lBs.pack( fill = BOTH, anchor = "center", padx = 5, pady = 5 )

        # Bitstream Retrieve
        self.b_rBs = Button( self.tab4, text ="Bitstream Retrieve" ) #, command = lambda: send_command('I') )
        self.b_rBs.config( background = c_frame, foreground = c_high )
        self.b_rBs.pack( fill = BOTH, anchor = "center", padx = 5, pady = 5 )

        # Clear Flash memory
        self.b_cFm = Button( self.tab4, text ="Clear Flash Memory" ) #, command = lambda: send_command('O') )
        self.b_cFm.config( background = c_frame, foreground = c_high )
        self.b_cFm.pack( fill = BOTH, anchor = "center", padx = 5, pady = 5 )



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# END OF CODE