#!/usr/bin/env python
import package
from package._baseModule import BaseClass


plugList = package.getModules(ofClass=BaseClass)
for plugName, plugInfo in plugList.items():
    print "Plugin module: ", plugName
    runFunc = plugInfo['runName']
    plugins = plugInfo['subClass']
    runFunc(plugins)
