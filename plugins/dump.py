from jinja2 import environmentfilter, escape

@environmentfilter
def dump(env, value):
    lines = []
    lines.append("%s" % value)
    for field in dir(value):
        lines.append("%s:%s" % (field, getattr(value, field)))
    return escape("\n".join(lines))