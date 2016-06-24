# IceWM desktop file extractor

Generates entries parseable by IceWM's menuprog command.

Parses [FreeDesktop.org .desktop and .directory][3] entries, trying to
have a very basic compliance with the [menu][2] spec. Uses [pyxdg][1]
for parsing.

Worked on under Ubuntu, on which it depends on `python-xdg`.

    sudo apt-get install python-xdg

## Usage

Use by adding the following to e.g. `${HOME}/.icewm/menu`, or perhaps to
`/etc/X11/icewm/menu` or maybe `/usr/share/icewm/menu`:

    menuprog "FD.o Programs" folder /path/to/icewm-desktop-files/icewm-desktop-files.py

You may also be interested in `icewm-menu-gnome2` from the [icewm-gnome-support][4] package, which does a similar thing.

> Copyright (c) 2015 Ivan Vucica
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
> 
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[1]: http://pyxdg.readthedocs.org/en/latest/desktopentry.html
[2]: http://standards.freedesktop.org/menu-spec/latest
[3]: http://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html
[4]: apt://icewm-gnome-support
