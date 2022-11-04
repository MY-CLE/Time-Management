class Date(object):

    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def getDay(self) -> int:
        return self.__day

    def getMonth(self) -> int:
        return self.__month

    def getYear(self) -> int:
        return self.__year
