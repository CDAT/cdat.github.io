import vcs

fill = vcs.createfillarea()

# A simple example to show the different ways you can specify a color
# X11 Color Names, colormap index, RGBA, RGB
fill.color = ["red", 242, (100, 0, 0, 100), (100, 0, 0)]

fill.x = [[0, 0, .5, .5], [0, 0, .5, .5], [.5, .5, 1, 1], [.5, .5, 1, 1]]
fill.y = [[0, .5, .5, 0], [.5, 1, 1, .5], [.5, 1, 1, .5], [0, .5, .5, 0]]
canvas = vcs.init()
canvas.plot(fill)
canvas.png("color")