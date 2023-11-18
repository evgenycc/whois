# whois
A script to get WHOIS information about domains.

I can't say with certainty that it worked, as it is still undergoing testing. But, as shown by more than 10000 domains, it works. 
To use this script you just need to unzip it to your desired directory. Then import it into your script for further use.
The only parameter that is passed to the script, besides the domain name, is to tell the script to use IANA's WHOIS server. Further, in the examples, I will show it.

Actually, the examples themselves. 
Simple use of the script, without additional parameters.

```python
from pprint import pprint

from whois import whois

pprint(whois("google.com"))
```

Result:

```
{'date': {'created': '1997-09-15T04:00:00Z',
          'expires': '2028-09-14T04:00:00Z',
          'updated': '2019-09-09T15:39:04Z'},
 'domain': 'google.com',
 'nserver': ['NS1.GOOGLE.COM',
             'NS2.GOOGLE.COM',
             'NS3.GOOGLE.COM',
             'NS4.GOOGLE.COM'],
 'registrar': {'registrar': 'MarkMonitor Inc.',
               'registrar_url': 'http://www.markmonitor.com',
               'registrar_whois_server': 'whois.markmonitor.com'}}
```

Use of a parameter specifying to use the IANA WHOIS server in the absence of information from the main WHOIS server.

```python
from pprint import pprint

from whois import whois

if data := whois("google8888888888888888888888888888888.com"):
    pprint(data)
else:
    if data := whois("google8888888888888888888888888888888.com", wh_serv=True):
        pprint(data)
    else:
        print("No data received")
```

Result:

```
{'date': {'created': '1985-01-01', 'expires': None, 'updated': '2023-09-12'},
 'domain': 'google8888888888888888888888888888888.com',
 'nserver': ['A.GTLD-SERVERS.NET 192.5.6.30 2001503a83e000230',
             'B.GTLD-SERVERS.NET 192.33.14.30 2001503231d000230',
             'C.GTLD-SERVERS.NET 192.26.92.30 200150383eb000030',
             'D.GTLD-SERVERS.NET 192.31.80.30 2001500856e000030',
             'E.GTLD-SERVERS.NET 192.12.94.30 20015021ca1000030',
             'F.GTLD-SERVERS.NET 192.35.51.30 2001503d414000030',
             'G.GTLD-SERVERS.NET 192.42.93.30 2001503eea3000030',
             'H.GTLD-SERVERS.NET 192.54.112.30 20015028cc000030',
             'I.GTLD-SERVERS.NET 192.43.172.30 200150339c1000030',
             'J.GTLD-SERVERS.NET 192.48.79.30 20015027094000030',
             'K.GTLD-SERVERS.NET 192.52.178.30 2001503d2d000030',
             'L.GTLD-SERVERS.NET 192.41.162.30 2001500d937000030',
             'M.GTLD-SERVERS.NET 192.55.83.30 2001501b1f9000030'],
 'registrar': {'registrar': None,
               'registrar_url': None,
               'registrar_whois_server': 'whois.verisign-grs.com'}}
```

Well and an example where the script can't get the information:

```python
from pprint import pprint

from whois import whois

if data := whois("agnese.arpa"):
    pprint(data)
else:
    if data := whois("agnese.arpa", wh_serv=True):
        pprint(data)
    else:
        print("No data received")
```

Result:

```
No data received
```
