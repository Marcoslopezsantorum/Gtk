import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk



class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 11-12-2021")
        self.set_border_width(10)

        noteBook = Gtk.Notebook()
        self.add(noteBook)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        noteBook.append_page(caixaV, Gtk.Label(label="Zoa1"))



        grid = Gtk.Grid()
        caixaV.pack_start(grid, True, True, 0)

        lblTitulo = Gtk.Label(label="Configuración zoa de rego")
        lblActivada = Gtk.Label(label="Activada")
        lblHoraComezo = Gtk.Label(label="Hora de comezo")
        lblDuracionRego = Gtk.Label(label="Duración do Rego")
        swtActivada = Gtk.Switch()
        swtActivada.connect("notify::active", self.on_btnBotonAbrir_clicked)
        txtHoraComezo = Gtk.Entry()
        cmbPosicionSaltar = Gtk.ComboBox()

        modelo = Gtk.ListStore(int, str)
        modelo.append([1, "5 min"])
        modelo.append([2, "10 min"])
        modelo.append([3, "20 min"])
        modelo.append([4, "30 min"])
        modelo.append([5, "60 min"])

        cmbPosicionSaltar = Gtk.ComboBox.new_with_model_and_entry(modelo)
        cmbPosicionSaltar.connect("changed", self.on_cmbNomes_changed)
        cmbPosicionSaltar.set_entry_text_column(1)
        cmbNomesEntry = cmbPosicionSaltar.get_child()
        cmbNomesEntry.connect("activate", self.on_cmbNomesEntry_activate, modelo)



        cmbPosicionSaltar.set_size_request(140, 10)




        btnAceptar = Gtk.Button(label="Aceptar")
        frmOpcions = Gtk.Frame(label="Opcións")
        chkAntixiada = Gtk.CheckButton(label="Antixiada")
        chkDiario = Gtk.CheckButton(label="Diario")
        chkChuvia = Gtk.CheckButton(label="Chuvia")

        grid.add(lblTitulo)
        grid.attach_next_to(lblActivada, lblTitulo, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(lblHoraComezo, lblActivada, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(lblDuracionRego, lblHoraComezo, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(swtActivada, lblActivada, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(txtHoraComezo, lblHoraComezo, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(cmbPosicionSaltar, lblDuracionRego, Gtk.PositionType.RIGHT, 1, 2)

        grid.attach_next_to(frmOpcions, lblDuracionRego, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(chkAntixiada, frmOpcions, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(chkDiario, chkAntixiada, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(chkChuvia, chkDiario, Gtk.PositionType.RIGHT, 1, 1)


        builder = Gtk.Builder()
        builder.add_from_file("cadroDiasGlade.glade")
        caixaGlade = builder.get_object("frame1")
        caixaV.pack_start(caixaGlade, True, True, 0)

        #caixaH = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # btnBoton = Gtk.Button(label = "Etiqueta")
        # btnBoton = Gtk.Button.new_with_label("Etiqueta")

        #btnBotonAbrir = Gtk.Button.new_with_mnemonic("_Abrir")  # atajo al+a
        #btnBotonAbrir.connect("clicked", self.on_btnBotonAbrir_clicked)
        #caixaH.pack_start(btnBotonAbrir, True, True, 0)

        #caixaV.add(caixaH)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixaV.add(caixaH)

        # btnBoton = Gtk.Button(label = "Etiqueta")
        # btnBoton = Gtk.Button.new_with_label("Etiqueta")

        btnBotonAbrir = Gtk.Button.new_with_mnemonic("Aceptar")  # atajo al+a
        btnBotonAbrir.connect("clicked", self.on_btnBotonAbrir_clicked)
        caixaH.pack_end(btnBotonAbrir, False, False, 0)











        panel = Gtk.Stack()
        etiqueta = Gtk.Label()
        panel.add_titled(etiqueta, "Etiqueta", "Zoa1")

        selector_paneis = Gtk.StackSwitcher()
        selector_paneis.set_stack(panel)



        self.connect("destroy", Gtk.main_quit)
        self.show_all()


    def on_cmbNomes_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            id_fila, nome = modelo [fila]
            print("Extension: %s" %(nome))

    def on_cmbNomesEntry_activate(self,txtHoraComezo,modelo):
        punteiro = self.bufer.get_end_iter()
        self.bufer.insert(punteiro, txtHoraComezo.get_text() + "\n")


    def on_btnEngadir_clicked(self, boton, entryCorreo, textCorreos):
        punteiro = self.bufer.get_end_iter()
        self.bufer.insert(punteiro, entryCorreo.get_text() + "\n")

    def on_btnBotonAbrir_clicked(self , boton, estado):
            print("O boton 'Activada' Esta activado")

    def on_btnBotonActivado_clicked(self, control):
            print("Activado")


if __name__ == "__main__":
    Exame()
    Gtk.main()