from CalendarEvent import *
from ApprovalState import *


class Vacation(CalendarEvent):

    def __init__(self, startDate: Date, endDate: Date, startTime: Time, endTime: Time, comment: str,
                 approvalState: ApprovalState):
        super().__init__(startDate, endDate, startTime, endTime, comment)
        self.__approvalState = approvalState

    def getApprovalState(self) -> ApprovalState:
        return self.__approvalState

    # todo
    def vacation(self, startDate: Date, endDate: Date) -> None:

