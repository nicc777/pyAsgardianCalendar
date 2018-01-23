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
    def __init__(self, input_gregorian_calendar: Gregorian=None):
        if not input_gregorian_calendar:
            self.input_gregorian_calendar = Gregorian()
        elif isinstance(input_gregorian_calendar, Gregorian):
            self.input_gregorian_calendar = input_gregorian_calendar
        else:
            self.input_gregorian_calendar = Gregorian()
        self.asgardian_datetime = self.timetuple()

    def timetuple(self, input_gregorian_calendar: Gregorian=None)->tuple:
        """
                                  0            1          2           3          4          5           6          7            8
        Looking to produce tm_year=2018, tm_mon=1, tm_mday=21, tm_hour=20, tm_min=44, tm_sec=22, tm_wday=6, tm_yday=21, tm_isdst=-1 - similar to Python's datetime

        Differences to Python datetime.timetuple():

            tm_mon -> Asgardian month (range 1 to 13)
            tm_mday -> Asgardian month day (range 1 to 28)
            tm_wday -> Asgardian week day (range 1 to 7, 1=Sunday) - will align this in the next round...

        :param input_gregorian_calendar: Gregorian object
        :return: a tuple similar to Python's datetime.timetuple object, but adapted for asgardian calendar
        """
        if not input_gregorian_calendar:
            input_gregorian_calendar = self.input_gregorian_calendar
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
        # TODO align asgardian_wday so that 0 = Monday...
        asgardian_wday = int(input_gregorian_calendar.get_day_number()%7)
        if asgardian_wday == 0:
            asgardian_wday = 7
        asgardian_tuple = (
            gregorian_tuple[0],
            asgardian_month_nr,
            asgardian_mday,
            gregorian_tuple[3],
            gregorian_tuple[4],
            gregorian_tuple[5],
            asgardian_wday,
            gregorian_tuple[7],
            -1,
        )
        return asgardian_tuple

    def __str__(self):
        t = self.timetuple()
        if t[1] > 9:
            month_str = str(t[1])
        else:
            month_str = '0{}'.format(str(t[1]))
        if t[2] > 9:
            day_str = str(t[2])
        else:
            day_str = '0{}'.format(str(t[2]))
        return 'Asgardian date: {}-{}-{}'.format(t[0], month_str, day_str)

# EOF
