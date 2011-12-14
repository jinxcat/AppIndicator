import pygtk
pygtk.require('2.0')
import gtk

have_appindicator = True
try:
    import appindicator
except:
    have_appindicator = False

class MyIndicator:
   
    ## global variables
    isAboutOpen = False

    ## functions to handle events    
    def quit(self, widget, data=None):
        gtk.main_quit()
       
    ## Handles about menu choice
    def about_response(self, w, param):
        if self.isAboutOpen == False:
            self.isAboutOpen = True
            ## Show about window
            # actually show a constructed window
            ## MAKE CERTAIN that the isAboutOpen property is set to False when the window is destroyed!
            print param


    ## Initialise
    def __init__(self):
        ## Create appindicator object
        if have_appindicator:
            self.ind = appindicator.Indicator ("example-simple-client",
                        "indicator-messages",
                        appindicator.CATEGORY_APPLICATION_STATUS)
            self.ind.set_status (appindicator.STATUS_ACTIVE)
            self.ind.set_attention_icon ("new-messages-red")
            self.ind.set_icon("distributor-logo")
        else:
            self.ind = gtk.status_icon_new_from_stock(gtk.STOCK_HOME)
        
        ## Create menu object
        self.menu = gtk.Menu()
    
        ## Add menu items below 
        
        ## About
        menuItemAbout = gtk.MenuItem('About')
        menuItemAbout.connect("activate", self.about_response, "About")
        self.menu.append(menuItemAbout)
    
        ## Quit
        menuItemQuit = gtk.MenuItem('Quit')
        menuItemQuit.connect('activate', self.quit)
        self.menu.append(menuItemQuit)
    
        ## Show all in menu (instead of calling .show() for each item)
        self.menu.show_all()

        ## Add constructed menu as indicator menu
        self.ind.set_menu(self.menu)   
    
def main():
    gtk.main()
    return 0

if __name__ == "__main__":
   indicator = MyIndicator()
   main()
