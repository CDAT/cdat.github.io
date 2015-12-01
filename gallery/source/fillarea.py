import vcs


canvas = vcs.init()

base_fill = canvas.createfillarea("solid")
base_fill.x = []
base_fill.y = []
base_fill.color = []

number_of_fills = 20

fill_width = 1.0 / (1.5 * number_of_fills + .5)
offset_width = fill_width / 2.

offset_height = offset_width
fill_height = (1.0 - offset_height * 4.) / 3.

for i in range(number_of_fills):
    x1 = offset_width + offset_width * i + fill_width * i
    x2 = x1 + fill_width
    y1 = offset_height
    y2 = y1 + fill_height
    # Describe the points of the rect clockwise
    base_fill.x.append([x1, x1, x2, x2])
    base_fill.y.append([y1, y2, y2, y1])
    # Pick a color from the middle of the range
    base_fill.color.append(20 + (i * (200 / number_of_fills)))

# Inherit from the base_fill so we only need to adjust a few things
pattern_fill = canvas.createfillarea("pattern", "solid")

for i in range(number_of_fills):
    pattern_fill.y[i] = [y + offset_height + fill_height for y in pattern_fill.y[i]]

pattern_fill.style = "pattern"
pattern_fill.index = range(1, 21)

# Inherit from the base_fill so we only need to adjust a few things
hatch_fill = canvas.createfillarea("hatch", "pattern")

for i in range(number_of_fills):
    hatch_fill.y[i] = [y + offset_height + fill_height for y in hatch_fill.y[i]]
hatch_fill.style = "hatch"

canvas.plot(base_fill)
canvas.plot(pattern_fill)
canvas.plot(hatch_fill)

canvas.png("pattern_chart")
