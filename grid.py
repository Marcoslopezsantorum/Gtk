
import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GLib

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de uso Gtk.Grid")



        cuadricula = Gtk.Grid()
        self.add (cuadricula)

        btnBoton1 = Gtk.Button(label="Boton 1 ")
        btnBoton2 = Gtk.Button(label="Boton 2 ")
        btnBoton3 = Gtk.Button(label="Boton 3 ")
        btnBoton4 = Gtk.Button(label="Boton 4 ")
        btnBoton5 = Gtk.Button(label="Boton 5 ")
        btnBoton6 = Gtk.Button(label="Boton 6 ")

        cuadricula.add(btnBoton1)
        cuadricula.attach(btnBoton2,1,0,2,1) #para posicionar el boton donde quieras
        cuadricula.attach_next_to(btnBoton3, btnBoton1, Gtk.PositionType.BOTTOM,1,2)
        cuadricula.attach(btnBoton4,1,1, 2,1) #FORMA ABSOLUTA
        cuadricula.attach_next_to(btnBoton5,btnBoton4, Gtk.PositionType.BOTTOM, 1, 1)#Forma Relativa
        cuadricula.attach(btnBoton6,2,2,1,1 )



        builder = Gtk.Builder()
        builder.add_from_file("cadroGlade.glade")
        caixaGlade = builder.get_object ("caixaGlade")

        cuadricula.pack_start(caixaGlade, True, True, 0)

        self.connect ("destroy", Gtk.main_quit)
        self.show_all()


if __name__ =="__main__":
    Aplicacion()
    Gtk.main()