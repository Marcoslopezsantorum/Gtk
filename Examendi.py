import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 15-12-2021")
        self.set_border_width(10)



        cuadricula = Gtk.Grid()
        self.add(caixaH)



        lblNome = Gtk.Label(label = "Nome:")
        txtNome= Gtk.Entry()
        lblApelido = Gtk.Label(label="Apelido:")
        lblTratamento = Gtk.Label(label="Tratamento:")
        txtTratamento= Gtk.Entry()
        txtApelido = Gtk.Entry()
        lblFormato = Gtk.Label(label="Formato:")
        btnBoton5 = Gtk.ComboBoxText()

        lblNomeUsuario = Gtk.Label(label="Nome de Usuario:")
        txtNomeUsuario = Gtk.Entry()
        cuadricula.add(lblNome)
        cuadricula.attach(txtNome, 1, 0, 1, 1)  # para posicionar el boton donde quieras
        cuadricula.attach_next_to(lblTratamento, lblNome, Gtk.PositionType.BOTTOM, 1, 1)
        cuadricula.attach(txtTratamento, 1, 1, 1, 1)  # FORMA ABSOLUTA
        cuadricula.attach_next_to(lblFormato, lblTratamento, Gtk.PositionType.BOTTOM, 1, 1)
        cuadricula.attach_next_to(btnBoton5, txtTratamento, Gtk.PositionType.BOTTOM, 3, 2)  # Forma Relativa
        cuadricula.attach_next_to(lblApelido, txtNome, Gtk.PositionType.RIGHT, 1, 1)
        cuadricula.attach_next_to(txtApelido, lblApelido, Gtk.PositionType.RIGHT, 1, 1)
        cuadricula.attach_next_to(lblNomeUsuario, lblApelido, Gtk.PositionType.BOTTOM, 1, 1)
        cuadricula.attach_next_to(txtNomeUsuario, txtApelido, Gtk.PositionType.BOTTOM, 1, 1)

        builder = Gtk.Builder()
        builder.add_from_file("cadroCorreoGlade.glade")
        caixaGlade = builder.get_object("caixaGlade")

        caixaH.pack_start(caixaGlade, True, True, 0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__=="__main__":

    Exame()
    Gtk.main()