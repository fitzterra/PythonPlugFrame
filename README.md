Python Basic Plugin Framework Template
======================================

**NOTE**: This is still concept phase... and may never get out ;-)

Abstract
--------
This repo is the initial template for creating a very simple **Plugin
Framework** for Python to satisfy the following features and functionality:
* All plugins are contained within one python _package_
* All plugins extends a base _class_ that is contained inside a base _module_ in
  the package
* The plugin is a _module_ file inside the _package_, but each _plugin module_
  may contain one or more subclasses of the _base plugin class_
* Each _plugin module_ has a main entry point which is a function that may be
  called to instantiate and _"execute"_ the plugin class(es) in that module
* Introspection are used to enable plugins to _auto register_ by just being
  present as a module inside the package

Structure
---------
An example structure (file layout and main members) for this plugin package
framework could be:

```
package/
├── __init__.py
│   └── def getModules()
│
├── _baseModule.py
│   ├── class BaseClass()
│   └── def run()
│
├── pluginModule-1.py
│   ├── class Plugin1(BaseClass)
│   └── def run()
│
└── pluginModule-2.py
    ├── class Plugin2(BaseClass)
    └── def run()
```

Auto-registration
-----------------
The auto registration functionality is via calling the `package.getModules()`
function.

This function expects these arguments:
* **`runName`** : The name of the plugin module's main entry point. It defaults
  to "`run`" if not supplied, and must be a function in the module. Only if this
  function exists in a module will the module be registered as an available
  plugin.
* **`ofClass`** : If not None, this should be a reference to the base class
  defined in the base module. All modules in the package that have been
  registered via their `runName` function being present, will be searched for
  class defintions that have this class as base class.

The return from package.getModules() will be a dictionary (refering to
[structure](#structure) above for names) :
```python
{
    'pluginModule-1': {
        'runName': <package.pluginModule-1.run>,
        'ofClass': [<package.pluginModule-1.Plugin1>] # or empty if ofClass==None
    },
    'pluginModule-2': {
        'runName': <package.pluginModule-2.run>,
        'ofClass': [<package.pluginModule-2.Plugin2>] # or empty if ofClass==None
    }
}
```

Note that module files with names starting with `_` are ignored when searching
for plugin modules.

Usage
-----
The idea would be to import the plugin package, run it's `getModules()` function
to return a structure describing all plugin modules, with their entry point
functions and optionally any plugin classes that are sub classes of a base
class.

With this information the caller can use the plugins in any way needed.

The framework as describe is very open and informally structured. It should be
easily adaptable for many situations, and can be made more specific for specific
situations.

