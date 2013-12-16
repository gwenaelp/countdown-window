#!/usr/bin/env python

import pygtk
pygtk.require('2.0')

import gobject
import gtk
import args
import sys
import commands


class App:

    def destroy(self, widget, data=None):
        print("destroy signal occurred")
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)

        self.window.set_keep_above(True)
        self.window.show()

        vbox = gtk.VBox()
        vbox.show()
        self.window.add(vbox)

        t = args.get().message
        if t is None:
            t = "Remaining time :"

        self.text = gtk.Label(t)
        self.text.show()
        vbox.pack_start(self.text, False, True)

        self.text_countdown = gtk.Label("text_countdown")
        self.text_countdown.show()
        vbox.pack_start(self.text_countdown, False, True)

        self.cancel_button = gtk.Button("Cancel")
        self.cancel_button.connect("clicked", self.cancel_clicked)
        self.cancel_button.show()
        vbox.pack_start(self.cancel_button, False, True)

        pos = args.get().position
        if pos is not None:
            pos = pos.split(",")

            x = int(pos[0])
            y = int(pos[1])

            self.window.move(x, y)

        self.counter = int(args.get().countdown)
        gobject.timeout_add_seconds(1, self.countdown_refresh)

    def countdown_refresh(self):
        if self.counter > 0:
            self.counter -= 1
            self.text_countdown.set_text(str(self.counter))
            gobject.timeout_add_seconds(1, self.countdown_refresh)
        else:
            self.text_countdown.set_text("All done!")
            commands.getstatusoutput(args.get().command)
            gtk.main_quit()

    def cancel_clicked(self, sender):
        gtk.main_quit()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    theme = args.get().theme
    if theme is not None:
        gtk.rc_parse(theme)

    app = App()
    app.main()

    sys.exit(args.get().command)
