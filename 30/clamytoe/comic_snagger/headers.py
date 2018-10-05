"""
headers.py

Sample headers to be used with requests
"""
from typing import Dict

IE: Dict[str, str] = {
    "Accept": "text/html, application/xhtml+xml, */*",
    "Accept-Language": "en-US",
    "Connection": "Keep-Alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) "
    "like Gecko",
}

FIREFOX_LINUX: Dict[str, str] = {
    "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, " "*/*;q=0.8",
    "Accept-Language": "en-GB, en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) "
    "Gecko/20100101 Firefox/60.0",
}

CHROME_MOBILE: Dict[str, str] = {
    "Accept": "text/html.application/xhtml+xml, application/xml;q=0.9, " "*/*;q=0.8",
    "Accept-Language": "en-us",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) "
    "AppleWebKit/604.1.34 (KHTML, like Gecko) "
    "CriOS/67.0.3396.87 Mobile/15F79 Safari/604.1",
}

FIREFOX_MOBILE: Dict[str, str] = {
    "Accept": "text/html.application/xhtml+xml, application/xml;q=0.9, " "*/*;q=0.8",
    "Accept-Language": "en-us",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/12.1b10941 "
    "Mobile/15F79 Safari/605.1.15",
}

SAFARI_MOBILE: Dict[str, str] = {
    "Accept": "text/html.application/xhtml+xml, application/xml;q=0.9, " "*/*;q=0.8",
    "Accept-Language": "en-us",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 "
    "Mobile/15E148 Safari/604.1",
}
