from datetime import datetime as dtm

from dateutil.parser import parse

months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "Jun": "06", "Jul": "07",
          "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12", "January": "01", "February": "02",
          "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09",
          "October": "10", "November": "11", "December": "12"}


def date_parse(date: str):
    if ("(Changed)" in date and " AT " in date) or ("(Assigned)" in date and " AT "):
        date = date.split()[-2]
        return dtm.strptime(parse(date).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    if " #" in date:
        date = date.split()[0]
        return dtm.strptime(parse(date).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    if "before " in date:
        dt = date.replace("before ", "")
        date = f'{dt.split("-")[1]}-{dt.split("-")[0].replace(dt.split("-")[0], months[dt.split("-")[0]])}-01 00:00:00'
        return dtm.strptime(parse(date).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    if "(GMT" in date or "(UTC" in date:
        return dtm.strptime(parse(date.split("(")[0].strip()).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    if date.strip() == "-" or not date.strip() or "N/A" in date.strip():
        return None
    if " each year" in date:
        year = dtm.now().year + 1
        cd_d = date.replace("st", "").replace("nd", "").replace("rd", "").replace("th", ""). \
            replace("each year", str(year))
        cd_d = (f'{cd_d.split()[2]}-{cd_d.split()[1].replace(cd_d.split()[1], months[cd_d.split()[1]])}-'
                f'{cd_d.split()[0]} 00:00:00')
        return dtm.strptime(parse(cd_d).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    return dtm.strptime(parse(date).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
