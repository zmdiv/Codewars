'''Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
omain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

def domain_name(url):
    starters = ['http://', 'www.', 'https://']
    for a in starters:
        url = url.replace(a, '')
    url = url.split('.', 1)[0]
    return url
