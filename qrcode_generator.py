# python3, GTK 3.0
import pyqrcode
import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk
from os import remove

qrcode_interface = \
    """
    <?xml version="1.0" encoding="UTF-8"?>
    <!-- Generated with glade 3.36.0 -->
    <interface>
      <requires lib="gtk+" version="3.22"/>
      <object class="GtkWindow" id="main">
        <property name="name">main</property>
        <property name="can_focus">False</property>
        <property name="title" translatable="yes">QRcode generator</property>
        <property name="resizable">False</property>
        <property name="default_width">440</property>
        <property name="default_height">500</property>
        <property name="icon">static\\icons\\QRcode_icon.png</property>
        <signal name="destroy" handler="on_main_destroy" swapped="no"/>
        <child>
          <object class="GtkBox">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="margin_top">5</property>
            <property name="orientation">vertical</property>
            <child>
              <object class="GtkBox">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">center</property>
                <property name="hexpand">True</property>
                <child>
                  <object class="GtkEntry" id="entry_link">
                    <property name="name">entry_link</property>
                    <property name="width_request">300</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <property name="hexpand">False</property>
                    <property name="placeholder_text" translatable="yes">URL</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="button_done">
                    <property name="label" translatable="yes">Done</property>
                    <property name="name">button_done</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <property name="hexpand">True</property>
                    <property name="border_width">5</property>
                    <signal name="clicked" handler="on_button_done_clicked" swapped="no"/>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkBox">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">center</property>
                <property name="hexpand">True</property>
                <child>
                  <object class="GtkRadioButton" id="theme_light">
                    <property name="label" translatable="yes">Theme Light</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="halign">center</property>
                    <property name="hexpand">True</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">True</property>
                    <signal name="toggled" handler="on_theme_light_toggled" swapped="no"/>
                    <style>
                      <class name="radio_theme"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="theme_dark">
                    <property name="label" translatable="yes">Theme Dark</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="halign">center</property>
                    <property name="hexpand">True</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">theme_light</property>
                    <signal name="toggled" handler="on_theme_dark_toggled" swapped="no"/>
                    <style>
                      <class name="radio_theme"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkImage" id="QRcode_img">
                <property name="name">Qrcode_photo</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
                <property name="hexpand">True</property>
                <property name="vexpand">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel" id="label">
                <property name="name">label</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">center</property>
                <property name="valign">end</property>
                <property name="margin_bottom">5</property>
                <property name="hexpand">True</property>
                <property name="vexpand">True</property>
                <property name="label" translatable="yes">QRcode generator (c)</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">3</property>
              </packing>
            </child>
          </object>
        </child>
        <child type="titlebar">
          <placeholder/>
        </child>
      </object>
    </interface>

    """

css_style_light = \
    b"""
    #main 
    { 
        background: #F6F5F4; 
    }
    #entry_link 
    { 
        background: #FCFCFC; color: #2E3436; 
    }
    #button_done 
    {
        background: #EDEBE9; 
        color: #2E3436; 
    }
    .radio_theme 
    { 
        color: #2E3436; 
    }
    #label 
    { 
        color: #2E3436;  
    }
    """

css_style_dark = \
    b"""
    #main 
    { 
        background: #36393F; 
    }
    #entry_link 
    {
        border-color: white; 
        background: #40444B; 
        font-size: 13px; 
        color: #FFFAFA; 
    }
    #button_done 
    { 
        background: #40444B; 
        color: #FFFAFA; 
    }
    .radio_theme 
    { 
        color: #FFFAFA; 
    }
    
    #label { color: #FFFAFA; font-size: 13px; }
    """


class Handler:
    def __init__(self):

        self.css_style(0)

        self.entry_link = builder.get_object('entry_link')
        self.button_generate = builder.get_object('button_done')
        self.QRcode_image = builder.get_object('QRcode_img')

    @staticmethod
    def on_main_destroy(button):
        print(button)
        Gtk.main_quit()

    @staticmethod
    def css_style(style):
        css = Gtk.CssProvider()
        css.load_from_data(css_style_dark if style == 1 else css_style_light)
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen.get_default(),
                                              css,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def on_button_done_clicked(self, button):
        print(button)

        try:
            remove('static\\QRcode_img\\QRcode.png')
        except FileNotFoundError:
            print("Image Error")

        url = self.entry_link.get_text()
        img = pyqrcode.create(url)
        img.png('static\\QRcode_img\\QRcode.png', scale=6)

        self.QRcode_image.set_from_file('static\\QRcode_img\\QRcode.png')

    def on_theme_light_toggled(self, radio):
        print(radio, "THEMA LIGHT")
        self.css_style(0)

    def on_theme_dark_toggled(self, radio):
        print(radio, "THEMA DARK")
        self.css_style(1)


if __name__ == "__main__":
    builder = Gtk.Builder()
    builder.add_from_string(qrcode_interface)
    builder.connect_signals(Handler())

    window = builder.get_object("main")
    window.show_all()

    Gtk.main()
