"""
Parser for domain zones whose information is transferred in linear form.
pip install python-dateutil
"""
from wh_parsers.data_update import data_update
from wh_parsers.date_parse import date_parse


def standard(msg: str, dom: str) -> (dict, bool):
    registrar = set()
    registrar_whois = []
    date = []
    nserver = []

    changed = False
    for ms in msg.splitlines():
        try:
            # registrar
            if ms.strip().startswith(("Registrar Handle...........:", "Registrar:..........", "registrar............:",
                                      "Registrar:", "registrar:", "Registar created:", "Registrar Name:",
                                      "registrar name:", "Registrar Compagnie Name :", "registrar-name:",
                                      "Authorized Agency           :", "Sponsoring Registrar Organization:",
                                      "registrar..........:", "Sponsoring Registrar:", "Registrar name:")):
                spl = next(filter(ms.strip().startswith, ("Registrar Handle...........:", "Registrar:..........",
                                                          "registrar............:", "Registrar:", "registrar:",
                                                          "Registar created:", "Registrar Name:", "registrar name:",
                                                          "Registrar Compagnie Name :", "registrar-name:",
                                                          "Authorized Agency           :",
                                                          "Sponsoring Registrar Organization:",
                                                          "registrar..........:", "Sponsoring Registrar:",
                                                          "Registrar name:")))
                if ms.strip().split(spl)[1].strip() != "":
                    rgs = ms.strip().split(spl)[1].strip()
                    if "(" in rgs:
                        url = rgs.split("(")[1].replace(")", "").strip()
                        if "." in url or "http:" in url or "https:" in url or "www" in url:
                            registrar_whois.append({"registrar_url": url})
                            registrar.add(rgs.split("(")[0].strip())
                            continue
                    registrar.add(rgs)

            # registrar_url
            if ms.strip().startswith(("registrar-url:", "Registrar URL:", "website:", "www..................:",
                                      "registrar info:", "Referral URL:", "URL:", "Registrar website:",
                                      "Sponsoring Registrar URL:", "www................:", "admin-contact:")):
                spl = next(filter(ms.strip().startswith, ("registrar-url:", "Registrar URL:", "website:",
                                                          "www..................:", "registrar info:",
                                                          "Referral URL:", "URL:", "Registrar website:",
                                                          "Sponsoring Registrar URL:", "www................:",
                                                          "admin-contact:")))
                if ms.strip().split(spl)[1].strip() != "":
                    url_rg = ms.strip().split(spl)[1].strip()
                    if "http:" in url_rg or "https:" in url_rg or "www" in url_rg or "." in url_rg:
                        registrar_whois.append({"registrar_url": ms.strip().split(spl)[1].strip()})

            # registrar_whois_server
            if ms.strip().startswith(("Registrar WHOIS Server:", "whois:", "Registry WHOIS Server:", "WHOIS Server:",
                                      "Registrar WHOIS server:")):
                spl = next(filter(ms.strip().startswith, ("Registrar WHOIS Server:", "whois:",
                                                          "Registry WHOIS Server:", "WHOIS Server:",
                                                          "Registrar WHOIS server:")))
                wh = ms.strip().split(spl)[1].strip()
                if wh != "":
                    if wh.endswith("/"):
                        wh = wh[:-1]
                    if "whois" in wh or "www" in wh or "." in wh:
                        registrar_whois.append({"registrar_whois_server": wh})

            # created
            if ms.strip().startswith(("Registration date:", "created:", "Creation Date:", "Created:",
                                      "Date de création:", "Activation:.........", "registered:", "Registered On:",
                                      "Date Created:", "Domain created:", "created..............:",
                                      "Created (JJ/MM/AAAA) :", "Created On:", "Registered on:", "Registered:",
                                      "Registered Date             :", "created............:", "Registration Time:",
                                      "Creation date:", "Fecha de activación:", "Created date:", "Created Date:",
                                      "record created:")):
                spl = next(filter(ms.strip().startswith, ("Registration date:", "created:", "Creation Date:",
                                                          "Created:", "Date de création:", "Activation:.........",
                                                          "registered:", "Registered On:", "Date Created:",
                                                          "Domain created:", "created..............:",
                                                          "Created (JJ/MM/AAAA) :", "Created On:", "Registered on:",
                                                          "Registered:", "Registered Date             :",
                                                          "created............:", "Registration Time:",
                                                          "Creation date:", "Fecha de activación:", "Created date:",
                                                          "Created Date:", "record created:")))
                if ms.strip().split(spl)[1].strip() != "":
                    cr_d = ms.strip().split(spl)[1].strip()
                    if cr_d.endswith("."):
                        cr_d = cr_d[:-1]
                    date.append({"created": date_parse(cr_d)})

            # updated
            if ms.strip().startswith(("Modification date:", "modified:", "Updated Date:", "Updated:",
                                      "Dernière modification:", "last-update:", "changed:", "Renewed On:",
                                      "Last modified :", "Last Modified:", "modified.............:",
                                      "Last renewed (JJ/MM/AAAA) :", "Last updated:", "Last Updated On:",
                                      "Last Updated Date           :", "modified...........:", "Update Date:",
                                      "Updated date:")):
                spl = next(filter(ms.strip().startswith, ("Modification date:", "modified:", "Updated Date:",
                                                          "changed:", "Updated:", "Dernière modification:",
                                                          "last-update:", "Renewed On:", "Last modified :",
                                                          "Last Modified:", "modified.............:",
                                                          "Last renewed (JJ/MM/AAAA) :", "Last updated:",
                                                          "Last Updated On:", "Last Updated Date           :",
                                                          "modified...........:", "Update Date:", "Updated date:")))
                if not changed:
                    if ms.strip().split(spl)[1].strip() != "":
                        up_d = ms.strip().split(spl)[1].strip()
                        if up_d.endswith("."):
                            up_d = up_d[:-1]
                        date.append({"updated": date_parse(up_d)})
                        changed = True

            # expires
            if ms.strip().startswith(("Expiration date:", "expires:", "expire:", "Registry Expiry Date:",
                                      "Valid Until:", "Date d'expiration:", "Expiration Date:", "Expiry Date:",
                                      "Expiration:.........", "Expiry :", "Expires On:", "Expiry date:",
                                      "expires..............:", "expire:", "validity:", "Expire (JJ/MM/AAAA) :",
                                      "Expires    on:", "Expires:", "Expiration Date             :",
                                      "Registrar Registration Expiration Date:", "expires............:",
                                      "Expiration Time:", "Fecha de corte:", "free-date:", "Exp date:")):
                spl = next(filter(ms.strip().startswith, ("Expiration date:", "expires:", "expire:",
                                                          "Registry Expiry Date:", "Valid Until:", "Expiry :",
                                                          "Date d'expiration:", "Expiration Date:", "Expiry Date:",
                                                          "Expiration:.........", "Expires On:", "Expiry date:",
                                                          "expires..............:", "expire:", "validity:",
                                                          "Expire (JJ/MM/AAAA) :", "Expires    on:", "Expires:",
                                                          "Expiration Date             :",
                                                          "Registrar Registration Expiration Date:",
                                                          "expires............:", "Expiration Time:",
                                                          "Fecha de corte:", "free-date:", "Exp date:")))
                if ms.strip().split(spl)[1].strip() != "":
                    ex_d = ms.strip().split(spl)[1].strip()
                    if ex_d.endswith("."):
                        ex_d = ex_d[:-1]
                    date.append({"expires": date_parse(ex_d)})

            # nserver
            if ms.strip().startswith(("DNS:", "nserver:", "nameserver:", "Name Server:", "Nameserver:", "NS 1   :",
                                      "Serveur de noms:", "Name Server (DB):...", "NS 2   :", "NS 3   :", "NS 4   :",
                                      "NS 5   :", "DNS servers1:", "DNS servers2:", "DNS servers3:", "DNS servers4:",
                                      "DNS servers5:", "Primary server.........:", "Secondary server.......:",
                                      "nserver..............:", "Name server 1 :", "Name server 2 :",
                                      "Name server 3 :", "Name server 4 :", "Name server 5 :",
                                      "Name Server Handle.........:", "Host Name                :",
                                      "nserver............:", "Hostname:", "Name server:")):
                spl = next(filter(ms.strip().startswith, ("DNS:", "nserver:", "nameserver:", "Name Server:", "NS 1   :",
                                                          "Nameserver:", "Serveur de noms:", "Name Server (DB):...",
                                                          "NS 2   :", "NS 3   :", "NS 4   :", "NS 5   :",
                                                          "DNS servers1:", "DNS servers2:", "DNS servers3:",
                                                          "DNS servers4:", "DNS servers5:", "nserver..............:",
                                                          "Primary server.........:", "Secondary server.......:",
                                                          "Name server 1 :", "Name server 2 :", "Name server 3 :",
                                                          "Name server 4 :", "Name server 5 :",
                                                          "Name Server Handle.........:",
                                                          "Host Name                :", "nserver............:",
                                                          "Hostname:", "Name server:")))
                if ms.strip().split(spl)[1].strip().replace(":", "") != "":
                    nserver.append(ms.strip().split(spl)[1].strip().replace(":", "").replace("[OK]", "").strip())
        except IndexError:
            pass

    data = data_update(dom, registrar, registrar_whois, date, nserver)
    if data.get("domain"):
        return data
    return False
