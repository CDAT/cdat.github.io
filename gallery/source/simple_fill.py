import vcs

canvas = vcs.init()

# Draw a white stripe and a dark grey stripe across the canvas
bg_boxes = canvas.createfillarea("bg")
bg_boxes.x = [[0, 0, 1, 1], [0, 0, 1, 1]]
bg_boxes.y = [[.5, 1, 1, .5], [0, .5, .5, 0]]
bg_boxes.color = [(25, 25, 25), "white"]

offset = 1 / 24.
box_width = (1. - offset * 4) / 3.
box_height = (1 - offset * 3) / 2.

# Draw solid colored partially transparent
solid_boxes = canvas.createfillarea("solid")

# Make sure the relevant boxes are drawn on top
solid_boxes.priority = 2
solid_boxes.x = [[offset, offset, offset + box_width, offset + box_width]] * 2
solid_boxes.y = [[offset, offset + box_height, offset + box_height, offset],
                 [offset * 2 + box_height, offset * 2 + box_height * 2, offset * 2 + box_height * 2, offset * 2 + box_height]]

solid_boxes.color = [25, 25]
solid_boxes.opacity = [50, 50]

pattern_boxes = canvas.createfillarea("pattern", "solid")
pattern_boxes.priority = 2
# Move boxes to the right
middle_x = [
    offset * 2 + box_width,
    offset * 2 + box_width,
    offset * 2 + box_width * 2,
    offset * 2 + box_width * 2,
]

pattern_boxes.x = [middle_x] * 2

pattern_boxes.style = "pattern"
# Refer to http://uvcdat.llnl.gov/examples/pattern_chart.html for a list of patterns
pattern_boxes.index = 9
pattern_boxes.opacity = [50, 50]

hatch_boxes = canvas.createfillarea("hatch", "pattern")
hatch_boxes.priority = 2

# Move boxes to the right
right_x = [
    offset * 3 + box_width * 2,
    offset * 3 + box_width * 2,
    offset * 3 + box_width * 3,
    offset * 3 + box_width * 3,
]

hatch_boxes.x = [right_x] * 2
hatch_boxes.style = "hatch"

canvas.plot(bg_boxes)
canvas.plot(solid_boxes)
canvas.plot(pattern_boxes)
canvas.plot(hatch_boxes)

canvas.png("simple_fill")