"""
Generalized plugin package initialization and support functions.
"""

import os
import importlib
import inspect

def getModules(runName="run", ofClass=None):
    """
    Dynamically imports all modules within this package, and tries to find the
    module entry point function, and optionally any class definitions that are
    subclasses of a base class(es).

    Only modules in the package that have a .py extension and does **not** start
    with an underscore (_) will be imported. It is a good idea then for the base
    module name to start with an underscore, to avoid wasting resources also
    importing that : i.e. _baseModule.py

    Args:
        runName (str): the name of the main entry point in the module. This
            function could do anything module wide to set up the plugin, or to
            run it, or whatever. Default is a function called "run"
        ofClass (class): if supplied, all classes in the module will be tested
            to see if the class is a subclass of this base class. If so, all
            these class members will be returned in a list. The caller may use
            this as needed.

    Returns: a dictionary with module (plugin) names as keys, and a details of
        the found members as:
            {
              'module' : {
                "runName": reference to function in module or None
                "subClass": [reference(s) to subclass(es) of base] (possibly empty)
              }
            }
    """
    # Container dict for all modules found with a runName function
    modules = {}
    
    # Cycle through all python files, excluding any starting with '_' in this
    # package dir
    for f in os.listdir(os.path.dirname(__file__)):
        # Split into module name and extension
        mod_name, ext = os.path.splitext(f)
        # Must be a .py file and not start with '_'
        if ext != '.py' or mod_name.startswith('_'):
            continue
        # Import the module relative to the current package
        mod = importlib.import_module("."+mod_name, __package__)

        # Cycle through all members in the module, looking for the entry point
        # function and subclasses if needed
        members = {'runName': None, 'subClass': []}
        for obj_name, obj in inspect.getmembers(mod):
            # The .getmembers() method returns a tuple with the first element
            # the full member name , and the second the member definition.
            
            # Check for our entry function if we have not found it yet
            if members['runName'] is None and \
                    inspect.isfunction(obj) and \
                    obj.__name__ == runName:
                members['runName'] = obj
                continue

            # Check for any subclasses
            if ofClass is not None and \
                    inspect.isclass(obj) and \
                    issubclass(obj, ofClass) and \
                    obj != ofClass:
                members['subClass'].append(obj)
                continue

        # Only add this module if we found a runName
        if members['runName'] is not None:
            modules[mod_name] = members

    return modules
