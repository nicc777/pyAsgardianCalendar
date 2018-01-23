# pyAsgardianCalendar

The Asgardian Calendar conversion library in Python (unofficial)

At the moment this is a quick and dirty hack. If there is enough interest, I'll develop it further.

# Quick Start

    >>> from pyAsgardianCalendar.conversions import Asgardian, Gregorian
    >>> import datetime
    >>> g = Gregorian(input_datetime=datetime.datetime(2018, 2, 19))
    >>> a = Asgardian(input_gregorian_calendar=g)
    >>> a.timetuple()
    (2018, 2, 22, 0, 0, 0, 0, 50, -1)
    >>> a.timetuple(pythonic_wday=True)
    (2018, 2, 22, 0, 0, 0, 6, 50, -1)
    >>> str(a)
    'Asgardian date: 2018-02-22'

Still a lot to do - but the basics are ok.
