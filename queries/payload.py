from datetime import date, timedelta


yesterday = date.today() - timedelta(days=12)
today = date.today() + timedelta(days=1)
dateTimeAfter = yesterday.strftime("%d.%m.%Y")
dateTimeUntil = today.strftime("%d.%m.%Y")

payload = {
    'Length': 13,
    'reqType': 'identification',
    'pageNumber': 1,
    'sortDirection': 'CreatedAsc',
    'assigned': 'NULL',
    'merchantType': 'MerchantOff',
    'PartnerCountry': 'RU',
    'PartnerIdentifier': '',
    'ShopIdentifier': '',
    'reqState': 92,
    'DateType': 'modified',
    'dateTimeAfter': dateTimeAfter,
    'dateTimeUntil': dateTimeUntil,
    'fetchRows': 30,
    'X-Requested-With': 'XMLHttpRequest'
}