let socket = io.connect(window.origin +"/restaurant")
let room = window.location.pathname.split("/")[2]

socket.on("connect",()=>{socket.send(room)})

socket.on("test",(m)=>{console.log(m)})


// we look for "queue" in local storage and if not found then we create two key value pairs
if (!localStorage.getItem("queue")){
	localStorage.setItem("queue",0)
	localStorage.setItem("orders",[])
}
