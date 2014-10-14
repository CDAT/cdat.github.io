from hyde.model import Expando
from jinja2 import environmentfilter
import misaka

default_gfm = {
    "tables": True,
    "autolink": True,
    "lax_html": False,
    "strikethrough": True,
    "internal_emphasis": True,
    "space_headers": True,
    "superscript": True,
    "code_fence":True,
}

gfm_keys = {
    "tables": misaka.EXT_TABLES,
    "code_fence": misaka.EXT_FENCED_CODE,
    "autolink": misaka.EXT_AUTOLINK,
    "lax_html": misaka.EXT_LAX_HTML_BLOCKS,
    "strikethrough": misaka.EXT_STRIKETHROUGH,
    "internal_emphasis": misaka.EXT_NO_INTRA_EMPHASIS,
    "space_headers": misaka.EXT_SPACE_HEADERS,
    "superscript": misaka.EXT_SUPERSCRIPT
}

@environmentfilter
def gfm(env, value):
    """
    Github-flavored Markdown filter with support for extensions.
    """
    output = value
    
    d = 0
    
    # Expando converts a dict into an object
    gfm = getattr(env.config, "gfm", Expando({}))

    for (field, value) in default_gfm.iteritems():
        val = getattr(gfm, field, value)
        if val:
            d |= gfm_keys[field]


    renderer = misaka.HtmlRenderer()
    marked = misaka.Markdown(renderer, d)

    rendered = marked.render(output)

    if hasattr(gfm, 'table_class'):
        table_tag = "<table class='%s'>" % gfm.table_class
        return rendered.replace("<table>", table_tag)
    else:
        return rendered
