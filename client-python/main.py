import socketio
import asyncio
import aioconsole
from os import system

username=""
io=socketio.AsyncClient()

async def main():
    try:
        await io.connect("http://localhost:8080")
        await io.wait()
    except:
        await io.disconnect()


@io.on("new-user")
async def new_user():
    global username
    print("Welcom to our Chat !!!")
    username=input("Your username : ")
    await io.emit("subscribe",username)

@io.on("subscribe-error")
async def err():
    global username
    system("cls")
    print("User already exists !!!")
    username=input("Your username : ")
    await io.emit("subscribe",username)

@io.on("leave")
async def disconnect():
    await io.disconnect()
    print("--------------Bye--------------")

@io.on("refresh")
async def refesh(data):
    global username
    system("cls")
    print(username)
    print("-----------------------MSG-----------------------")
    for o in data:
        print("{} : {}".format(o['sender'],o['msg']))
    print("-------------------------------------------------")
    msg=await aioconsole.ainput("Message (\q for quit) : ")
    if(msg=="\q"):
        print("--------------Disconnect--------------")
        await io.emit("leave-chat",username)
    else:
        await io.emit("message",{
            "sender":username,
            "msg":msg
        })

if __name__=="__main__":
    asyncio.run(main())