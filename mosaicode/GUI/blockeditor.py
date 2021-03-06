#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noqa: E402
"""
This module contains the BlockEditor class.
"""
import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk
from gi.repository import GtkSource
from mosaicode.GUI.blocknotebook import BlockNotebook
from mosaicomponents.codefield import CodeField
from mosaicomponents.colorfield import ColorField
from mosaicomponents.combofield import ComboField
from mosaicomponents.commentfield import CommentField
from mosaicomponents.openfilefield import OpenFileField
from mosaicomponents.stringfield import StringField
from mosaicode.GUI.dialog import Dialog
from mosaicode.GUI.fieldtypes import *
from mosaicode.GUI.blockporteditor import BlockPortEditor
from mosaicode.GUI.blockcommoneditor import BlockCommonEditor
from mosaicode.GUI.blockpropertyeditor import BlockPropertyEditor
from mosaicode.GUI.blockcodeeditor import BlockCodeEditor
from mosaicode.system import System as System
import gettext

_ = gettext.gettext


class BlockEditor(Gtk.Dialog):
    """
    This class contains methods related the BlockEditor class
    """

    # ----------------------------------------------------------------------
    def __init__(self, block_manager, block):
        Gtk.Dialog.__init__(self, _("Block Editor"),
                            block_manager,
                            0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        self.block_manager = block_manager
        self.block = block
        self.set_default_size(800, 600)
        box = self.get_content_area()

        self.tabs = Gtk.Notebook()
        self.tabs.set_scrollable(True)
        box.pack_start(self.tabs, True, True, 0)

        self.tabs.append_page(BlockCommonEditor(self, self.block),
                    Gtk.Label(_("Common Properties")))
        self.tabs.append_page(BlockPropertyEditor(self, self.block),
                    Gtk.Label(_("Properties")))
        self.tabs.append_page(BlockPortEditor(self, self.block),
                    Gtk.Label(_("Ports")))
        self.tabs.append_page(BlockCodeEditor(self, self.block),
                    Gtk.Label(_("Code")))

        self.show_all()
        result = self.run()
        if result == Gtk.ResponseType.OK:
            self.block_manager.main_control.add_new_block(block)
            self.block_manager.update()
        self.close()
        self.destroy()

# ----------------------------------------------------------------------
