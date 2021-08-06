let socket = io.connect(window.origin +"/device")
let room = window.location.pathname.split("/")[2]

socket.on("connect",()=>{socket.send(room)})

socket.on("test",(m)=>{console.log(m)})

