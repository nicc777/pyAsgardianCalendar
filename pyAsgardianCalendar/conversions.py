import datetime


class Gregorian:
    def __init__(self, input_datetime: datetime=None):
        if input_datetime is None:
            self.default_datetime = datetime.datetime.today()
            self.input_datetime = self.default_datetime
        elif isinstance(input_datetime, datetime.datetime):
            self.input_datetime = input_datetime
            self.default_datetime = input_datetime
        elif not isinstance(input_datetime, datetime.datetime):
            raise Exception('Input must be a Python datetime.datetime object')

    def get_day_number(self, input_datetime: datetime=None)->int:
        if not input_datetime:
            input_datetime = self.default_datetime
        return input_datetime.timetuple()[7]


class Asgardian:
    def __init__(self):
        self.asgardian_datetime = self.timetuple()

    def timetuple(self, input_gregorian_calendar: Gregorian=None)->tuple:
        """
        Looking to produce tm_year=2018, tm_mon=1, tm_mday=21, tm_hour=20, tm_min=44, tm_sec=22, tm_wday=6, tm_yday=21, tm_isdst=-1 - similar to Python's datetime

        :param input_gregorian_calendar: Gregorian object
        :return: a tuple similar to Python's datetime.timetuple object, but adapted for asgardian calendar
        """
        if not input_gregorian_calendar:
            input_gregorian_calendar = Gregorian()
        else:
            if not isinstance(input_gregorian_calendar, Gregorian):
                raise Exception('Input must be a Gregorian calendar type.')
        gregorian_tuple = input_gregorian_calendar.input_datetime.timetuple()
        asgardian_month_nr = int(input_gregorian_calendar.get_day_number()/28)
        if int(input_gregorian_calendar.get_day_number()%28) > 0:
            asgardian_month_nr = asgardian_month_nr + 1
        asgardian_mday = int(input_gregorian_calendar.get_day_number()%28)
        if asgardian_mday == 0:
            asgardian_mday = 1
        asgardian_tuple = (
            gregorian_tuple[0],
            asgardian_month_nr,
            asgardian_mday,
            gregorian_tuple[3],
            gregorian_tuple[4],
            gregorian_tuple[5],
            gregorian_tuple[6],
            gregorian_tuple[7],
            gregorian_tuple[8],
        )
        return asgardian_tuple

# EOF
