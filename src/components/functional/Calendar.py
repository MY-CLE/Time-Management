from CalendarEvent import *


class Calendar(object):

    def __init__(self):
        self.__calendarEvents = None

    def getCalendarEvents(self) -> list:
        return self.__calendarEvents

    def addMultipleCalendarEvents(self, calendarEvents: list) -> None:
        self.__calendarEvents += calendarEvents

    def addCalendarEvent(self, calendarEvent: CalendarEvent) -> None:
        self.__calendarEvents.append(calendarEvent)


