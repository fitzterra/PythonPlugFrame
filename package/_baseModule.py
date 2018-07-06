"""
Base module defining the base plugin behaviour.

It contains the base class(es) and the main entry point (run() )
"""

class BaseClass(object):
    """
    The base class for all plugins to extend.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializer.

        Simply stores the args and keyword args locally. The subclasses can
        override this, or for a specific plugin type framework, this could be a
        more specific or formal initializer for that type of plugin system.

        The subclasses should normally call this via super:
            super(MyCalssName, self).__init__(kw, kwargs)
        """

        self.args = args
        self.kwargs = kwargs

    def execute(self):
        """
        The main plugin execute method to be called after instantiation.

        This method should be a generalized entrypoint for all plugins to do the
        work they are supposed. It will normally be called at some point after
        instantiation, and may be overridden by the subclass if needed.
        """
        # Do the work here
        return self.doCalc()

    def doCalc(self):
        """
        A sample method that should normally be overwridden by the subclass to
        do plugin specifc work.
        """
        raise NameError('Subclass should override this method')


def run(plugins):
    """
    Main module/plugin entry point.

    This would be called by the caller after importing the plugin package. The
    purpose of this function is to initialize all plugin classes, and then
    possibly calling their execute methods, but should really be tailored to
    handle the specific plugin system being developed.

    If this function is fairly generic across all plugin modules, all plugin
    modules can import this function and then do not have to write their own.

    Each plugin modeule **must** have this entry point function, or else it will
    not be seen as a plugin. The name of the module depends on the name supplied
    to the 'runName' arg to the getModules() function in the package __init__.py
    file.
    """

    # Initialize each plugin and execute it's main method.
    for pdef in plugins:
        p = pdef(x=3)
        p.execute()
