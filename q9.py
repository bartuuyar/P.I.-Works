import re

def extract_url_info(url):
    #regular expression to capture pattern
    pattern = r'<[a-z]+>https?://([a-z0-9._]+)</[a-z]+>'
    
    match = re.match(pattern, url, flags=re.IGNORECASE)
    return match.group(1)

url = "<url>https://xcd32112.smart_meter.com</url>"
output = extract_url_info(url)
print(output)
