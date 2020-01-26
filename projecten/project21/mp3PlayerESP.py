from machine import Pin
from networking import wifi, socketServer
from mp3PlayerMod import mp3Player

def selectCommando(mp3, commando):
    print(commando)
    command = commando.split(":")
    if command[0] == 'play':
        if len(command) == 1:
            mp3.play()
        else:
            mp3.playTrack(int(command[1]))
    elif command[0] == 'pause':
        mp3.pause()
    elif command[0] == 'stop':
        mp3.stop()
    elif command[0] == 'next':
        mp3.next()
    elif command[0] == 'prev':
        mp3.prev()
    elif command[0] == 'vol+':
        mp3.volumeStepUp()
    elif command[0] == 'vol-':
        mp3.volumeStepDown()
    elif command[0] == 'vol':
        waarde = int(command[1])
        volume = int(waarde * 30.0 / 100.0)
        mp3.setVolume(volume)

        
def app():
    # connecteren met netwerk
    wifi.connectWIFI()
    if socketServer.start() == False:
        wifi.disconnectWIFI()
        return 0

    # initialisatie mp3 player
    mp3 = mp3Player()
    mp3.start()
        
    while True:
        status = socketServer.waitCn()
        if status < 0:
            print("Wrong command")
        elif status == 0:
            print("Halt ESP")
            break
        else:
            socketServer.sendData("OK")
            res = socketServer.readData()
            selectCommando(mp3, res)
            socketServer.sendData("OK")
            socketServer.stopClient()

    wifi.disconnectWIFI()
    
app()
