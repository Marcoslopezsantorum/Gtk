import gi
import gridConBotons
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo gladeintento")
        self.set_border_width(5)
        self.set_default_size(500,250)

        caixaV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL)
        self.add (caixaV)

        caixaH = Gtk.Box (orientation = Gtk.Orientation.HORIZONTAL)
        lblId = Gtk.Label(label = "Id :")
        caixaH.pack_start(lblId, True,True,2)
        txtId=Gtk.Entry()
        caixaH.pack_start(txtId, True,True,2)
        caixaV.pack_start(caixaH, True, True, 2)


        lblApariencia = Gtk.Label()
        lblApariencia.set_markup("<b>Appearance</b>")
        lblApariencia.props.xalign = 0
        caixaV.pack_start(lblApariencia,True,True,2)


        rede = Gtk.Grid()
        caixaV.pack_start(rede,True,True,0)
        lblEtiqueta = Gtk.Label()
        lblEtiqueta.set_markup("<i>Etiqueta</i>")
        rede.add(lblEtiqueta)

        caixa = Gtk.Box (orientation = Gtk.Orientation.HORIZONTAL)
        txvEtiqueta= Gtk.TextView()
        txvEtiqueta.set_size_request(300,50)
        caixa.pack_start(txvEtiqueta,True, True, 0)

        btnEditarEtiqueta = Gtk.Button()
        imaxe = Gtk.Image.new_from_icon_name('preferences-other', Gtk.IconSize.BUTTON)
        btnEditarEtiqueta.set_image(imaxe)
        caixa.pack_start(btnEditarEtiqueta,True,False,0)
        rede.attach_next_to(caixa,lblEtiqueta,Gtk.PositionType.RIGHT,3,2)

        rbtAtributos = Gtk.RadioButton(label = "Atributos:")
        rede.attach(rbtAtributos,0,2,1,1)
        btnEditarAtributos = Gtk.Button(label="Editar atributos")
        rede.attach_next_to(btnEditarAtributos,rbtAtributos,Gtk.PositionType.RIGHT,3,1)


        rbtUsarMarcado = Gtk.RadioButton (label="Usar marcado")
        rede.attach(rbtUsarMarcado,0,3,2,1)


        rbtPatron = Gtk.RadioButton(label = "Patrón")
        rede.attach(rbtPatron,0,4,1,1)
        txtPatron = Gtk.Entry()
        rede.attach(txtPatron,2,4,2,1)


        lblComportamentoEtiqueta = Gtk.Label(label = "Comportamento da etiqueta")
        lblComportamentoEtiqueta.set_markup("<b>Comportamento de etiqueta</b>")
        lblComportamentoEtiqueta.props.xalign = 0
        caixaV.pack_start(lblComportamentoEtiqueta,False,False,0)

        grid = Gtk.Grid()
        caixaV.pack_start(grid,True,True,0)
        chkSeleccionable = Gtk.CheckButton(label ="Seleccionable")
        grid.add(chkSeleccionable)
        chkUtilizarSubraiado = Gtk.CheckButton (label= "Utilizar Subraiado")
        grid.attach_next_to(chkUtilizarSubraiado,chkSeleccionable,Gtk.PositionType.BOTTOM,1,1)




        self.connect("destroy",Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    Aplicacion()
    Gtk.main()