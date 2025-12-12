#import sys

#try:
#print("hello, my name is", sys.argv[1])
#except IndexError:
    #print("Too few arguments")

# to run 
# python name.py martins


#import sys

# Check for errors 
#if len(sys.argv) < 2:
 #   print("Too few arguments" )
#elif len(sys.argv) > 2:
  #  print("Too many arguments")
    # Print name tags
#else:
 #   print("hello, my name is", sys.argv[1])


# using sys.exit
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments" )
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    
else:
    print("hello, my name is", sys.argv[1])

# python can take twonames and run it like that by just using dobule quotes such as"Martins Odeshina" if using argv

# APIs third party
# requests allow to make web requests pypi.org/projects/requests
# Apple have thier own api 
# JSON 
# 

# import json
# import requests
#import sys
# 
# 
# if len(sys.argv) != 2: 
#    sys.exit()
# 
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[2])
# print(json.dumps(respons.json(), indent=2))
# 
# o = response.json()
# for result in o["results"]:
#     print(results["trackName"])
# #


