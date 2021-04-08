Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> dir(urllib)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'parse']
>>> from urllib import request
>>> dir(request)
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_splitattr', '_splithost', '_splitpasswd', '_splitport', '_splitquery', '_splittag', '_splittype', '_splituser', '_splitvalue', '_thishost', '_to_bytes', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_registry', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
>>> res=request.openurl("https://www.wikipedia.org")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    res=request.openurl("https://www.wikipedia.org")
AttributeError: module 'urllib.request' has no attribute 'openurl'
>>> res=request.urlopen(""https://www.wikipedia.org")
		    
SyntaxError: invalid syntax
>>> res=request.urlopen("https://www.wikipedia.org")
>>> type(res)
<class 'http.client.HTTPResponse'>
>>> res.status
200
>>> res.peek()
b'<!DOCTYPE html>\n<html lang="en" class="no-js">\n<head>\n<meta charset="utf-8">\n<title>Wikipedia</title>\n<meta name="description" content="Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation.">\n<script>\ndocument.documentElement.className = document.documentElement.className.replace( /(^|\\s)no-js(\\s|$)/, "$1js-enabled$2" );\n</script>\n<meta name="viewport" content="initial-scale=1,user-scalable=yes">\n<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png">\n<link rel="shortcut icon" href="/static/favicon/wikipedia.ico">\n<link rel="license" href="//creativecommons.org/licenses/by-sa/3.0/">\n<style>\n.sprite{background-image:linear-gradient(transparent,transparent),url(portal/wikipedia.org/assets/img/sprite-46c49284.svg);background-repeat:no-repeat;display:inline-block;vertical-align:middle}.svg-Commons-logo_sister{background-position:0 0;width:47px;height:47px}.svg-MediaWiki-logo_sister{background-position:0 -47px;width:42px;height:42px}.svg-Meta-Wiki-logo_sister{background-position:0 -89px;width:37px;height:37px}.svg-Wikibooks-logo_sister{background-position:0 -126px;width:37px;height:37px}.svg-Wikidata-logo_sister{background-position:0 -163px;width:49px;height:49px}.svg-Wikimedia-logo_black{background-position:0 -212px;width:42px;height:42px}.svg-Wikipedia_wordmark{background-position:0 -254px;width:176px;height:32px}.svg-Wikiquote-logo_sister{background-position:0 -286px;width:42px;height:42px}.svg-Wikisource-logo_sister{background-position:0 -328px;width:39px;height:39px}.svg-Wikispecies-logo_sister{background-position:0 -367px;width:42px;height:42px}.svg-Wikiversity-logo_sister{background-position:0 -409px;width:43px;height:37px}.svg-Wikivoyage-logo_sister{background-position:0 -446px;width:36px;height:36px}.svg-Wiktionary-logo_sister{background-position:0 -482px;width:37px;height:37px}.svg-arrow-down{background-position:0 -519px;width:12px;height:8px}.svg-arrow-down-blue{background-position:0 -527px;width:14px;height:14px}.svg-badge_google_play_store{background-position:0 -541px;width:124px;height:38px}.svg-badge_ios_app_store{background-position:0 -579px;width:110px;height:38px}.svg-language-icon{background-position:0 -617px;width:22px;height:22px}.svg-noimage{background-position:0 -639px;width:58px;height:58px}.svg-search-icon{background-position:0 -697px;width:22px;height:22px}.svg-wikipedia_app_tile{background-position:0 -719px;width:42px;height:42px}\n</style>\n<style>\nhtml{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;font-size:62.5%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background-color:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:1px dotted}b,strong{font-weight:700}dfn{font-style:italic}h1{font-size:32px;font-size:3.2rem;margin:12px 0;margin:1.2rem 0}mark{background:#fc3;color:#000}small{font-size:13px;font-size:1.3rem}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-.5em}sub{bottom:-.25em}svg:not(:root){overflow:hidden}figure{margin:16px 40px;margin:1.6rem 4rem}hr{box-sizing:content-box}pre{overflow:auto}code,kbd,pre,samp{font-family:monospace,monospace;font-size:14px;font-size:1.4rem}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type=button],input[type=reset],input[type=submit]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type=checkbox],input[type=radio]{box-sizing:border-box;padding:0}input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{height:auto}input[type=search]{-webkit-appearance:none;box-sizing:content-box}input[type=search]::-webkit-search-cancel-button,input[type=search]::-webkit-search-decoration{-webkit-appearance:none}input[type=search]:focus{outline-offset:-2px}fieldset{border:1px solid #a2a9b1;margin:0 2px;margin:0 .2rem;padding:6px 10px 12px;padding:.6rem 1rem 1.2rem}legend{border:0;padding:0}textarea{overflow:auto}optgroup{font-weight:700}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}.hidden,[hidden]{display:none!important}.screen-reader-text{display:block;position:absolute!important;clip:rect(1px,1px,1px,1px);width:1px;height:1px;margin:-1px;border:0;padding:0;overflow:hidden}body{background-color:#fff;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Lato,Helvetica,Arial,sans-serif;font-size:14px;font-size:1.4rem;line-height:1.5;margin:4px 0 16px;margin:.4rem 0 1.6rem}a{-ms-touch-action:manipulation;touch-action:manipulation}a,a:active,a:focus{unicode-bidi:embed;outline:0;color:#36c;text-decoration:none}a:focus{outline:1px solid #36c}a:hover{text-decoration:underline}img{vertical-align:middle}hr,img{border:0}hr{clear:both;height:0;border-bottom:1px solid #c8ccd1;margin:2.6px 13px;margin:.26rem 1.3rem}.pure-button{display:inline-block;zoom:1;line-height:normal;white-space:nowrap;text-align:center;cursor:pointer;-webkit-user-drag:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;box-sizing:border-box;background-color:#f8f9fa;color:#202122;position:relative;min-height:19.2px;min-height:1.92rem;min-width:16px;min-width:1.6rem;margin:1.6px 0;margin:.16rem 0;border:1px solid #a2a9b1;border-radius:2px;padding:8px 16px;padding:.8rem 1.6rem;font-family:inherit;font-size:inherit;font-weight:700;text-decoration:none;vertical-align:top;transition:background .1s ease,color .1s ease,border-color .1s ease,box-shadow .1s ease}.pure-button::-moz-focus-inner{padding:0;border:0}.pure-button-hover,.pure-button:hover{background-color:#fff;border-color:#a2a9b1;color:#404244}.pure-button-active,.pure-button:active{background-color:#c8ccd1;border-color:#72777d;color:#000}.pure-button:focus{outline:0;border-color:#36c;box-shadow:inset 0 0 0 1px #36c}.pure-button-primary-progressive{background-color:#36c;border-color:#36c;color:#fff}.pure-button-primary-progressive:hover{background:#447ff5;border-color:#447ff5}.pure-button-primary-progressive:active{background-color:#2a4b8d;border-color:#2a4b8d;box-shadow:none;color:#fff}.pure-button-primary-progressive:focus{box-shadow:inset 0 0 0 1px #36c,inset 0 0 0 2px #fff;border-color:#36c}.pure-form input[type=search]{background-color:#fff;display:inline-block;box-sizing:border-box;border:1px solid #a2a9b1;border-radius:2px;padding:8px;padding:'
>>> r=res.read()
>>> len(r)
66691
>>> r[:50]
b'<!DOCTYPE html>\n<html lang="en" class="no-js">\n<he'
>>>  h=r.decode("utf-8")
 
SyntaxError: unexpected indent
>>> h=r.decode("utf-8")
>>> len(h)
64844
>>> h[:50]
'<!DOCTYPE html>\n<html lang="en" class="no-js">\n<he'
>>> """Httpclient"""
'Httpclient'
>>> import http.client as httplib
>>> con = httplib.HTTPConnection("www.wikipedia.org")
>>> con.request("HEAD","/index.html")
>>> res=con.getresponse()
>>> print(res)
<http.client.HTTPResponse object at 0x000001D8A6814AC0>
>>> print(res.getheaders())
[('Date', 'Wed, 07 Apr 2021 20:17:32 GMT'), ('Server', 'Varnish'), ('X-Varnish', '91027727'), ('X-Cache', 'cp5009 int'), ('X-Cache-Status', 'int-front'), ('Server-Timing', 'cache;desc="int-front", host;desc="cp5009"'), ('Set-Cookie', 'WMF-Last-Access=07-Apr-2021;Path=/;HttpOnly;secure;Expires=Sun, 09 May 2021 12:00:00 GMT'), ('Set-Cookie', 'WMF-Last-Access-Global=07-Apr-2021;Path=/;Domain=.wikipedia.org;HttpOnly;secure;Expires=Sun, 09 May 2021 12:00:00 GMT'), ('X-Client-IP', '2405:201:c024:4031:dc2b:44f6:e78d:f887'), ('Location', 'https://www.wikipedia.org/index.html'), ('Content-Length', '0'), ('Connection', 'keep-alive')]
>>> """SMTP LIB"""
'SMTP LIB'
>>> import smtplib as sp
>>> dir(sp)
['CRLF', 'LMTP', 'LMTP_PORT', 'OLDSTYLE_AUTH', 'SMTP', 'SMTPAuthenticationError', 'SMTPConnectError', 'SMTPDataError', 'SMTPException', 'SMTPHeloError', 'SMTPNotSupportedError', 'SMTPRecipientsRefused', 'SMTPResponseException', 'SMTPSenderRefused', 'SMTPServerDisconnected', 'SMTP_PORT', 'SMTP_SSL', 'SMTP_SSL_PORT', '_MAXLINE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_addr_only', '_fix_eols', '_have_ssl', '_quote_periods', 'bCRLF', 'base64', 'copy', 'datetime', 'email', 'encode_base64', 'hmac', 'io', 'quoteaddr', 'quotedata', 're', 'socket', 'ssl', 'sys']
>>> s_e="krishnaprahladm@gmail.com"
>>> password = input(str("Enter password:"))
Enter password:9676125109@hanuman
>>> s_r=sp.SMTP('smtp.gmail.com',587)
>>> s_r.starttls()
(220, b'2.0.0 Ready to start TLS')
>>> s_r.login(s_e,password)
(235, b'2.7.0 Accepted')
>>> 
