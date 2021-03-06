from urllib.parse import urlparse


def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        if len(results > 2):
            return results[-3] + '.' + results[-2] + '.' + results[-1]
        else
            return ''
    except:
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

