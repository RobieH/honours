from numpy import linspace
import holopy as hp
from holopy.core import Optics
from holopy.propagation import propagate
from holopy.core.tests.common import get_example_data
from holopy.core import load

#holo = get_example_data('image0001.yaml')
#rec_vol = propagate(holo, linspace(4e-6, 10e-6, 7))
#hp.show(rec_vol)

optics = hp.core.Optics(wavelen=.660, index=1.33,
                        polarization=[1.0, 0.0])
holo = hp.core.load('newredblood2.png',spacing=7.6,optics=optics)
rec_vol = propagate(holo, linspace(1e-3,5e-2,100))
hp.show(holo)
hp.show(rec_vol)
