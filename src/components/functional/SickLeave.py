from CalendarEvent import *


class SickLeave(CalendarEvent):

    def __init__(self, startDate: Date, endDate: Date,
                 startTime: Time, endTime: Time, comment: str):
        super().__init__(startDate, endDate, startTime, endTime, comment)

    #todo
    def sickLeave(self, startDate: Date) -> None:


