def days_in_months(year):
    is_leap_year = False
    if year%4==0: is_leap_year = True
    if year%100==0: is_leap_year = False
    if year%400==0: is_leap_year = True
    return [31,28+int(is_leap_year),31,30,31,30,31,31,30,31,30,31]


if __name__ == '__main__':
    days = ['sun','mon','tue','wed','thu','fri','sat']
    months = ['jan','feb','mar','apr','may','jun',
                'jul','aug','sep','oct','nov','dec']

    first_sundays = 0

    count = 0
    year = 1900
    date = 0
    month = 1
    date_totals = days_in_months(year)
    while year<2001:
        count += 1
        date += 1
        day = days[count%7]
        if date>date_totals[month-1]:
            date = 1
            month += 1
        if month>12:
            month = 1
            year += 1
            date_totals = days_in_months(year)
        if date==1 and day=='sun' and year>1900:
            first_sundays += 1
            print(day,months[month-1],date,year)
    print(first_sundays)
