let socket = io.connect("http://127.0.0.1:5001/device")
let room = "seahawk"
//This is a hardcoded uid of the restaurant

socket.on("connect",()=>{socket.send(room)})

socket.on("test",(m)=>{console.log(m)})

