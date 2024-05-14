import re

def extract_url_info(url):
    pattern = r'<[a-z]+>https?://([a-z0-9._]+)</[a-z]+>'
    
    match = re.match(pattern, url, flags=re.IGNORECASE)
    return match.group(1)

url = "<SSL>https://xcd32112.smart_meter.com</SSL>"
output = extract_url_info(url)
print(output)
