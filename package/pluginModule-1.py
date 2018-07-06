"""
Plugin based on the base plugin
"""

from _baseModule import BaseClass, run as runBase

class Plugin1(BaseClass):
    """
    Plugin sub classing base class.
    """

    def __init__(self, *args, **kwargs):
        super(Plugin1, self).__init__(*args, **kwargs)

    def doCalc(self):
        self.kwargs['x'] *= 2
        print "{0}: doubling x to: {1}".format(self.__class__.__name__, self.kwargs['x'])
        return self.kwargs['x']

