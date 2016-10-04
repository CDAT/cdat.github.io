import os
import vcs
import cdms2
import EzTemplate
import cdutil

vcs.download_sample_data_files()

def spaghetti_plot(variables, template=None, min_y=None, max_y=None, left_label=None, right_label=None, tick_sides=None, line="default", marker="default", x_labels="*", y_labels="*", canvas=None):
    """
    This file is ready to be imported by your scripts, and you can just call this function.

    Sample usage is below.

    variables: List of variables to plot
    template: The template to use as the base for the plot.
    min_y: If you want to adjust the y axis bounds, you can set a minimum value. Will be derived from data if not specified.
    max_y: If you want to adjust the y axis bounds, you can set a maximum value. Will be derived from data if not specified.
    left_label: Text to put on the left Y axis
    right_label: Text to put on the right Y axis
    tick_sides: A list of "left" or "right" values indicating which side of the chart you want the variable axes to be displayed.
    line: A line object or name of a line object used to describe the lines plotted. Set to None to hide.
    marker: A marker object or name of a marker object used to describe the markers plotted. Set to None to hide.
    x_labels: Dictionary for setting axis tick labels
    y_labels: Dictionary for setting axis tick labels
    """
    if canvas is None:
        canvas = vcs.init()

    if isinstance(template, (str, unicode)):
        template = vcs.gettemplate(template)

    if template is None:
        # Use our custom default template for 1ds
        template = vcs.createtemplate()
        # Shrink the template a bit
        template.scale(.78, "x")
        template.move(.02, "x")
        template.yname.x = .01
        template.data.y1 = .1
        template.box1.y1 = .1
        ticlen = template.xtic1.y2 - template.xtic1.y1
        template.xtic1.y1 = template.data.y1
        template.xtic1.y2 = template.xtic1.y1 + ticlen
        template.xtic2.priority = 0
        template.xlabel1.y = template.xtic1.y2 - .01
        template.legend.x1 = template.data.x2 + (1 - template.data.x2) / 3.
        template.legend.x2 = .95
        template.legend.y1 = template.data.y1
        template.legend.y2 = template.data.y2
        template.yname.y = (template.data.y1 + template.data.y2)/2.
        template.xname.y = template.xlabel1.y - .05

    # The labels don't make any sense with multiple values; hide them.
    template.min.priority = 0
    template.max.priority = 0
    template.mean.priority = 0
    template.dataname.priority = 0
    templates = EzTemplate.oneD(len(variables), template=template)
    templates.x = canvas

    if tick_sides is None:
        tick_sides = ["left"] * len(variables)

    clean_ticks = []
    for t in tick_sides:
        if t.lower() not in ('left', 'right'):
            raise ValueError("tick_sides must be a list of 'left' or 'right' values; found '%s'." % t)
        clean_ticks.append(t.lower())

    tick_sides = clean_ticks
    if len(tick_sides) < len(variables):
        tick_sides += tick_sides[-1:] * len(variables)

    # Store min/max per side for appropriate scaling
    min_vals = {"left": min_y, "right": min_y}
    if min_y is None:
        for i, var in enumerate(variables):
            v_min = min(var)
            min_y = min_vals[tick_sides[i]]
            if min_y is None or min_y > v_min:
                min_vals[tick_sides[i]] = v_min

    max_vals = {"left": max_y, "right": max_y}
    if max_y is None:
        for i, var in enumerate(variables):
            v_max = max(var)
            max_y = max_vals[tick_sides[i]]
            if max_y is None or max_y < v_max:
                max_vals[tick_sides[i]] = v_max

    if isinstance(line, (str, unicode)):
        line = vcs.getline(line)
    if isinstance(marker, (str, unicode)):
        marker = vcs.getmarker(marker)

    to_pad = []
    if line is not None:
        widths = line.width
        to_pad.append(widths)

        styles = line.type
        to_pad.append(styles)

        colors = line.color
        to_pad.append(colors)

    if marker is not None:
        markers = marker.type
        to_pad.append(markers)

        marker_colors = marker.color
        to_pad.append(marker_colors)

        marker_sizes = marker.size
        to_pad.append(marker_sizes)

    for padded in to_pad:
        if len(padded) < len(variables):
            padded += padded[-1:] * (len(variables) - len(padded))

    for n in range(len(variables)):
        gm = vcs.create1d()

        if line is not None:
            gm.line = styles[n]
            gm.linewidth = widths[n]
            gm.linecolor = colors[n]
        else:
            gm.linewidth = 0

        if marker is not None:
            gm.marker = markers[n]
            gm.markersize = marker_sizes[n]
            gm.markercolor = marker_colors[n]
        else:
            gm.marker = None

        gm.datawc_y1 = min_vals[tick_sides[n]]
        gm.datawc_y2 = max_vals[tick_sides[n]]

        template = templates.get(n)
        gm.xticlabels1 = x_labels
        if tick_sides[n] == "left":
            if tick_sides.index("left") == n:
                template.ylabel1.priority = 1
                if left_label is not None:
                    template.yname.priority = 0
                    left_text = vcs.createtext(Tt_source=template.yname.texttable, To_source=template.yname.textorientation)
                    left_text.x = template.yname.x
                    left_text.y = template.yname.y
                    left_text.string = [left_label]
                    templates.x.plot(left_text)
            else:
                template.ylabel1.priority = 0
                template.yname.priority = 0
            template.ylabel2.priority = 0
            gm.yticlabels1 = y_labels
            gm.yticlabels2 = ""
        else:
            template.ylabel1.priority = 0
            if tick_sides.index("right") == n:
                template.ylabel2.priority = 1
                if right_label is not None:
                    right_text = vcs.createtext(Tt_source=template.yname.texttable, To_source=template.yname.textorientation)
                    right_text.x = template.data.x2 + (template.data.x1 - template.yname.x)
                    right_text.y = template.yname.y
                    right_text.string = [right_label]
                    templates.x.plot(right_text)
            else:
                template.ylabel2.priority = 0
            gm.yticlabels1 = ""
            gm.yticlabels2 = y_labels
        if n != 0:
            template.xlabel1.priority = 0
            template.xname.priority = 0

        var = variables[n]
        templates.x.plot(var, gm, template)
    return templates.x

