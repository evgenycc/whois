"""
Information about parsers that are used for a particular domain zone.
"""

from wh_parsers.not_line_parsers import am_parse
from wh_parsers.not_line_parsers import as_parse
from wh_parsers.not_line_parsers import aw_parse
from wh_parsers.not_line_parsers import be_parse
from wh_parsers.not_line_parsers import bg_parse
from wh_parsers.not_line_parsers import bn_parse
from wh_parsers.not_line_parsers import edu_parse
from wh_parsers.not_line_parsers import ee_parse
from wh_parsers.not_line_parsers import eu_parse
from wh_parsers.not_line_parsers import gg_parse
from wh_parsers.not_line_parsers import hk_parse
from wh_parsers.not_line_parsers import it_parse
from wh_parsers.not_line_parsers import je_parse
from wh_parsers.not_line_parsers import mo_parse
from wh_parsers.not_line_parsers import nl_parse
from wh_parsers.not_line_parsers import sg_parse
from wh_parsers.not_line_parsers import sm_parse
from wh_parsers.not_line_parsers import tn_parse
from wh_parsers.not_line_parsers import tr_parse
from wh_parsers.not_line_parsers import tw_parse
from wh_parsers.not_line_parsers import kg_parse
from wh_parsers.not_line_parsers import uk_parse
from wh_parsers.not_line_parsers import xn__j6w193g_parse
from wh_parsers.not_line_parsers import xn__kprw13d_parse
from wh_parsers.not_line_parsers import xn__kpry57d_parse
from wh_parsers.not_line_parsers import xn__qxa6a_parse

