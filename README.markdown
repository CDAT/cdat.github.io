## uvcdat-site
This is the new [UV-CDAT website]. It was generated with
[Webshooter][aims-group/webshooter] and runs on [Hyde][hyde/hyde]. It uses
[hyde-bootstrap][aims-group/hyde-bootstrap] as a starting point.

## Usage

### Dependencies
* [Hyde][hyde/hyde] (`pip install hyde` with Python >= 2.7)

If you're getting errors when running even `hyde --version`, and you installed
it using `pip install hyde`, you probably used a pip for Python 2.6 or
earlier. Remove Hyde and install it using a Python 2.7 or higher pip.

### First run

    git clone https://github.com/UV-CDAT/uvcdat-site.git
    cd uvcdat-site
    hyde gen

Then open `deploy/index.html` in a web browser. Alternatively, run `hyde serve` from here to run a webserver with `deploy` as the root directory.

## Adding/editing content
Content is stored in, where else, `content/`. Each page is an HTML file and can
be written (with some exceptions) entirely in HTML or [Markdown][] (the latter
is preferred), or in some combination of the two.

Each page extends a layout template from `layouts/`. You'll usually just extend
`topbar.j2`, which puts the navbar in place then gives you the rest of the page
for whatever. See some existing pages for examples.

  To get a page on the navbar, edit `site.yaml` and add the page as a list item
  in `context->data->menu`. Make sure your indentation follows that of the other
  list items. A navigation item is just a two-item dict with a string `title` and
  a string or list `url`. If `url` is a list, the nav item will be a dropdown
  menu (and its contents will be read exactly like the contents of `menu` -- a
  two-item dict -- except that the URLs can't be lists this time). Otherwise, it
  will just be a link.

### Layout templates
There are a variety of templates that you can subclass using
`{% extends "templatename.j2" %}` on the top of your article or post.

* `base.j2` contains the bulk of the layout logic, but not the best for
  subclassing because it doesn't have any grid attached to it.
  * `columns.j2` has a main content area and a sidebar with links to content
    within the page.
    * `topbar.j2` adds a top bar to the base layout
    * `hero.j2` places the bootstrap "hero" area on the page (good for a home
      page)

    Look at all of the `.html` files in the `content` directory for an example of
    how to begin adding your own content.

### Adding CSS
To extend the CSS of a given page, use the `{% block css %}{% endblock %}`
block. You can do this with a `<style>` block or a `<link>` to a CSS file.

[uv-cdat website]:           http://uv-cdat.llnl.gov/
[aims-group/webshooter]:     http://github.com/aims-group/webshooter
[hyde/hyde]:                 http://github.com/hyde/hyde
[aims-group/hyde-bootstrap]: http://github.com/aims-group/hyde-bootstrap
[hyde docs]:                 http://hyde.github.io/install.html
[markdown]:                  http://daringfireball.net/projects/markdown/
