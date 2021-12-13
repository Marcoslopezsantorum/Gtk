import gi
import gridConBotons
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo combobox")
        self.set_border_width(5)
        self.set_default_size(500,250)

        modelo = Gtk.ListStore (int,str)
        modelo.append([3, "Marcos"])
        modelo.append([2, "Angel"])
        modelo.append([1, "Manuel"])
        modelo.append([19, "Alexander"])
        modelo.append([8, "Joel"])
        modelo.append([4, "Britza"])

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        cmbNomes = Gtk.ComboBox.new_with_model_and_entry(modelo)
        cmbNomes.connect("changed", self.on_cmbNomes_changed)
        cmbNomes.set_entry_text_column(1)
        cmbNomesEntry = cmbNomes.get_child()
        cmbNomesEntry.connect("activate", self.on_cmbNomesEntry_activate, modelo)
        # celda = Gtk.CellRendererText()
        # cmbNomes.pack_start(celda, True)
        # cmbNomes.add_attribute(celda, "text", 1)
        caixaV.pack_start(cmbNomes, False, False, 0)
        self.add(caixaV)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_cmbNomes_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            id_fila, nome = modelo[fila][:2]
            id_fila= modelo [fila][0]
            nome2 = modelo [fila][1]
            print("Seleccionado: ID=%d, nome= %s" % (id_fila, nome))
        # else:
        # cadroTexto = combo.get_child()
        # print("Escrito: %s" % cadroTexto.get_text())

    def on_cmbNomesEntry_activate(self, cadroTexto, modelo):
        print("Escrito: %s" % cadroTexto.get_text())
        modelo.append([10,cadroTexto.get_text()])

if __name__=="__main__":
    Aplicacion()
    Gtk.main()