from CalendarEvent import *
from ApprovalState import *


class Workday(CalendarEvent):

    # todo: replace None type in parameters startDate & endDate with useful values.
    def __init__(self, startTime: Time, endTime: Time, comment: str, approvalState: ApprovalState):
        super().__init__(None, None, startTime, endTime, comment)
        self.__approvalState = approvalState

    def getApprovalState(self) -> ApprovalState:
        return self.__approvalState
