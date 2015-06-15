from gooey.core.Widget import Widget
from gooey.core.FocusableWidget import *
from gooey.widgets.CompositeWidget import CompositeWidget

from gooey.core.Exceptions import UnhandledEventException

import logging

class FocusWidget(FocusableWidget):
    def __init__(self, model, controller):
        FocusableWidget.__init__(self, model, controller)
        
    def validate_canvas( self, canvas ):
        if not canvas.type == "AsciiCanvas":
            raise InvalidCanvasTypeError("ArtificialHorizons only support AsciiCanvases for now...")
        
    def handle_event( self, event ):
        raise UnhandledEventException()
    
    @property    
    def _width( self ):
        return self.canvas.size[0]
        
    @property    
    def _height( self ):
        return self.canvas.size[1]
        
    def render( self ):      
        if self.focused:
            self.canvas.paint_rect( (0,0), (self.canvas.size[0]-1,self.canvas.size[1]-1), bg_color = 'Y' )
        else:
            self.canvas.paint_rect( (0,0), (self.canvas.size[0]-1,self.canvas.size[1]-1), bg_color = 'B' )
            
    def best_focus_location( self, focus_metric ):
        best_metric = None
        best_location = None
        width, height = self.size
        for x in range(width):
            for y in range(height):
                metric = focus_metric((x,y))
                if best_metric == None or metric < best_metric:
                    best_metric = metric
                    best_location = (x,y)
        return best_location
                    
            
from gooey.app.CursesApplication import CursesApplication

from gooey.core import Model, Controller

model = Model()
controller = Controller(model)
widget = CompositeWidget(model, controller)

widget.add( FocusWidget(model, controller), (0,0), (10,10) )
widget.add( FocusWidget(model, controller), (11,11), (21,21) )
widget.add( FocusWidget(model, controller), (0,11), (10,21) )
widget.add( FocusWidget(model, controller), (11,0), (21,10) )

with CursesApplication( model, widget, controller ) as app:
    app.run()
            
