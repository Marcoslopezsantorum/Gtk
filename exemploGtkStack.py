import gi
import gridConBotons

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de uso Stack e StackSwitcher")
        self.set_border_width(5)

        caixaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(caixaV)

        panel = Gtk.Stack()
        panel.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        panel.set_transition_duration(2000)

        pulsame = Gtk.CheckButton(label = "tocame ;)")
        panel.add_titled(pulsame, "Púlsame",  "paso1")

        etiqueta =  Gtk.Label()
        etiqueta.set_markup ("<big>Unha etiqueta presuntuosa</big>")
        panel.add_titled(etiqueta, "Etiqueta", "paso2")

        casa = gridConBotons.CaixaConBotons()
        panel.add_titled(casa, "Etiqueta", "paso3")

        selector_paneis = Gtk.StackSwitcher()
        selector_paneis.set_stack(panel)

        caixaV.pack_start(selector_paneis, True,True,0)
        caixaV.pack_start(panel,True,True,0)


        self.connect ("destroy", Gtk.main_quit)
        self.show_all()





if __name__ =="__main__":
    Aplicacion()
    Gtk.main()