# import pyglet
# audio = pyglet.media.load("8d3b1fa30e92ead.mp3")
# audio.play()
from audioplayer import AudioPlayer
AudioPlayer("8d3b1fa30e92ead.mp3").play(block=True)
