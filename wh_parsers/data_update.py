"""
Updating the data dictionary.
"""


def data_update(dom: str, registrar: set, registrar_whois: list, date: list, nserver: list) -> dict:
    data = dict()

    data.update({"domain": None})
    if "registrar" not in data:
        data["registrar"] = dict()
    data["registrar"].update({"registrar": None, "registrar_url": None, "registrar_whois_server": None})
    if "date" not in data:
        data["date"] = dict()
    data["date"].update({"created": None, "updated": None, "expires": None})
    data.update({"nserver": None})

    if registrar:
        data.update({"domain": dom})
        data["registrar"].update({"registrar": "; ".join(registrar)})

    if registrar_whois:
        data.update({"domain": dom})
        for reg in registrar_whois:
            data["registrar"].update(reg)

    if date:
        data.update({"domain": dom})
        for dat in date:
            data["date"].update(dat)

    if nserver:
        data.update({"domain": dom})
        data.update({"nserver": sorted(list(set(nserver)))})

    return data
