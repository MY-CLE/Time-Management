from src.components.util.Date import *
from src.components.util.Time import *


class CalendarEvent(object):

    def __init__(self, startDate: Date, endDate: Date,
                 startTime: Time, endTime: Time,
                 comment: str):
        self.__startDate = startDate
        self.__endDate = endDate
        self.__startTime = startTime
        self.__endTime = endTime
        self.__comment = comment

    def getStartDate(self) -> Date:
        return self.__startDate

    def setStartDate(self, startDate: Date) -> None:
        self.__startDate = startDate

    def getEndDate(self) -> Date:
        return self.__endDate

    def setEndDate(self, endDate: Date) -> None:
        self.__endDate = endDate

    def getStartTime(self) -> Time:
        return self.__startTime

    def setStartTime(self, startTime: Time) -> None:
        self.__startTime = startTime

    def getEndTime(self) -> Time:
        return self.__endTime

    def setEndTime(self, endTime: Time) -> None:
        self.__endTime = endTime

    def getComment(self) -> str:
        return self.__comment

    def setComment(self, comment: str) -> None:
        self.__comment = comment
