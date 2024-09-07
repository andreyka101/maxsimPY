
# from audioplayer import AudioPlayer
# AudioPlayer("8d3b1fa30e92ead.mp3").play(block=True)

s = ""
for x in range(10):
    for y in range(10):
        s += str(x) + str(y)+"  "
    print(s)
    s = ""