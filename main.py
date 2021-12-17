import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 15-12-2021")
        self.set_border_width(10)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(caixaV)

        grid = Gtk.Grid()
        caixaV.pack_start(grid, True, True, 0)
        lblNome = Gtk.Label(label="Nome:")
        grid.add(lblNome)
        txtNome = Gtk.Entry()
        grid.attach_next_to(txtNome, lblNome, Gtk.PositionType.RIGHT, 1, 1)

        lblApelido = Gtk.Label(label="Apelido:")
        grid.attach_next_to(lblApelido, txtNome, Gtk.PositionType.RIGHT, 1, 1)
        txtApelido = Gtk.Entry()
        grid.attach_next_to(txtApelido, lblApelido, Gtk.PositionType.RIGHT, 1, 1)
        lblNomeUsuario = Gtk.Label(label="Nome de Usuario:")
        grid.attach_next_to(lblNomeUsuario, lblApelido, Gtk.PositionType.BOTTOM, 1, 1)
        lblTratamento = Gtk.Label(label="Tratamento:")
        grid.attach_next_to(lblTratamento, lblNome, Gtk.PositionType.BOTTOM, 1, 1)
        lblFormato = Gtk.Label(label="Formato:")
        grid.attach_next_to(lblFormato, lblTratamento, Gtk.PositionType.BOTTOM, 1, 1)

        txtTratamento = Gtk.Entry()
        grid.attach_next_to(txtTratamento, lblTratamento, Gtk.PositionType.RIGHT, 1, 1)

        txtNomeUsuario = Gtk.Entry()
        grid.attach_next_to(txtNomeUsuario, lblNomeUsuario, Gtk.PositionType.RIGHT, 1, 1)

        modelo = Gtk.ListStore(int, str)
        modelo.append([1, "pdf"])
        modelo.append([2, "docx"])
        modelo.append([3, "odt"])
        modelo.append([4, "texto"])

        cmbFormato = Gtk.ComboBox.new_with_model_and_entry(modelo)
        cmbFormato.connect("changed", self.on_cmbNomes_changed)
        cmbFormato.set_entry_text_column(1)
        cmbNomesEntry = cmbFormato.get_child()
        cmbNomesEntry.connect("activate", self.on_cmbNomesEntry_activate, modelo)

        grid.attach_next_to(cmbFormato, lblFormato, Gtk.PositionType.RIGHT, 3, 1)

        builder = Gtk.Builder()
        builder.add_from_file("cadroCorreoGlade.glade")
        caixaGlade = builder.get_object("box1")
        btnEngadir = builder.get_object("btnEngadir")
        entryCorreo = builder.get_object("txtDireccionCorreo")
        textCorreos = builder.get_object("txvListaCorreos")
        self.bufer = textCorreos.get_buffer()
        btnEngadir.connect("clicked", self.on_btnEngadir_clicked, entryCorreo, textCorreos)
        caixaV.pack_start(caixaGlade, True, True, 0)


        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.btnAceptar = Gtk.Button(label="Aceptar")
        caixaH.pack_end(self.btnAceptar, False, False, 0)
        self.btnCancelar = Gtk.Button(label="Cancelar")
        self.btnCancelar.connect("clicked", self.on_btnCancelar_clicked)
        caixaH.pack_end(self.btnCancelar, False, False, 0)
        caixaV.add(caixaH)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_cmbNomes_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            id_fila, nome = modelo[fila][:2]
            print("%s" % (nome))

    def on_cmbNomesEntry_activate(self, cadroTexto, modelo):
        print("Escrito: %s" % cadroTexto.get_text())
        modelo.append([10, cadroTexto.get_text()])

    def on_btnCancelar_clicked(self, boton):
        Gtk.main_quit()

    def on_btnEngadir_clicked(self, boton, entryCorreo, textCorreos):
        punteiro = self.bufer.get_end_iter()
        self.bufer.insert(punteiro, entryCorreo.get_text() + "\n")


    def cambio(self, control):
        print(control.get_active_text())

if __name__ == "__main__":
    Exame()
    Gtk.main()
