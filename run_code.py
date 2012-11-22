__all__ = ['run_code']

def run_code():
    args = args_parser()
    codepad(args['lang'], args['code'])

def args_parser():
    import argparse

    parser = argparse.ArgumentParser(description='''
                                                 It is an online compiler/interpreter (http://codepad.org/)
                                                 Languages: C, C++, D, Haskell, Lua, OCaml, PHP, Perl, Plain Text, Python, Ruby, Scheme, Tcl.
                                                ''')
    parser.add_argument("code", type=str, help="File name with code")
    parser.add_argument("lang", type=str, help="Language")
    
    args = vars(parser.parse_args())
    
    return args

def codepad(lang, file):
    from urllib.request import urlopen, build_opener
    from urllib.parse import urlencode
    from bs4 import BeautifulSoup

    code = open(file, encoding='utf-8').read()
    opener = build_opener()    
    opener.addheaders = [("User-agent", "Chrome/23.0")]
    post_params = {
        'lang' : lang,
        'code': code,
        'private' : True,
        'run' : True,
        'submit': True
            }
    post_args = urlencode(post_params)
    link = 'http://codepad.org/'
    try:
        fp = opener.open(link, post_args.encode('utf-8')).read()
    except:
        print("Error: No such language. Available language: C, C++, D, Haskell, Lua, OCaml, PHP, Perl, Plain Text, Python, Ruby, Scheme, Tcl.")
        return
    soup = BeautifulSoup(fp)
    i = soup.findAll('td', {'width':'100%'})
    print("Output:\n%s" % i[1].text.strip())

if __name__ == "__main__":
    run_code()
