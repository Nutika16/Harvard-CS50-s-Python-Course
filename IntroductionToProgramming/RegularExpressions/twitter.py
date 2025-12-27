'''In this we are going to extract the username from the twitter url'''

# url = input("url: ").strip()

# username = url.replace("https://twitter.com/" , "")

# print(f"Username: {username}")

'''The above program literally broke in many cases like if you use http protocol instead of https or write a sentence 
before defining the url and many more. '''

import re 

url = input("url: ").strip()


'''While using this re.sub it will work fine with twitter url but what if user type something like www.google.com or any other url then it will print the same thing as username'''

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/" , "" , url)

# print(f"Username: {username}")

'''Therefore, we are going to use the re.search with condition'''

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url , re.IGNORECASE):
    print(f"Username:" ,matches.group(1))