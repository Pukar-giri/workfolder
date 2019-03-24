from urllib import quote, unquote
from base64 import b64encode, b64decode

cookies=["_ga=GA1.2.1469851431.1539959281"," __auc=6681ddad1668f9d340012105520"," _gid=GA1.2.1368686734.1540308147"," PHPSESSID=89arhnestf7vubc5jtbi1qe482"," iknowmag1k=ZwkMiFxtQXnMN4vlv5507IDLgtN%2Feqe29NabnXROYzra378zmlZR6Q%3D%3D"]

for cookie in cookies:
    cookie.split("=")
    cookieval=cookie[1]
    cookieval=unquote(cookieval)
    cookieval=b64decode(cookieval)
    print(cookie[0]+"="+cookieval)
