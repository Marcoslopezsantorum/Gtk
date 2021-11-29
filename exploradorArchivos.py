import gi
import gridConBotons
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo explorador de archivos")
        self.set_border_width(5)
        self.set_default_size(500,250)

        area = Gtk.FlowBox()
        bDesprazamento=Gtk.ScrolledWindow()
        bDesprazamento.add(area)
        self.add(bDesprazamento)

        with os.scandir ('.') as elementos:
            for elemento in elementos:
                caixa = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 0)
                tipo = "folder" if elemento.is_dir() else   "text-x-generic"
                icono = Gio.ThemedIcon(name=tipo)
                imaxe = Gtk.Image.new_from_gicon(icono,Gtk.IconSize.DIALOG)

                caixa.pack_start(imaxe, True, True,0)
                caixa.pack_start(Gtk.Label(label  = elemento.name), True, True, 0)
                area.add(caixa)


        self.connect("destroy",Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    Aplicacion()
    Gtk.main()