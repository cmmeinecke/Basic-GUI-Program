#GUI Program by Caitlin Meinecke CST 150

#Import tkinter to create GUI widgets
import tkinter

#Create the main frame for the GUI program
class MyGUI(tkinter.Frame):
    def __init__(self):
        #Create the main window widget
        self.window = tkinter.Tk()

        #Create frame for diplaying info
        self.frame = tkinter.Frame(self.window, width=500, height=40, padx=40, pady=25)
        self.frame.grid(row=5)
        #Info to display in the GUI program
        self.name = '\tCaitlin Meinecke\n\t274 Bally Drive\n\tWaynesville, NC 27999'

        #Create labels
        self.label1 = tkinter.Label(self.frame)

        #Elements in a grid view
        self.label1.grid(row=0, column=1)

        #Show info button
        self.info_button = tkinter.Button(self.frame, text="Show Info", command=self.show_info)
        self.info_button.grid(row=8, column=1, padx=40, pady=25)
        
        #Create quit button
        self.quit = tkinter.Button(self.frame, text='Quit', command=self.quit_window)
        self.quit.grid(row=8, column=4, padx=40, pady=25)

        #run the mainloop
        self.window.mainloop()

    #create method to display name and address in label
    def show_info(self):
        self.label1['text'] = self.name

    #Create method to close the window using destroy function
    def quit_window(self):
        self.window.destroy()
        
#Create an instance of the MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()
