
import gi
import gridConBotons

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GLib

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de uso NoteBook")
        self.set_border_width(10)

        cartafol=Gtk.Notebook()

        paxina1 = Gtk.Box()
        paxina1.set_border_width(10)
        paxina1.add(Gtk.Label(label = "Paxina principal"))
        cartafol.append_page(paxina1, Gtk.Label(label="Identificador da paxina 1"))

        paxina2 = Gtk.Box()
        paxina2.set_border_width(10)
        paxina2.add(Gtk.Label(label="Paxina con imaxe na lapela"))
        cartafol.append_page(paxina2, Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))

        CaixaConBotons = gridConBotons.CaixaConBotons()
        cartafol.append_page(CaixaConBotons, Gtk.Label(label = "Grid con Botons"))


        self.add(cartafol)



        self.connect ("destroy", Gtk.main_quit)
        self.show_all()





if __name__ =="__main__":
    Aplicacion()
    Gtk.main()