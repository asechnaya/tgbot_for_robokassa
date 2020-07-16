from datetime import datetime, timedelta


def payload():
    this_time = (datetime.utcnow() + timedelta(days=1)).strftime("%d.%m.%Y %H:%M")
    minus_hour = (datetime.utcnow() + timedelta(minutes=-30)).strftime("%d.%m.%Y %H:%M")

    data = {"SpecialOpFilter": "Finished",
            "Filter[Limit]": 100,
            "Filter[UsePeriod]": True,
            "Filter[DateFrom]": minus_hour,
            "Filter[DateTill]": this_time,
            "Filter[IncAccountFull]": False,
            "Filter[OutAccountFull]": False,
            "Filter[IncCurr]": "",
            "Filter[OutCurr]": "BNT",
            "Filter[IncludeAccounts]": False,
            "Filter[Processes]": ''}
    return data