z_standard = ["rs", "se", "si", "ski", "sk", "sn", "st", "tf", "tg", "tm", "tz", "ug", "vu", "wf", "yt", "xn--80ao21a",
              "xn--wgbl6a", "ga", "ax", "gf", "ls", "mq", "mw", "ae", "baidu", "br", "il", "cy", "gp", "pk", "ro", "re",
              "qa", "pm", "pf", "nu", "no", "mx", "md", "lu", "lt", "kz", "kr", "is", "id", "hr", "fr", "fi", "dk",
              "cr", "cn", "cl", "bo", "at", "xn--3hcrj9c", "xn--2scrj9c", "okinawa", "fire", "amica", "xn--ogbpf8fl",
              "xn--80aswg", "ws", "so", "mm", "games", "fj", "docs", "cam", "bayern", "band", "alstom", "ally", "ads",
              "statefarm", "prudential", "pru", "open", "msd", "microsoft", "food", "flickr", "dhl", "zero", "zappos",
              "you", "yandex", "yahoo", "yamaxun", "xn--tiq49xqyj", "xn--rovu88b", "xn--otu796d", "xn--nyqy26a",
              "xn--ngbrx", "xn--mgbi4ecexp", "xn--mgbab2bd", "xn--mgbaakc7dvf", "xn--mgba3a3ejt", "xn--jvr189m",
              "xn--jlq480n2rg", "xn--imr513n", "xn--gk3at1e", "xn--gckr3f0f", "xn--fct429k", "xn--eckvdtc9d",
              "xn--czr694b", "xn--czr694b", "xn--cckwcxetd", "xn--cck2b3b", "xn--bck1b9a5dre4c", "xn--80aqecdr1a",
              "xn--1ck2e1b", "xbox", "wow", "winners", "windows", "williamhill", "weir", "weatherchannel", "weather",
              "watches", "wanggou", "vivo", "unicom", "tushu", "tunes", "tube", "tmall", "tjx", "tjmaxx", "td",
              "target", "taobao", "talk", "suzuki", "stream", "staples", "ss", "spot", "sport", "spa", "song", "smile",
              "skype", "silk", "sener", "secure", "search", "save", "sas", "sakura", "safety", "safe", "rugby", "room",
              "ril", "ren", "reliance", "realtor", "read", "prime", "ping", "pin", "pictet", "phone", "phd", "pharmacy",
              "pfizer", "pay", "otsuka", "oldnavy", "office", "ntt", "now", "nike", "nhk", "nfl", "neustar", "netflix",
              "nba", "music", "mr", "moto", "moi", "mobile", "mlb", "mint", "merckmsd", "mattel", "marshalls", "map",
              "maif", "llp", "llc", "living", "lincoln", "lilly", "like", "lifeinsurance", "lb", "lanxess", "kpn",
              "kpmg", "kindle", "kids", "joy", "jot", "jnj", "jmp", "jio", "intuit", "inc", "imdb", "hyatt", "hotmail",
              "hotels", "hot", "hospital", "homesense", "homegoods", "health", "hbo", "hair", "gucci", "grocery",
              "grainger", "got", "gmo", "gay", "gap", "fun", "ftr", "frontier", "free", "fox", "ford", "flir",
              "ferrero", "fast", "farmers", "etisalat", "earth", "dupont", "dnp", "discover", "dell", "dealer", "deal",
              "data", "cruise", "crs", "cpa", "coupon", "citic", "citi", "citadel", "cisco", "circle", "chase",
              "charity", "cbre", "cbn", "catholic", "caravan", "calvinklein", "call", "box", "bot", "boston", "booking",
              "book", "bloomberg", "bing", "bible", "baseball", "baby", "azure", "axa", "aws", "author", "audible",
              "aramco", "arab", "analytics", "amex", "africa", "accenture", "tkmaxx", "praxi", "pramerica", "kw",
              "jprs", "jpmorgan", "itau", "ipiranga", "ieee", "hsbc", "guardian", "gh", "ge", "do", "bm", "bharti",
              "bh", "athleta", "able", "by", "xn--cg4bki", "xn--mk1bu44c", "xn--t60b56a", "xn--5su34j936bgsg",
              "xn--kcrx77d1x4a", "xn--fzys8d69uvgm", "xn--3bst00m", "xn--g2xx48c", "xn--flw351e", "xn--8y0a063a",
              "xn--io0a7i", "xn--5tzm5g", "xn--hxt814e", "xn--ses554g", "xn--nqv7fs00ema", "xn--6frz82g", "xn--unup4y",
              "xn--b4w605ferd", "xn--nqv7f", "xn--9et52u", "xn--efvy88h", "xn--mxtq1m", "xn--kput3i", "xn--6qq986b3xl",
              "xn--30rr7y", "xn--9krt00a", "xn--fjq720a", "xn--3ds443g", "xn--w4r85el8fhu5dnra", "xn--w4rs40l",
              "xn--czrs0t", "xn--czru2d", "xn--55qx5d", "xn--45q11c", "xn--vuq861b", "xn--vhquv", "xn--fiq228c5hs",
              "xn--rhqv96g", "xn--tckwe", "xn--qcka1pmc", "xn--q9jyb4c", "xn--42c2d9a", "xn--i1b6b1a6a2e",
              "xn--h2brj9c", "xn--11b4c3d", "xn--mgbt3dhd", "xn--4gbrim", "xn--fhbei", "xn--ngbc5azd", "xn--ngbe9e0a",
              "xn--mgba7c0bbn0a", "xn--mgbca7dzdo", "xn--p1ai", "xn--p1acf", "xn--c1avg", "xn--80asehdb",
              "xn--80adxhks", "xn--j1aef", "xn--d1acj3b", "xn--90ais", "zuerich", "zone", "zm", "zip", "zara", "za",
              "yun", "youtube", "yoga", "yodobashi", "yachts", "xyz", "xxx", "xin", "xihuan", 'xfinity', "xerox", "wtf",
              "wtc", "world", "works", "work", "woodside", "wolterskluwer", "wme", "wine", "win", "wiki", "wien",
              "whoswho", "weibo", "wedding", "wed", "website", "weber", "webcam", "watch", "wang", "walter", "walmart",
              "wales", "voyage", "voto", "voting", "vote", "volvo", "volkswagen", "vodka", "vlaanderen", "viva",
              "vision", "visa", "virgin", "vip", "vin", "villas", "viking", "vig", "video", "viajes", "vg", "vet",
              "versicherung", "xn--vermgensberatung-pwb", "xn--vermgensberater-ctb", "verisign", "ventures", "vegas",
              "ve", "vc", "vanguard", "vana", "vacations", "us", "ups", "uol", "uno", "university", "ubs", "ubank",
              "tvs", "tv", "tui", "trv", "trust", "travelersinsurance", "travelers", "travel", "training", "trading",
              "trade", "toys", "toyota", "town", "tours", "total", "toshiba", "toray", "top", "tools", "today", "tl",
              "tirol", "tires", "tips", "tienda", "tickets", "tiaa", "theatre", "theater", "thd", "th", "teva",
              "tennis", "temasek", "tel", "technology", "tech", "team", "tdk", "tci", "tc", "taxi", "tax", "tattoo",
              "tatar", "tatamotors", "taipei", "tab", "systems", "sydney", "sy", "swiss", "swatch", "surgery", "surf",
              "support", "supply", "supplies", "sucks", "style", "study", "studio", "store", "storage", "stockholm",
              "stcgroup", "stc", "statebank", "star", "stada", "srl", "space", "soy", "sony", "solutions", "solar",
              "sohu", "software", "softbank", "social", "soccer", "sncf", "smart", "sling", "sl", "sky", "skin", "ski",
              "site", "singles", "sina", "show", "shouji", "shopping", "shoes", "shiksha", "shia", "shell", "shaw",
              "sharp", "shangrila", "sh", "sfr", "sexy", "sex", "sew", "seven", "services", "select", "seek",
              "security", "seat", "scot", "science", "schwarz", "schule", "school", "scholarships", "schmidt",
              "schaeffler", "scb", "sca", "sc", "sbs", "sbi", "sb", "saxo", "sarl", "sap", "sanofi", "sandvikcoromant",
              "sandvik", "samsung", "samsclub", "salon", "sale", "saarland", "rwe", "rw", "run", "ruhr", "ru", "rsvp",
              "rogers", "rodeo", "rocks", "rip", "rio", "ricoh", "richardli", "rich", "rexroth", "reviews", "review",
              "restaurant", "racing", "radio", 'realestate', 'realty', 'recipes', 'red', 'redstone', 'redumbrella',
              'rehab', 'reise', 'reisen', 'reit', 'rent', 'rentals', 'repair', 'report', 'republican', 'rest', 'page',
              'panasonic', 'paris', 'pars', 'partners', 'parts', 'party', 'pccw', 'pe', 'pet', 'philips', 'photo',
              'photography', 'photos', 'physio', 'pics', 'pictures', 'pid', 'pink', 'pioneer', 'pizza', 'place', 'play',
              'playstation', 'plumbing', 'plus', 'pnc', 'pohl', 'poker', 'politie', 'porn', 'post', 'pr', 'press',
              'pro', 'prod', 'productions', 'prof', 'progressive', 'promo', 'properties', 'property', 'protection',
              'pub', 'pw', 'pwc', 'qpon', 'quebec', 'quest', 'obi', 'observer', 'olayan', 'olayangroup', 'ollo', 'om',
              'omega', 'one', 'ong', 'onl', 'online', 'ooo', 'oracle', 'orange', 'org', 'organic', 'origins', 'osaka',
              'ott', 'ovh', 'nab', 'nagoya', 'natura', 'navy', 'nec', 'net', 'netbank', 'network', 'new', 'news',
              'next', 'nextdirect', 'nexus', 'nf', 'ng', 'ngo', 'nico', 'nikon', 'ninja', 'nissan', 'nissay', 'nokia',
              'norton', 'nowruz', 'nowtv', 'nra', 'nrw', 'nyc', 'nz', 'ma', 'madrid', 'maison', 'makeup', 'man',
              'management', 'mango', 'market', 'marketing', 'markets', 'marriott', 'mba', 'mckinsey', 'me', 'med',
              'media', 'meet', 'melbourne', 'meme', 'memorial', 'men', 'menu', 'mg', 'miami', 'mini', 'mit',
              'mitsubishi', 'ml', 'mma', 'mn', 'mobi', 'moda', 'moe', 'mom', 'monash', 'money', 'monster', 'mormon',
              'mortgage', 'moscow', 'motorcycles', 'mov', 'movie', 'ms', 'mtn', 'mtr', 'mu', 'museum', 'my', 'mz', 'la',
              'lacaixa', 'lamborghini', 'lamer', 'lancaster', 'land', 'landrover', 'lasalle', 'lat', 'latino',
              'latrobe', 'law', 'lawyer', 'lc', 'lds', 'lease', 'leclerc', 'lefrak', 'legal', 'lego', 'lexus', 'lgbt',
              'lidl', 'life', 'lifestyle', 'lighting', 'limited', 'limo', 'link', 'lipsy', 'live', 'loan', 'loans',
              'locker', 'locus', 'lol', 'london', 'lotte', 'lotto', 'love', 'lpl', 'lplfinancial', 'ltd', 'ltda',
              'lundbeck', 'luxe', 'luxury', 'ly', 'kaufen', 'kddi', 'ke', 'kerryhotels', 'kerrylogistics',
              'kerryproperties', 'kfh', 'kia', 'kim', 'kitchen', 'kn', 'koeln', 'komatsu', 'kosher', 'krd', 'kred',
              'kuokgroup', 'ky', 'jaguar', 'java', 'jcb', 'jeep', 'jetzt', 'jewelry', 'jll', 'jobs', 'joburg',
              'juegos', 'juniper', 'ibm', 'icbc', 'ice', 'icu', 'ifm', 'ikano', 'imamat', 'immo', 'immobilien', 'in',
              'industries', 'infiniti', 'info', 'ing', 'ink', 'institute', 'insurance', 'insure', 'international',
              'investments', 'io', 'irish', 'ismaili', 'ist', 'istanbul', 'itv', 'hamburg', 'hangout', 'haus', 'hdfc',
              'hdfcbank', 'healthcare', 'help', 'helsinki', 'here', 'hermes', 'hiphop', 'hisamitsu', 'hitachi', 'hiv',
              'hkt', 'hn', 'hockey', 'holdings', 'holiday', 'homedepot', 'homes', 'honda', 'horse', 'host', 'hosting',
              'house', 'how', 'ht', 'hughes', 'hyundai', 'gal', 'gallery', 'gallo', 'gallup', 'game', 'garden', 'gbiz',
              'gd', 'gdn', 'gea', 'gent', 'genting', 'george', 'ggee', 'gi', 'gift', 'gifts', 'gives', 'giving',
              'gl', 'glass', 'gle', 'global', 'globo', 'gmail', 'gmbh', 'gmx', 'godaddy', 'gold', 'goldpoint', 'golf',
              'goo', 'goodyear', 'goog', 'google', 'gop', 'graphics', 'gratis', 'green', 'gripe', 'group', 'gs', 'guge',
              'guide', 'guitars', 'guru', 'gy', 'fage', 'fail', 'fairwinds', 'faith', 'family', 'fan', 'fans', 'farm',
              'fashion', 'fedex', 'feedback', 'ferrari', 'fidelity', 'fido', 'film', 'final', 'finance', 'financial',
              'firestone', 'firmdale', 'fish', 'fishing', 'fit', 'fitness', 'flights', 'florist', 'flowers', 'fly',
              'fm', 'fo', 'foo', 'football', 'forex', 'forsale', 'forum', 'foundation', 'fresenius', 'frl', 'frogans',
              'fujitsu', 'fund', 'furniture', 'futbol', 'fyi', 'eat', 'edeka', 'education', 'email', 'emerck', 'energy',
              'engineer', 'engineering', 'enterprises', 'epson', 'equipment', 'ericsson', 'erni', 'esq', 'estate',
              'eurovision', 'eus', 'events', 'exchange', 'expert', 'exposed', 'express', 'extraspace', 'dabur', 'dad',
              'dance', 'date', 'dating', 'datsun', 'day', 'dclk', 'dds', 'deals', 'degree', 'delivery', 'deloitte',
              'delta', 'democrat', 'dental', 'dentist', 'desi', 'design', 'dev', 'diamonds', 'diet', 'digital',
              'direct', 'directory', 'discount', 'dish', 'diy', 'dm', 'doctor', 'dog', 'domains', 'dot', 'download',
              'drive', 'dtv', 'dubai', 'dunlop', 'durban', 'dvag', 'dvr', 'cab', 'cafe', 'cal', 'camera', 'camp',
              'canon', 'capetown', 'capital', 'capitalone', 'car', 'cards', 'care', 'career', 'careers', 'cars', 'casa',
              'case', 'cash', 'casino', 'cat', 'catering', 'cba', 'cc', 'cd', 'center', 'ceo', 'cern', 'cfa', 'cfd',
              'chanel', 'channel', 'chat', 'cheap', 'chintai', 'christmas', 'chrome', 'church', 'ci', 'cipriani',
              'city', 'claims', 'cleaning', 'click', 'clinic', 'clinique', 'clothing', 'cloud', 'club', 'clubmed', 'cm',
              'co', 'coach', 'codes', 'coffee', 'college', 'cologne', 'com', 'comcast', 'commbank', 'community',
              'company', 'compare', 'computer', 'comsec', 'condos', 'construction', 'consulting', 'contact',
              'contractors', 'cooking', 'cool', 'coop', 'corsica', 'country', 'coupons', 'courses', 'credit',
              'creditcard', 'creditunion', 'cricket', 'cruises', 'cuisinella', 'cx', 'cymru', 'cyou', 'cz', 'bank',
              'bar', 'barcelona', 'barclaycard', 'barclays', 'barefoot', 'bargains', 'basketball', 'bauhaus', 'bbc',
              'bbt', 'bbva', 'bcg', 'bcn', 'beats', 'beauty', 'beer', 'bentley', 'berlin', 'best', 'bestbuy', 'bet',
              'bi', 'bid', 'bike', 'bingo', 'bio', 'biz', 'bj', 'black', 'blackfriday', 'blockbuster', 'blog', 'blue',
              'bms', 'bmw', 'bnpparibas', 'boats', 'boehringer', 'bofa', 'bom', 'bond', 'boo', 'bosch', 'bostik',
              'boutique', 'bradesco', 'bridgestone', 'broadway', 'broker', 'brother', 'brussels', 'build', 'builders',
              'business', 'buy', 'buzz', 'bw', 'bz', 'bzh', 'aarp', 'abbott', 'abbvie', 'abc', 'abogado', 'abudhabi',
              'ac', 'academy', 'accountant', 'accountants', 'aco', 'actor', 'adult', 'aeg', 'aero', 'af', 'afl', 'ag',
              'agakhan', 'agency', 'airbus', 'airforce', 'airtel', 'akdn', 'alibaba', 'alipay', 'allfinanz', 'allstate',
              'alsace', 'americanfamily', 'amfam', 'amsterdam', 'android', 'anquan', 'anz', 'aol', 'apartments', 'app',
              'apple', 'aquarelle', 'archi', 'army', 'art', 'arte', 'asda', 'asia', 'associates', 'attorney',
              'au', 'auction', 'audi', 'audio', 'auspost', 'auto', 'autos', 'avianca', "ca", "cf", "ch", "dz", 'ec',
              'eco', 'es', 'gq', 'hm', 'jp', 'ki', 'kiwi', 'kyoto', 'li', 'mc', 'mil', 'mk', 'mls', 'na', 'nc', 'pl',
              'ps', 'pt', 'sx', 'tk', 'tokyo', 'ua', 'uy', 'xn--90ae', 'xn--e1a4c', 'xn--d1alf', 'xn--y9a3aq',
              'xn--9dbq2a', 'xn--lgbbat1ad8j', 'xn--mgberp4a5d4ar', 'xn--mgbaam7a8h', 'xn--mgbbh1a71e', 'xn--mgb9awbf',
              'xn--ygbi2ammx', 'xn--wgbh1c', 'xn--c2br7g', 'xn--45brj9c', 'xn--gecrj9c', 'xn--xkc2dl3a5ee0h',
              'xn--clchc0ea0b2g2a9gcd', 'xn--fpcrj9c3d', 'xn--o3cw4h', 'xn--fiq64b', 'xn--fiqs8s', 'xn--fiqz9s',
              'xn--1qqw23a', 'xn--55qw42g', 'xn--3oq18vl8pn36a', 'xn--pssy2u', 'xn--estv75g', 'xn--xhq521b',
              'xn--zfr164b', 'xn--yfro4i67o', 'xn--mix891f', 'xn--3pxu8k', 'xn--jlq61u9w7b', 'xn--3e0b707e', 'az',
              'ba', 'ck', 'eg', 'gb', 'gm', 'gr', 'jo', 'kp', 'lk', 'mt', 'sd', 'va', 'ar', 'crown', 'iq', 'ryukyu',
              'xn--45br5cyl', 'xn--4dbrk0ce', 'xn--fzc2c9e2c', 'xn--h2breg3eve', 'xn--h2brj9c8c', 'xn--mgbah1a3hjkrd',
              'xn--mgbbh1a', 'xn--mgbgu82a', 'xn--mgbtx2b', 'xn--pgbs0dh', 'xn--q7ce6a', 'xn--rvc1e0am3e',
              'xn--xkc2al3hye2a', 'yokohama', 'bt', 'tj', 'xn--90a3ac', 'to', 'de', 'gov', 'hu', 'int', 'ir', 'lv',
              'name', 'sa', 'xn--mgba3a4f16a', 'shop', "xn--j1amh", "hu", "uz", "im", "cg", "ie", "al", "gw", "su",
              "ai", "ni", "tt", "vn", "bb", "dj", "ph", "sr", "et", "cv", "pa", "bs", "gt", "bf", "bd", "mv", "zw",
              "abb", "ao", "aq", "cu", "cw", "kh", "lr", "mp", "ne", "np", "pn", "py", "sv", "vi", "ye", "km", "gn",
              "amazon", "aaa"]

other = {"sg": sg_parse, "sm": sm_parse, "tn": tn_parse, "tw": tw_parse, "uk": uk_parse,
         "xn--kprw13d": xn__kprw13d_parse, "xn--kpry57d": xn__kpry57d_parse, "xn--j6w193g": xn__j6w193g_parse,
         "tr": tr_parse, "xn--qxa6a": xn__qxa6a_parse, "nl": nl_parse, "mo": mo_parse, "it": it_parse, "hk": hk_parse,
         "eu": eu_parse, "ee": ee_parse, "edu": edu_parse, "bn": bn_parse, "am": am_parse, "aw": aw_parse,
         "bg": bg_parse, "be": be_parse, "je": je_parse, "gg": gg_parse, "as": as_parse, "kg": kg_parse}
