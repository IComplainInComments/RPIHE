#Raspberry Pi Hardware Encoder
#For Licensing Info see: LICENSE
#For usage/tech see: README.md

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class RPIHEGUI(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="RPIHE")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Start")
        button.connect("clicked", self.on_start_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Stop")
        button.connect("clicked", self.on_stop_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Quit")
        button.connect("clicked", self.on_quit_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_start_clicked(self, button):
        print("Staring encoding procedure")
    def on_stop_clicked(self, button):
        print("Terminating current encode...")
    def on_quit_clicked(self, button):
        print("Terminating Program...")
        Gtk.main_quit()


win = RPIHEGUI()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
