import datetime
from datetime import datetime, timedelta


def payload():
    this_time = datetime.today().strftime("%d.%m.%Y %H:%M")
    minus_hour = datetime.today() + timedelta(minutes=-30)
    minus_hour = minus_hour.strftime("%d.%m.%Y %H:%M")

    data = {"SpecialOpFilter": "Finished",
            "Filter[Limit]": 100,
            "Filter[UsePeriod]": True,
            "Filter[DateFrom]": minus_hour,
            "Filter[DateTill]": this_time,
            "Filter[IncAccountFull]": False,
            "Filter[OutAccountFull]": False,
            "Filter[IncCurr]": "BNT",
            "Filter[IncludeAccounts]": False,
            "Filter[Processes]": ''}
    return data
