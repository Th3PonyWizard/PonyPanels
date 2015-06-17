import requests
file = open("paths.txt", "r")
url = raw_input("Enter URL: ")
for line in file.readlines():
	url2 = url + line
	if(requests.get(url2.rstrip()).status_code == 404):
		print "Failed: " + str(requests.get(url + line).status_code) + " / " + url + line
	else:
		print line + "=" + "Nailed"
		break