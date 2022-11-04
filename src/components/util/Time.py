class Time(object):

    def __init__(self, hour: int, minute: int, second: int):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def getHour(self) -> int:
        return self.__hour

    def getMinute(self) -> int:
        return self.__minute

    def getSecond(self) -> int:
        return self.__second
