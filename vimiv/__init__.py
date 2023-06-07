"""vimiv: An image viewer with vim-like keybindings.

License:

    Copyright (c) 2023 Théo Cavignac
    Copyright (c) 2015 Christian Karl
    Copyright (c) 2010 James Campos

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

__version__ = "0.9.2.dev2"
__license__ = "MIT"
__author__ = "Christian Karl"
__maintainer__ = "Théo Cavignac"
__email__ = "theo.cavignac+dev@gmail.com"

try:
    from gi import require_version
    require_version("Gtk", "3.0")
    try:
        require_version("GExiv2", "0.10")
    # No EXIF support
    except ValueError:
        pass
    from gi.repository import GLib, Gtk, Gdk, GdkPixbuf, Pango

except ImportError as import_error:
    message = import_error.msg + "\n" + "Are all dependencies installed?"
    raise ImportError(message) from import_error
