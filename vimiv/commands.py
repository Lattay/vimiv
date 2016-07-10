#!/usr/bin/env python
# encoding: utf-8
""" Contains all commands and functions for vimiv """
from vimiv.tags import TagHandler

class Commands(object):
    """ Creates the commands for vimiv """

    def __init__(self, vimiv):
        self.vimiv = vimiv
        self.vimiv.tag_handler = TagHandler(vimiv)

        # Dictionary with command names and the corresponding functions
        self.vimiv.commands = {
            "accept_changes": [self.vimiv.button_clicked, "w", True],
            "autorotate": [self.vimiv.rotate_auto],
            "center": [self.vimiv.center_window],
            "clear_trash": [self.vimiv.clear, 'Trash'],
            "clear_thumbs": [self.vimiv.clear, 'Thumbnails'],
            "command": [self.vimiv.focus_cmd_line],
            "delete": [self.vimiv.delete],
            "discard_changes": [self.vimiv.button_clicked, "w", False],
            "first":  [self.vimiv.move_pos, False],
            "first_lib":  [self.vimiv.move_pos_lib, False],
            "fit": [self.vimiv.zoom_to, 0],
            "fit_horiz": [self.vimiv.zoom_to, 0, True, False],
            "fit_vert": [self.vimiv.zoom_to, 0, False, True],
            "flip": [self.vimiv.flip],
            "format": [self.vimiv.format_files],
            "grow_lib": [self.vimiv.resize_lib, None, True],
            "last":  [self.vimiv.move_pos, True],
            "last_lib":  [self.vimiv.move_pos_lib, True],
            "library": [self.vimiv.toggle_library],
            "focus_library": [self.vimiv.focus_library, True],
            "unfocus_library": [self.vimiv.focus_library, False],
            "manipulate": [self.vimiv.toggle_manipulate],
            "mark": [self.vimiv.mark],
            "mark_all": [self.vimiv.mark_all],
            "mark_between": [self.vimiv.mark_between],
            "toggle_mark": [self.vimiv.toggle_mark],
            "move_up": [self.vimiv.move_up],
            "next": [self.vimiv.move_index, True, True],
            "next!": [self.vimiv.move_index, True, True, 1, True],
            "optimize": [self.vimiv.cmd_edit, 'opt'],
            "prev": [self.vimiv.move_index, False, True],
            "prev!": [self.vimiv.move_index, False, True, 1, True],
            "q": [self.vimiv.quit],
            "q!": [self.vimiv.quit, True],
            "reload_lib": [self.vimiv.reload, '.'],
            "rotate": [self.vimiv.rotate],
            "set animation!": [self.vimiv.toggle_animation],
            "set brightness": [self.vimiv.cmd_edit, 'bri'],
            "set contrast": [self.vimiv.cmd_edit, 'con'],
            "set library_width": [self.vimiv.resize_lib],
            "set overzoom!": [self.vimiv.toggle_vars.toggle_overzoom],
            "set rescale_svg!": [self.vimiv.toggle_vars.toggle_rescale_svg],
            "set sharpness": [self.vimiv.cmd_edit, 'sha'],
            "set show_hidden!": [self.vimiv.toggle_hidden],
            "set slideshow_delay": [self.vimiv.set_slideshow_delay],
            "set statusbar!": [self.vimiv.toggle_statusbar],
            "shrink_lib": [self.vimiv.resize_lib, None, False],
            "slideshow": [self.vimiv.toggle_slideshow],
            "slideshow_inc": [self.vimiv.set_slideshow_delay, 2, "+"],
            "slideshow_dec": [self.vimiv.set_slideshow_delay, 2, "-"],
            "tag_load": [self.vimiv.tag_handler.tag_load],
            "tag_remove": [self.vimiv.tag_handler.tag_remove],
            "tag_write": [self.vimiv.tag_handler.tag_write, self.vimiv.marked],
            "thumbnail": [self.vimiv.toggle_thumbnail],
            "zoom_in": [self.vimiv.zoom_delta, +.25],
            "zoom_out": [self.vimiv.zoom_delta, -.25],
            "zoom_to": [self.vimiv.zoom_to]}

        self.vimiv.functions = {"focus_bri": [self.vimiv.focus_slider, "bri"],
            "focus_con": [self.vimiv.focus_slider, "con"],
            "focus_sha": [self.vimiv.focus_slider, "sha"],
            "slider_dec": [self.vimiv.change_slider, True, False],
            "slider_inc": [self.vimiv.change_slider, False, False],
            "slider_dec_large": [self.vimiv.change_slider, True, True],
            "slider_inc_large": [self.vimiv.change_slider, False, True],
            "cmd_history_up": [self.vimiv.history, False],
            "cmd_history_down": [self.vimiv.history, True],
            "discard_command": [self.vimiv.cmd_line_leave],
            "complete": [self.vimiv.cmd_complete],
            "down": [self.vimiv.scroll, "j"],
            "down_lib": [self.vimiv.scroll_lib, "j"],
            "down_page": [self.vimiv.scroll, "J"],
            "left": [self.vimiv.scroll, "h"],
            "left_lib": [self.vimiv.scroll_lib, "h"],
            "left_page": [self.vimiv.scroll, "H"],
            "right": [self.vimiv.scroll, "l"],
            "right_lib": [self.vimiv.scroll_lib, "l"],
            "right_page": [self.vimiv.scroll, "L"],
            "up": [self.vimiv.scroll, "k"],
            "up_lib": [self.vimiv.scroll_lib, "k"],
            "up_page": [self.vimiv.scroll, "K"],
            "search": [self.vimiv.cmd_search],
            "search_next": [self.vimiv.search_move, 1],
            "search_prev": [self.vimiv.search_move, 1, False],
            "fullscreen": [self.vimiv.toggle_fullscreen.toggle]}

        self.vimiv.functions.update(self.vimiv.commands)
