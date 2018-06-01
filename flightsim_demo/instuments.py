import datetime
import time
from math import sin

from gooey.app.CursesApplication import CursesApplication

from gooey.core import Model, Controller
from gooey.widgets.CompositeWidget import CompositeWidget

from MissionTimer import MissionTimer
from Altimeter import Altimeter
from ArtificialHorizon import ArtificialHorizon
from HeadingIndicator import HeadingIndicator
from Throttle import Throttle

class FlightSimController(Controller):
    def __init__(self, model):
        super().__init__(model)
        self.model.register('time')
        self.model.register('throttle')

        self.model.register('mode')
        self.model.update('mode', '*')

        self.model.register('above_horizon')

        self.model.register('roll')
        self.model.register('pitch')
        self.model.register('yaw')

        self.model.register('x')
        self.model.register('y')
        self.model.register('z')

    def update(self):
        t = datetime.datetime.now().time()
        self.model.update('time', t.isoformat())

        dt = time.time()

        throttle = int(50 * sin(dt / 24) + 50)
        self.model.update('throttle', throttle)

        roll = dt / 6
        self.model.update('roll', roll)

        above_horizon = int(10 * sin(dt / 5))
        self.model.update('above_horizon', above_horizon)

        x = int(49 * sin(dt / 25) + 50)
        self.model.update('x', x)
        y = int(49 * sin(dt / 26) + 50)
        self.model.update('y', y)
        z = int(49 * sin(dt / 27) + 50)
        self.model.update('z', z)
  

model = Model()
controller = FlightSimController(model)
widget = CompositeWidget(model, controller)

widget.add( MissionTimer(model, controller), (0,0), (200,200) )
widget.add( ArtificialHorizon(model, controller), (15,8), (200,200) )
widget.add( Altimeter(model, controller), (55,7), (200,200) )
widget.add( HeadingIndicator(model, controller), (15,30), (200,200) )
widget.add( Throttle(model, controller), (0,8), (200,200) )

with CursesApplication( model, widget, controller ) as app:
    app.run()
