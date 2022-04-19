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
    return pipe.readline().strip()

def handle_pipe(player, message):
    print("Msg :", message, message[-4:])
    if message[-4:].lower() == ".mp3":
        print("queue")
        player.queue(pyglet.media.load(message, streaming=False))

def handle_player(player):
    player.play()

def main():
    pipe = pipe_open()
    player = pyglet.media.Player()

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
