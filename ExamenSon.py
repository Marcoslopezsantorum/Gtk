import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 16-12-2021")
        self.set_border_width(10)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(caixaV)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        caixaV.add(caixaH)

        caixaV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixaH.add(caixaV2)


        imaxe = Gtk.Image()
        caixaV2.pack_start(imaxe, True, True, 0)
        imaxe.set_from_icon_name ("media-optical", Gtk.IconSize.DIALOG)

        chkAnimado= Gtk.CheckButton(label = "Animado")
        caixaV2.pack_start(chkAnimado, True, True, 0)

        tvwTaboa = Gtk.TreeView()
        tvwTaboa.set_size_request(420, 100)
        caixaH.pack_start(tvwTaboa, True, True, 0)

        grid = Gtk.Grid()
        caixaH.pack_start(grid, True, True, 0)

        btnReproducir = Gtk.Button(label = "Engadir a pista a reproducir")
        grid.add(btnReproducir)



        btnPausa = Gtk.Button(label = "Subir na lista")
        grid.attach_next_to(btnPausa, btnReproducir, Gtk.PositionType.BOTTOM, 1, 2)

        btnParar = Gtk.Button(label = "Baixar na lista")
        grid.attach_next_to(btnParar, btnPausa, Gtk.PositionType.BOTTOM, 1, 2)

        btnSaltar= Gtk.Button(label = "Saltar")

        caixaS = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        grid.attach_next_to(caixaS, btnParar, Gtk.PositionType.BOTTOM, 1, 1)
        caixaS.pack_start(btnSaltar, True, True, 0)

        modelo = Gtk.ListStore(int, str)
        modelo.append([1, "mp3"])
        modelo.append([2, "ovg"])
        modelo.append([3, "Brais"])
        modelo.append([4, "Joel"])
        modelo.append([5, "Hector"])

        cmbPosicionSaltar = Gtk.ComboBox.new_with_model_and_entry(modelo)
        cmbPosicionSaltar.connect("changed", self.on_cmbNomes_changed)
        cmbPosicionSaltar.set_entry_text_column(1)
        cmbNomesEntry = cmbPosicionSaltar.get_child()
        cmbNomesEntry.connect("activate", self.on_cmbNomesEntry_activate, modelo)


        caixaS.pack_start(cmbPosicionSaltar, True, True, 0)

        cmbPosicionSaltar.set_size_request(140, 10)

        btnAbrirFicheiro = Gtk.Button(label = "Abrir ficheiro...")
        grid.attach_next_to(btnAbrirFicheiro, caixaS, Gtk.PositionType.BOTTOM, 1, 2)
        btnFalarFicheiro = Gtk.Button (label = "Reproducir ficheiro...")
        grid.attach_next_to(btnFalarFicheiro, btnAbrirFicheiro, Gtk.PositionType.BOTTOM, 1, 2)
        btnGardarComo = Gtk.Button (label = "Gardar como...")
        grid.attach_next_to(btnGardarComo, btnFalarFicheiro, Gtk.PositionType.BOTTOM, 1, 2)
        btnEliminar = Gtk.Button (label = "Eliminar pista")
        grid.attach_next_to(btnEliminar, btnGardarComo, Gtk.PositionType.BOTTOM, 1, 2)


        contedorH2 = Gtk.Frame()
        contedorH2.set_label("Opcións de reproducción")




        chkAsincrono= Gtk.CheckButton(label = "Asíncrono")
        chkENomeFicheiro= Gtk.CheckButton(label = "É nome de ficheiro")
        chkXmlPersistente= Gtk.CheckButton(label = "XML persistente")
        chkFiltrarAntesReproducir= Gtk.CheckButton(label = "Filtrar antes de reproducir")
        chkExml= Gtk.CheckButton(label = "É XML")
        chkReproduccionNpl= Gtk.CheckButton(label = "Reproducción NPL")

        caixaH3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.btnAceptar = Gtk.Button(label="Aceptar")
        caixaH3.pack_end(self.btnAceptar, False, False, 0)
        self.btnCancelar = Gtk.Button(label="Cancelar")
        self.btnCancelar.connect("clicked", self.on_btnCancelar_clicked)
        caixaH3.pack_end(self.btnCancelar, False, False, 0)
        caixaV.pack_end(caixaH3, True, True, 0)


        builder = Gtk.Builder()
        builder.add_from_file("cadroSonGlade.glade")
        box1 = builder.get_object("boxExame")
        caixaV.pack_start(box1, True, True, 0)


        self.connect("destroy", Gtk.main_quit)
        self.show_all()
    def on_cmbNomes_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            id_fila, nome = modelo [fila][:2]
            idFila = modelo [fila][0]
            nome2 = modelo [fila][1]
            print("Extension: %s" %(nome))

    def on_cmbNomesEntry_activate(self,cadroTexto,modelo):
        print("Escribo: %s" % cadroTexto.get_text())
        modelo.append([10,cadroTexto.get_text()])

    def on_btnCancelar_clicked(self, boton):
            Gtk.main_quit()



if __name__=="__main__":

    Exame()
    Gtk.main()