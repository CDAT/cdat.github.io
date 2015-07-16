from hyde.model import Expando
from jinja2 import environmentfilter
import misaka

default_gfm = {
    "tables": True,
    "autolink": True,
    "lax_html": True,
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

from xml.sax.saxutils import escape, unescape
 # escape() and unescape() takes care of &, < and >.
html_escape_table = {
    '"': "&quot;",
    "'": "&apos;"
}

html_unescape_table = {v:k for k, v in html_escape_table.items()}

def html_escape(text):
    return escape(text, html_escape_table)

def html_unescape(text):
    return unescape(text, html_unescape_table)

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
        rendered = rendered.replace("<table>", table_tag)
    

    if hasattr(gfm, "raw_delimiters"):
        retrieve = gfm.raw_delimiters

        updated = rendered

        for delimiters in retrieve:
            print delimiters
            start = html_escape(delimiters.start)
            stop = html_escape(delimiters.stop)

            ind = updated.find(start)
            while ind != -1:
                end = updated.find(stop, ind)
                
                if end == -1:
                    # I don't know why this works, but it totally does
                    # I guess probably because the [:] operator passes the sides to a function, 
                    # which probably uses *args, and undefined args are None?
                    end = None
                else:
                    end += len(stop)

                substr = updated[ind:end]
                
                if end is not None:
                    updated = updated[0:ind] + html_unescape(substr) + updated[end:]
                else:
                    updated = updated[0:ind] + html_unescape(substr)
                
                if end is not None:
                    ind = updated.find(start, end)
                else:
                    ind = -1

        if updated != rendered:
            print updated
            rendered = updated

    return rendered