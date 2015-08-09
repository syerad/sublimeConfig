#!/usr/bin/python
# -*- coding: utf-8 -*-
###########################################################
# Import of used python modules
###########################################################
import sublime
import sublime_plugin
import re
import json
import os.path
import TrackYourTime.projectClass

# import sqlite3
from time import time
from datetime import date, datetime, timedelta
from threading import Timer
###########################################################
# vars
###########################################################

settings = None
interval = None
dbFilePath = sublime.packages_path() + "/TrackYourTime/tytDB.json"
dbFile = None
view = None
view_date = None

###########################################################
# helperFunctions
###########################################################

# *********************************************************
# set the actions to do after sublime has loaded this plugin
# *********************************************************


def plugin_loaded():
    sublime.status_message(
        "TrackYourTime was succesfully loaded! Ready for tracking!")
    init()

# *********************************************************
# init function. Check for existing JSON's and setting
# up the environment for using this plugin
# *********************************************************


def init():
    # global settings
    settings = sublime.load_settings(
        'TrackYourTime.sublime-settings')
    # get interval from config and convert it from minutes to seconds
    interval = int(settings.get('interval', 5)) * 60
    setupDB()
    # if plugin is not enabled don't track the time
    if settings.get('enabled', False) == False:
        return None
    # save the current timeStamp and some related metadata
    saveTimeObject()
    # global interval

    # test = sublime.packages_path() + "/TrackYourTime/tytDB.json"
    # sublime.message_dialog(settings)
    # print(test)

# *********************************************************
# saves the current Time incl. some metadata to the right
# Object in datastorage
# *********************************************************


def saveTimeObject():
    # get the project name
    projName = getProjectName()
    # get the current timeStamp
    timeStamp = getTimestamp()
    proj = TrackYourTime.projectClass.Project(projName, "timeStamp", "calenderWeek", "month")
    print(proj.name)
    # proof if the proj is already defined in the Json storage


# *********************************************************
# open the existing dbFile or create a new one if no
# file exists
# *********************************************************


def setupDB():
    dbFile = open(dbFilePath, "a+")


# *********************************************************
# placeholder tbd
# *********************************************************
def getDailyTrack():
    pass


# *********************************************************
# placeholder tbd
# *********************************************************
def getTimestamp():


def getProjectName():
    window = sublime.active_window()
    proj = window.project_file_name()
    proj = re.findall("\w*\W\w*\W\w*$", proj)
    proj = re.match("(\w*)\.", proj[0])
    proj = proj.group(1)
    return proj


###########################################################
# SublimeCommands
###########################################################


class TrackYourTimeDailyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        string = getDailyTrack()
        show(self.view.window(), edit, string)
