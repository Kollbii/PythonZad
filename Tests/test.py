import requests

for i in range(30,40):
    req = requests.get("http://rekru.kn-bit-cyber.ninja/division?id="+str(i)+"")
    print (req.status_code)
    print (req.text)

#Fajna flaga z tego IDORA 35

print("More Code Test To Git")