"""
Plugin based on the base plugin
"""

from _baseModule import BaseClass, run as runBase

class Plugin2(BaseClass):
    """
    Plugin sub classing base class.
    """

    def __init__(self, *args, **kwargs):
        super(Plugin2, self).__init__(*args, **kwargs)

    def doCalc(self):
        self.kwargs['x'] += 2
        print "{0}: Adding 2 to x: {1}".format(self.__class__.__name__, self.kwargs['x'])
        return self.kwargs['x']

class Plugin3(BaseClass):
    """
    Plugin sub classing base class.
    """

    def __init__(self, *args, **kwargs):
        super(Plugin3, self).__init__(*args, **kwargs)

    def doCalc(self):
        print "{0}: x+4 is this '{1}' many xes".format(self.__class__.__name__,
                                                       'x'*(self.kwargs['x']+4))
        return self.kwargs['x']

