from gooey.IML.IML import construct_widgets
from gooey.app.CursesApplication import CursesApplication

from gooey.core import Model, Controller

model = Model()
controller = Controller(model)
widget = construct_widgets( 'toggle.iml', model, controller )

with CursesApplication( model, widget, controller ) as app:
    app.run()
