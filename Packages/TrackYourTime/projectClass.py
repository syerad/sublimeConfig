#!/usr/bin/python
# -*- coding: utf-8 -*-
###########################################################
# Import of used python modules
###########################################################
import re
import json


# a sublime Project
class Project(object):

    ###########################################################
    # vars
    ###########################################################

    ###########################################################
    # methods
    ###########################################################

    def __init__(self, name, timeStamp, calenderWeek, month):
        self._name = name
        self._timeStamp = timeStamp
        self._calenderWeek = calenderWeek
        self._month = month


###########################################################
# getters and setters
###########################################################

    @property
    def name(self):
        """I'm the 'x' property."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name
