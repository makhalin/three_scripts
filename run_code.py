__all__ = ['run_code']

def run_code():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen, build_opener, install_opener
    from urllib.parse import urlencode

    opener = build_opener()    
    opener.addheaders = [("User-agent", "Chrome/23.0")]
    post_params = {
        'lang' : 'Python',
        'code': '''print('1')''',
        'run' : True,
        'submit': True
            }
    post_args = urlencode(post_params)
    link = 'http://codepad.org/'
    fp = opener.open(link, post_args.encode('utf-8')).read()
    open('1.htm', 'wb').write(fp)

if __name__ == "__main__":
    run_code()
