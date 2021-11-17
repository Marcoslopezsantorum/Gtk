
import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GLib

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de uso Gtk.Grid")
        self.set_border_width(5)

        cartafol=Gtk.Notebook()

        paxina1 = Gtk.Box()
        paxina1.set_border_width(10)


        self.connect ("destroy", Gtk.main_quit)
        self.show_all()





if __name__ =="__main__":
    Aplicacion()
    Gtk.main()