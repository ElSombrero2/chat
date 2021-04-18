const express = require('express')
const app = express()
const server = require('http').Server(app)
const io = require('socket.io')(server)

const model={
    users:[],
    messages:[]
}

function refreshAll(socket){
    socket.broadcast.emit("refresh",model.messages)
    socket.emit("refresh",model.messages)
}

io.on("connection",(socket)=>{
    
    socket.emit("new-user")

    socket.on("subscribe",(username)=>{
        if(model.users.includes(username))
            socket.emit("new-user")
        else{
            model.users.push(username)
            model.messages.push({
                sender:"[server]",
                msg:"New User Connected : "+username+"."
            })
            refreshAll(socket)
        }
    })
    
    socket.on("leave-chat",(username)=>{
        model.messages.push({
            sender:'[server]',
            msg:username+" left the chat."
        })
        model.users.splice(model.users.indexOf(username),1)
        socket.broadcast.emit("refresh",model.messages)
        socket.emit("leave")
    })

    socket.on('refresh',()=>{
        socket.emit("refresh",model.messages)
    })

    socket.on("message",(obj)=>{
        model.messages.push(obj)
        refreshAll(socket)
    })

})


io.listen(process.env.PORT || 8080)