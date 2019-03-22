# -*- coding: utf8 -*-
#
# kerasin's travel dash & notifier
#

import sys
import ac
import acsys 

# TODO: suspension travel, gap to packers, tyre slip sounds

appWindow = 0

maxTravel_FL = 0
maxTravel_FR = 0
maxTravel_RL = 0
maxTravel_RR = 0
l_maxTravel_FL = 0
l_maxTravel_FR = 0
l_maxTravel_RL = 0
l_maxTravel_RR = 0



# This function gets called by AC when the Plugin is initialised
# The function has to return a string with the plugin name
def acMain(ac_version):
#    global longitudinalGIndicator, appWindow, lateralGIndicator
    global appWindow
    global l_maxTravel_FR, l_maxTravel_FL, l_maxTravel_RR, l_maxTravel_RL
    
    appWindow = ac.newApp("Travel dash")
    ac.setSize(appWindow, 200, 200)
    ac.drawBorder(appWindow, 0)
#    ac.setBackgroundOpacity(appWindow, 0)

    ac.console("Travel dash & notifier started. © kero 2019")

    l_maxTravel_FL = ac.addLabel(appWindow, "FL: 0");
    l_maxTravel_FR = ac.addLabel(appWindow, "FR: 0");
    l_maxTravel_RL = ac.addLabel(appWindow, "RL: 0");
    l_maxTravel_RR = ac.addLabel(appWindow, "RR: 0");
    ac.setPosition(l_maxTravel_FL, 3, 30)
    ac.setPosition(l_maxTravel_FR, 103, 30)
    ac.setPosition(l_maxTravel_RL, 3, 100)
    ac.setPosition(l_maxTravel_RR, 103, 100)

#    ac.setBackgroundTexture(appWindow,"apps/python/gMeter/gmeterBackground.png")
#    lateralGIndicator = GIndicator(appWindow,22,62,"Lat.")
#    longitudinalGIndicator = GIndicator(appWindow,22,136,"Lon.")
#    ac.addRenderCallback(appWindow , onFormRender)

    return "Travel dash"


def acUpdate(deltaT):
    global maxTravel_FR, maxTravel_FL, maxTravel_RR, maxTravel_RL
    global l_maxTravel_FR, l_maxTravel_FL, l_maxTravel_RR, l_maxTravel_RL
    
    travel_FL = ac.getCarState(0, acsys.CS.LapCount)
    
    if travel_FL > maxTravel_FL:
    maxTravel_FL = travel_FL
    ac.setText(l_maxTravel_FL, "FL: {}".format(maxTravel_FL))


