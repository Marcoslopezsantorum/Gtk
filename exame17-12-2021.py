import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk



class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 11-12-2021")
        self.set_border_width(10)

        solapas = Gtk.Notebook()


        lblTitulo = Gtk.Label(label="Configuración zoa de rego")
        lblActivada = Gtk.Label(label="Activada")
        lblHoraComezo = Gtk.Label(label="Hora de comezo")
        lblDuracionRego = Gtk.Label(label="Duración do Rego")

        swtActivada = Gtk.Switch()
        txtHoraComezo = Gtk.Entry()
        cmbDuracionRego = Gtk.ComboBox()
        btnAceptar = Gtk.Button(label="Aceptar")

        frmOpcions = Gtk.Frame(label="Opcións")
        chkAntixiada = Gtk.CheckButton(label="Antixiada")
        chkDiario = Gtk.CheckButton(label="Diario")
        chkChuvia = Gtk.CheckButton(label="Chuvia")





if __name__ == "__main__":
    Exame()
    Gtk.main()