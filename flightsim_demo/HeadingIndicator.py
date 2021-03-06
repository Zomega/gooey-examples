#!/usr/bin/python
# -*- coding: utf-8 -*-

from gooey.core.widget import *

from gooey.core.canvas import *
from gooey.canvas.ascii_canvas import *
from gooey.canvas.ascii_sprite import *

from gooey.core.event import *
from gooey.core.event_type import *

SPRITE_CHARS = u'''
┌──┬──┬──┬──┬──┼──┬──┬──┬──┬──┐
│  07    08    09    10    11 │'''

SPRITE_FG_MASK = u'''
WWWWWWWWWWWWWWWRWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'''

SPRITE_BG_MASK = u'''
KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
KBBBBBBBBBBBBBBBBBBBBBBBBBBBBBK'''

SPRITE_ALTIMETER = AsciiSprite(SPRITE_CHARS, SPRITE_FG_MASK, SPRITE_BG_MASK)

class HeadingIndicator(Widget):
       
    def validate_canvas( self, canvas ):
        if not canvas.type == "AsciiCanvas":
            raise InvalidCanvasTypeError("ArtificialHorizons only support AsciiCanvases for now...")
        c_w, c_h = canvas.size
        s_w, s_h = SPRITE_ALTIMETER.size
        # TODO: Correct size.
        if not ( c_w >= s_w and c_h >= s_h ):
            raise InvalidCanvasSizeError("ArtificialHorizons need a larger canvas.")
        
    def handle_event( self, event ):
        return False
        
    def render( self ):      
        self.canvas.putsprite( (0,0),  SPRITE_ALTIMETER )
