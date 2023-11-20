"""
A set of parsers for different domain zones, the information from which is obtained in a non-linear form.
"""

from wh_parsers.data_update import data_update


def am_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        if ms.strip().startswith("Registrar:"):
            try:
                registrar.add(ms.strip().split(": ")[1].strip())
            except IndexError:
                pass
        if ms.strip().startswith("Registered:"):
            try:
                date.append({"created": ms.strip().split(": ")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Last modified:"):
            try:
                date.append({"updated": ms.strip().split(": ")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Expires:"):
            try:
                date.append({"expires": ms.strip().split(": ")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("DNS servers:"):
            try:
                ns = msg.strip().split("DNS servers:")[1].split("   Registered:")[0].strip()
                for n in ns.splitlines():
                    nserver.append(n.strip())
            except IndexError:
                pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def as_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    try:
        rgs = msg.split("Registrar:")[1].split("Relevant dates:")[0].strip()
        if rgs.strip() != "":
            registrar.add(rgs)
    except IndexError:
        pass
    try:
        rgs_whois = msg.split("Registrar:")[1].split("Relevant dates:")[0].strip(). \
                               split("(")[1].replace(")", "")
        if rgs_whois.strip() != "":
            registrar_whois.append({"registrar_url": rgs_whois})
    except IndexError:
        pass
    try:
        created = msg.split("Relevant dates:")[1].split("     Registry fee due on")[0].strip(). \
                    split("Registered on ")[1].strip()
        if created.strip() != "":
            date.append({"created": created})
    except IndexError:
        pass
    try:
        expires = msg.split("     Registry fee due on ")[1].split("Registration status:")[0].strip()
        if expires.strip() != "":
            date.append({"expires": expires})
    except IndexError:
        pass
    try:
        ns = msg.split("Name servers:")[1].split("WHOIS lookup made on")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def aw_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        try:
            if ms.strip().startswith("Creation Date:"):
                created = ms.strip().split(": ")[1].strip()
                if created.strip() != "":
                    date.append({"created": created})
            if ms.strip().startswith("Updated Date:"):
                updated = ms.strip().split(": ")[1].strip()
                if updated.strip() != "":
                    date.append({"updated": updated})
        except IndexError:
            pass
    try:
        ns = msg.split("Domain nameservers:")[1].split("Record maintained by:")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                nserver.append(n.strip())
    except IndexError:
        pass
    try:
        rgs = msg.split("Registrar:")[1].split("Creation Date:")[0].strip()
        if rgs.strip() != "":
            for nm, rg in enumerate(rgs.splitlines()):
                if nm == 0:
                    registrar.add(rg.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def be_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        try:
            if ms.strip().startswith("Registered:"):
                created = ms.strip().split(":")[1].strip()
                if created.strip() != "":
                    date.append({"created": created})
        except IndexError:
            pass
    try:
        ns = msg.split("Nameservers:")[1].split("Keys:")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                nserver.append(n.strip())
    except IndexError:
        pass
    try:
        rgs = msg.split("Registrar:")[1].split("Nameservers:")[0].strip()
        for rg in rgs.splitlines():
            if rg.strip().startswith("Name:"):
                registrar.add(rg.strip().split(":")[1].strip())
            if rg.strip().startswith("Website:"):
                registrar_whois.append({"registrar_url": rg.strip().split()[1].strip()})
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def bg_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    try:
        ns = msg.split("NAME SERVER INFORMATION:")[1].split("DNSSEC:")[0].strip()
        for n in ns.splitlines():
            nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def bn_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        try:
            if ms.strip().startswith("Registrar:"):
                registrar.add(ms.strip().split("Registrar:")[1].strip())
            if ms.strip().startswith("Creation Date:"):
                date.append({"created": ms.strip().split("Creation Date:")[1].strip()})
            if ms.strip().startswith("Modified Date:"):
                date.append({"updated": ms.strip().split("Modified Date:")[1].strip()})
            if ms.strip().startswith("Expiration Date:"):
                date.append({"expires": ms.strip().split("Expiration Date:")[1].strip()})
        except IndexError:
            pass
    try:
        ns = msg.split("Name Servers:")[1].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def edu_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        try:
            if ms.strip().startswith("Domain record activated:"):
                date.append({"created": ms.strip().split("Domain record activated:")[1].strip()})
            if ms.strip().startswith("Domain record last updated:"):
                date.append({"updated": ms.strip().split("Domain record last updated:")[1].strip()})
            if ms.strip().startswith("Domain expires:"):
                date.append({"expires": ms.strip().split("Domain expires:")[1].strip()})
        except IndexError:
            pass
    try:
        ns = msg.split("Name Servers:")[1].split("Domain record activated:")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def ee_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    try:
        dom_info = msg.split("Domain:")[1].split("Registrant:")[0].strip()
        if dom_info.strip() != "":
            for df in dom_info.splitlines():
                if df.strip().startswith('registered:'):
                    date.append({"created": df.strip().split("registered:")[1].strip()})
                if df.strip().startswith('changed:'):
                    date.append({"updated": df.strip().split("changed:")[1].strip()})
                if df.strip().startswith('expire:'):
                    date.append({"expires": df.strip().split("expire:")[1].strip()})
    except IndexError:
        pass
    try:
        rgs = msg.split("Registrar:")[1].split("Name servers:")[0].strip()
        if rgs.strip() != "":
            for rg in rgs.splitlines():
                if rg.strip().startswith("name:"):
                    registrar.add(rg.strip().split("name:")[1].strip())
                if rg.strip().startswith("url:"):
                    registrar_whois.append({"registrar_url": rg.strip().split("url:")[1].strip()})
    except IndexError:
        pass
    try:
        ns = msg.split("Name servers:")[1].split("More information at")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                if n.strip().startswith("nserver:"):
                    nserver.append(n.strip().split("nserver:")[1].strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def eu_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    try:
        rgs = msg.split("Registrar:")[1].split("Name servers:")[0].strip()
        if rgs.strip() != "":
            for rg in rgs.splitlines():
                if rg.strip().startswith("Name:"):
                    registrar.add(rg.strip().split("Name:")[1].strip())
                if rg.strip().startswith("Website:"):
                    registrar_whois.append({"registrar_url": rg.strip().split("Website:")[1].strip()})
    except IndexError:
        pass
    try:
        ns = msg.split("Name servers:")[1].split("Please visit")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def gg_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    # registrar, reg_url
    try:
        rgs = msg.split("Registrar:")[1].split("Relevant dates:")[0].strip()
        if "(" in rgs.strip():
            url = rgs.strip().split("(")[1].replace(")", "").strip()
            registrar_whois.append({"registrar_url": url})
        registrar.add(rgs)
    except IndexError:
        pass
    # created
    try:
        cr_d = msg.split("Relevant dates:")[1].split("Registration status:")[0].split("Registered on")[1]. \
            split("Registry fee")[0].strip()
        date.append({"created": cr_d})
    except IndexError:
        pass
    # expires
    try:
        ex_d = msg.split("Relevant dates:")[1].split("Registration status:")[0].split("Registry fee due on")[1].strip()
        date.append({"expires": ex_d})
    except IndexError:
        pass
    # nserver
    try:
        ns = msg.split("Name servers:")[1].split("WHOIS lookup made on")[0].strip()
        for n in ns.splitlines():
            nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def hk_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        try:
            if ms.strip().startswith("Registrar Name:"):
                registrar.add(ms.strip().split("Registrar Name:")[1].strip())
            if ms.strip().startswith("Domain Name Commencement Date:"):
                date.append({"created": ms.strip().split("Domain Name Commencement Date:")[1].strip()})
            if ms.strip().startswith("Expiry Date:"):
                date.append({"expires": ms.strip().split("Expiry Date:")[1].strip()})
        except IndexError:
            pass
    try:
        ns = msg.split("Name Servers Information:")[1].split("Status Information:")[0].strip()
        if ns.strip():
            for n in ns.splitlines():
                nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def it_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    try:
        rg = msg.split("Registrar")[1].split("  DNSSEC:")[0].split("Name:")[1].strip()
        for r in rg.splitlines():
            if r.strip().startswith("Web:"):
                registrar_whois.append({"registrar_url": r.split("  Web:")[1].strip()})
            else:
                registrar.add(r.strip())
    except IndexError:
        pass
    try:
        date.append({"created": msg.split("Created:")[1].split("Last Update:")[0].strip()})
    except IndexError:
        pass
    try:
        date.append({"updated": msg.split("Last Update:")[1].split("Expire Date:")[0].strip()})
    except IndexError:
        pass
    try:
        date.append({"expires": msg.split("Expire Date:")[1].split("Registrant")[0].strip()})
    except IndexError:
        pass
    try:
        ns = msg.split("Nameservers")[1].strip()
        for n in ns.splitlines():
            if n.strip() == "":
                continue
            nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def je_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    # registrar, reg_url
    try:
        rgs = msg.split("Registrar:")[1].split("Relevant dates:")[0].strip()
        if "(" in rgs.strip():
            url = rgs.strip().split("(")[1].replace(")", "").strip()
            registrar_whois.append({"registrar_url": url})
        registrar.add(rgs)
    except IndexError:
        pass
    # created
    try:
        cr_d = msg.split("Relevant dates:")[1].split("Registration status:")[0].split("Registered on")[1]. \
            split("Registry fee")[0].strip()
        date.append({"created": cr_d})
    except IndexError:
        pass
    # expires
    try:
        ex_d = msg.split("Relevant dates:")[1].split("Registration status:")[0].split("Registry fee due on")[1].strip()
        date.append({"expires": ex_d})
    except IndexError:
        pass
    # nserver
    try:
        ns = msg.split("Name servers:")[1].split("WHOIS lookup made on")[0].strip()
        for n in ns.splitlines():
            nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def kg_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        if ms.strip().startswith("Record created:"):
            try:
                date.append({"created": ms.strip().split("Record created:")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Record last updated on:"):
            try:
                date.append({"updated": ms.strip().split("Record last updated on:")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Record expires on:"):
            try:
                date.append({"expires": ms.strip().split("Record expires on:")[1].strip()})
            except IndexError:
                pass

    try:
        ns = msg.split("Name servers in the listed order:")[1].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def mo_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    try:
        date.append({"created": msg.split("Record created on")[1].split("Record expires on")[0].strip()})
    except IndexError:
        pass
    try:
        date.append({"expires": msg.split("Record expires on")[1].split("Domain name servers:")[0].strip()})
    except IndexError:
        pass
    try:
        ns = msg.split("Domain name servers:")[1].strip()
        for n in ns.splitlines():
            if n.strip().startswith("-"):
                continue
            nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def nl_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    try:
        rgs = msg.split("Registrar:")[1].split("Abuse Contact:")[0].strip()
        for nm, rg in enumerate(rgs.splitlines()):
            if nm == 0:
                registrar.add(rg.strip())
    except IndexError:
        pass
    for ms in msg.splitlines():
        if ms.startswith("Creation Date:"):
            try:
                date.append({"created": ms.split("Creation Date:")[1].strip()})
            except IndexError:
                pass
        if ms.startswith("Updated Date:"):
            try:
                date.append({"updated": ms.split("Updated Date:")[1].strip()})
            except IndexError:
                pass
    try:
        ns = msg.split("Domain nameservers:")[1].split("Record maintained by:")[0].strip()
        for n in ns.splitlines():
            nserver.append(n.strip())
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def sg_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    try:
        rgs = msg.split("Registrar:")[1].split("Domain Name:")[0].strip()
        registrar.add(rgs)
    except IndexError:
        pass
    try:
        dt = msg.split("Registrar:")[1].split("Registrant:")[0].strip()
        if dt.strip() != "":
            for d in dt.splitlines():
                if d.strip().startswith("Creation Date:"):
                    try:
                        date.append({"created": d.strip().split("Creation Date:")[1].strip()})
                    except IndexError:
                        pass
                if d.strip().startswith("Modified Date:"):
                    try:
                        date.append({"updated": d.strip().split("Modified Date:")[1].strip()})
                    except IndexError:
                        pass
                if d.strip().startswith("Expiration Date:"):
                    try:
                        date.append({"expires": d.strip().split("Expiration Date:")[1].strip()})
                    except IndexError:
                        pass
    except IndexError:
        pass

    try:
        ns = msg.split("Name Servers:")[1].split("DNSSEC:")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def sm_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        if ms.strip().startswith("Registration date:"):
            try:
                date.append({"created": ms.strip().split("Registration date:")[1].strip()})
            except IndexError:
                pass
    try:
        ns = msg.split("DNS Servers:")[1].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def tn_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        if ms.strip().startswith("Creation date.......:"):
            try:
                date.append({"created": ms.strip().split("Creation date.......:")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Registrar...........:"):
            try:
                registrar.add(ms.strip().split("Registrar...........:")[1].strip())
            except IndexError:
                pass

    try:
        ns = msg.split("DNS servers")[1].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.split("Name................:")[1].strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def tr_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        if ms.strip().startswith("Created on..............:"):
            try:
                date.append({"created": ms.strip().split("Created on..............:")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Expires on..............:"):
            try:
                date.append({"expires": ms.strip().split("Expires on..............:")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Organization Name	:"):
            try:
                registrar.add(ms.strip().split("Organization Name	:")[1].strip())
            except IndexError:
                pass

    try:
        ns = msg.split("** Domain Servers:")[1].split("** Additional Info:")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def tw_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        if ms.strip().startswith("Record created on"):
            try:
                date.append({"created": ms.strip().split("Record created on")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Record expires on"):
            try:
                date.append({"expires": ms.strip().split("Record expires on")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Registration Service Provider:"):
            try:
                registrar.add(ms.strip().split("Registration Service Provider:")[1].strip())
            except IndexError:
                pass
        if ms.strip().startswith("Registration Service URL:"):
            try:
                registrar_whois.append({"registrar_url": ms.strip().split("Registration Service URL:")[1].strip()})
            except IndexError:
                pass

    try:
        ns = msg.split("Domain servers in listed order:")[1].split("Registration Service Provider:")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def uk_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    try:
        rgs = msg.split("Registrar:")[1].split("Relevant dates:")[0].strip()
        if rgs.strip() != "":
            for nm, rg in enumerate(rgs.splitlines()):
                try:
                    if nm == 0:
                        registrar.add(rg.strip().split("[")[0].strip())
                    if rg.strip().startswith("URL:"):
                        registrar_whois.append({"registrar_url": rg.strip().split("URL:")[1].strip()})
                except IndexError:
                    pass
    except IndexError:
        pass

    try:
        dt = msg.split("Relevant dates:")[1].split("Registration status:")[0].strip()
        if dt.strip() != "":
            for d in dt.splitlines():
                try:
                    if d.strip().startswith("Registered on:"):
                        date.append({"created": d.strip().split("Registered on:")[1].strip()})
                except IndexError:
                    pass
                try:
                    if d.strip().startswith("Last updated:"):
                        date.append({"updated": d.strip().split("Last updated:")[1].strip()})
                except IndexError:
                    pass
                try:
                    if d.strip().startswith("Expiry date:"):
                        date.append({"expires": d.strip().split("Expiry date:")[1].strip()})
                except IndexError:
                    pass
    except IndexError:
        pass

    try:
        ns = msg.split("Name servers:")[1].split("WHOIS lookup made at")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def xn__j6w193g_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        if ms.strip().startswith("Registrar Name:"):
            try:
                registrar.add(ms.strip().split("Registrar Name:")[1].strip())
            except IndexError:
                pass
        if ms.strip().startswith("Expiry Date:"):
            try:
                date.append({"expires": ms.strip().split("Expiry Date:")[1].strip()})
            except IndexError:
                pass
    try:
        ns = msg.split("Name Servers Information:")[1].split("Status Information:")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def xn__kprw13d_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        if ms.strip().startswith("Registration Service Provider:"):
            try:
                registrar.add(ms.strip().split("Registration Service Provider:")[1].strip())
            except IndexError:
                pass
        if ms.strip().startswith("Registration Service URL:"):
            try:
                registrar_whois.append({"registrar_url": ms.strip().split("Registration Service URL:")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Record expires on"):
            try:
                date.append({"expires": ms.strip().split("Record expires on")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Record created on"):
            try:
                date.append({"created": ms.strip().split("Record created on")[1].strip()})
            except IndexError:
                pass
    try:
        ns = msg.split("Domain servers in listed order:")[1].split("Registration Service Provider:")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def xn__kpry57d_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    for ms in msg.splitlines():
        if ms.strip().startswith("Registration Service Provider:"):
            try:
                registrar.add(ms.strip().split("Registration Service Provider:")[1].strip())
            except IndexError:
                pass
        if ms.strip().startswith("Registration Service URL:"):
            try:
                registrar_whois.append({"registrar_url": ms.strip().split("Registration Service URL:")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Record expires on"):
            try:
                date.append({"expires": ms.strip().split("Record expires on")[1].strip()})
            except IndexError:
                pass
        if ms.strip().startswith("Record created on"):
            try:
                date.append({"created": ms.strip().split("Record created on")[1].strip()})
            except IndexError:
                pass
    try:
        ns = msg.split("Domain servers in listed order:")[1].split("Registration Service Provider:")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False


def xn__qxa6a_parse(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    try:
        rgs = msg.split("Registrar:")[1].split("Name servers:")[0].strip()
        if rgs.strip() != "":
            for r in rgs.splitlines():
                if r.strip().startswith("Name:"):
                    try:
                        registrar.add(r.strip().split("Name:")[1].strip())
                    except IndexError:
                        pass
                if r.strip().startswith("Website:"):
                    try:
                        registrar_whois.append({"registrar_url": r.strip().split("Website:")[1].strip()})
                    except IndexError:
                        pass
    except IndexError:
        pass
    try:
        ns = msg.split("Name servers:")[1].split("Please visit")[0].strip()
        if ns.strip() != "":
            for n in ns.splitlines():
                try:
                    nserver.append(n.strip())
                except IndexError:
                    pass
    except IndexError:
        pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False
