# -*- coding: utf-8; -*-
"""
Copyright (C) 2007-2009 Lincoln de Sousa <lincoln@minaslivre.org>
Copyright (C) 2007 Gabriel Falcão <gabrielteratos@gmail.com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

__all__ = [
    'NAME', 'VERSION', 'IMAGE_DIR', 'GLADE_DIR', 'LOCALE_DIR',
    'GCONF_PATH', 'KEY', 'TERMINAL_MATCH_EXPRS', 'TERMINAL_MATCH_TAGS',
    'ALIGN_CENTER', 'ALIGN_RIGHT', 'ALIGN_LEFT',
    ]

NAME = 'guake'
VERSION = '0.4.4'
IMAGE_DIR = '/usr/local/share/pixmaps/' + NAME
GLADE_DIR = '/usr/local/share/' + NAME
LOCALE_DIR = '/usr/local/share/locale'

# Gconf stuff. Yep, it is hardcoded =)
GCONF_PATH = '/apps/guake'
KEY = lambda x: (GCONF_PATH+x)

# regular expressions to highlight links in terminal. This code was
# lovely stolen from the great gnome-terminal project, thank you =)
USERCHARS = "-[:alnum:]"
PASSCHARS = "-[:alnum:],?;.:/!%$^*&~\"#'"
HOSTCHARS = "-[:alnum:]"
HOST      = "[" + HOSTCHARS + "]+(\\.[" + HOSTCHARS + "]+)*"
PORT      = "(:[:digit:]{1,5})?"
PATHCHARS =  "-[:alnum:]_$.+!*(),;:@&=?/~#%"
SCHEME    = "(news:|telnet:|nntp:|file:/|https?:|ftps?:|webcal:)"
USER      = "[" + USERCHARS + "]+(:[" + PASSCHARS + "]+)?"
URLPATH   = "/[" + PATHCHARS + "]*[^]'.}>) \t\r\n,\\\"]"

TERMINAL_MATCH_EXPRS = [
  "\<" + SCHEME + "//(" + USER + "@)?" + HOST + PORT + "(" + URLPATH + ")?\>/?",
  "\<(www|ftp)[" + HOSTCHARS + "]*\." + HOST + PORT + "(" +URLPATH + ")?\>/?",
  "\<(mailto:)?[" + USERCHARS + "][" + USERCHARS + ".]*@[" + HOSTCHARS +
  "]+\." + HOST + "\>"
  ]

TERMINAL_MATCH_TAGS = 'schema', 'http', 'email'
ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT = range(3)
