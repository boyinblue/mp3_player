import pyglet
import time
import os

pipe_path = "/tmp/mp3_player"

def pipe_open():
    if not os.path.exists(pipe_path):
        os.mkfifo(pipe_path)
    os.chmod(pipe_path, 0o666)
    pipe_fd = os.open(pipe_path, os.O_RDONLY | os.O_NONBLOCK)
    return os.fdopen(pipe_fd)

def read_pipe(pipe):
    return pipe.readline()

def handle_pipe(player, message):
#    print("msg :", message)
    message = message.strip()
    print("Msg :", message, message[-4:])
    if message[-4:].lower() == ".mp3":
        print("queue")
        player.queue(pyglet.media.load(message))
    elif message == "next":
        print("next")
        player.next_source()

def handle_player(player):
    if not player.playing:
        print("Play!")
    player.play()

def on_eos():
    print("on_eos()")

def on_player_eos():
    print("on_player_eos()")

def on_player_next_source():
    print("on_player_next_source()")

def main():
    pipe = pipe_open()
    player = pyglet.media.Player()
    player.on_eos = on_eos
    player.on_player_eos = on_player_eos
    player.on_player_next_source = on_player_next_source

    try:
        while True:
            handle_player(player)
            message = read_pipe(pipe)
            if message:
                handle_pipe(player, message)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

def main2():
    try:
        while True:
            pyglet.app.run()
            if not music.playing:
                print("Music End")
                exit(0)
        time.sleep(0.1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
