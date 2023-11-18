import socket
import time
from pathlib import Path

from wh_set.set_zones import zones
from wh_parsers.standard import standard
from wh_set.zones_list import z_standard, other


def run_whois(server: str, query: str) -> (tuple, bool):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(5)
        s.connect((server, 43))

        s.send((bytes(query, 'utf-8')) + b'\r\n')
        msg = ''
        while len(msg) < 10000:
            receive_data = str((s.recv(100)), encoding='utf-8')
            if receive_data == '':
                break
            msg = msg + receive_data
        s.close()
        return msg
    except Exception:
        s.close()
        return False, False


def whois(dom: str, wh_serv=False) -> (dict, str):
    try:
        dom = dom.replace("\u200f", "").replace("\u200e", "").encode('idna').decode()
        zone = Path(dom).suffix.replace(".", "")
        if wh_serv:
            whois_srv = "whois.iana.org"
        else:
            whois_srv = zones[zone].get('primary')
        if "www." in dom:
            dom = dom.replace("www.", "")
        if len(dom.split(".")) > 2:
            if zone not in ['abb', 'abbott', 'amsterdam', 'apple', 'au', 'aws', 'ba', 'bd', 'br', 'cba', 'chat',
                            'citic', 'ck', 'co', 'com', 'dev', 'dhl', 'eg', 'fj', 'fr', 'gh', 'gn', 'gr', 'gt',
                            'hisamitsu', 'il', 'ke', 'kh', 'komatsu', 'kw', 'lb', 'link', 'live', 'locus', 'lr', 'lu',
                            'makeup', 'mattel', 'md', 'me', 'microsoft', 'mm', 'mo', 'mobile', 'mx', 'my', 'mz', 'nf',
                            'ni', 'ninja', 'nl', 'np', 'ntt', 'nz', 'ott', 'page', 'pe', 'pharmacy', 'pictet', 'pn',
                            'py', 'sakura', 'sap', 'schmidt', 'school', 'schwarz', 'se', 'sharp', 'sk', 'sv', 'total',
                            'tr', 'trust', 'tz', 'uy', 'va', 've', 'vi', 'weber', 'weir', 'woodside', 'xn--h2brj9c',
                            'xn--qxa6a', 'xn--wgbl6a', 'yandex', 'ye', 'youtube', 'za', 'zm', 'zw']:
                dom = f'{dom.split(".")[-2]}.{dom.split(".")[-1]}'
        parser = ""
        if wh_serv:
            parser = standard
        else:
            if zone in z_standard:
                parser = standard
            elif other.get(zone):
                parser = other.get(zone)

        msg = ""
        cnt = 0
        while (msg == "" or msg is False) and cnt < 7:
            msg = run_whois(whois_srv, dom)
            if msg:
                msg = msg.strip()
                break
            cnt += 1
            time.sleep(1)

        if msg:
            dat = parser(msg, dom)
            if dat:
                return dat
            return False
        return False
    except (KeyError, TypeError, AttributeError):
        return False