if __name__ == "__main__":
    # A quick example on how to use the above function
    f = cdms2.open(os.path.join(vcs.sample_data, "tas_ccsr-95a.xml"))

    variables = []
    for i in range(6):
        tas = f("tas", slice(i*12, (i+1)*12))  # Extract one year
        # Assign an ID that will distinguish the years
        tas.id = "tas_%i" % tas.getTime().asComponentTime()[0].year
        # Manipulating the variable changes the id; we'll save it here.
        saved_id = tas.id
        # Make sure the data is bounded before averaging
        cdutil.setTimeBoundsMonthly(tas)
        var = cdutil.averager(tas(squeeze=1), axis="xy")
        var = cdutil.ANNUALCYCLE.climatology(var)
        var.id = saved_id
        variables.append(var)

    # Customize the lines used to draw the plots
    line = vcs.createline()
    line.width = 2
    line.color = ["red", "blue", "salmon", "medium aquamarine", "orange", "chartreuse"]
    line.type = ["dot", "dash", "dash-dot", "long-dash", "solid", "dash"]

    # Customize the markers drawn
    marker = vcs.createmarker()
    marker.size = 6
    # You can just use the same colors as the lines
    marker.color = line.color
    marker.type = ["triangle_up", "plus", "diamond", "circle", "cross", "triangle_down"]

    # Middle of the month (from the time axis)
    months = {
              15.5: "Jan",
              45.0: "Feb",
              74.5: "March",
              105.0: "April",
              135.5: "May",
              166.0: "June",
              196.5: "July",
              227.5: "Aug",
              258.0: "Sep",
              288.5: "Oct",
              319.0: "Nov",
              349.5: "Dec"
            }

    # While there are a lot of options, you can rely on most of the defaults to make a nice plot.
    canvas = spaghetti_plot(variables, x_labels=months, left_label="Temperature (K)", line=line, marker=marker)

    f.close()

    # Make a nice title label
    title = vcs.createtext()
    title.halign = "center"
    title.valign = "top"
    title.height = 20
    title.string = ["Surface Temperature Averages"]
    title.x = .5
    title.y = .95
    title.font = "Clarendon"
    canvas.plot(title)

    canvas.png("TAS_spaghetti")