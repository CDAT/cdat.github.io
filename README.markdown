# uvcdat-site
This is the in-development new [UV-CDAT.org]. It was generated with
[Webshooter][aims-group/webshooter] and runs on [Hyde][hyde/hyde]. It uses
[hyde-bootstrap][aims-group/hyde-bootstrap] as a starting point.


## Usage
You'll need to have Hyde to run this (`pip install hyde`). Once you do, just

    hyde gen

in this directory, then open `deploy/index.html` in a web browser.
Alternatively, run `hyde serve` to run a webserver with `deploy` as the root
directory.

## Editing
There are a variety of templates that you can subclass using
`{% extends "templatename.j2" %}` on the top of your article or post.

  * `base.j2` contains the bulk of the layout logic, but not the best for
    subclassing because it doesn't have any grid attached to it.
  * `columns.j2` has a main content area and a sidebar with links to content
    within the page.
  * `topbar.j2` adds a top bar to the base layout
  * `hero.j2` places the bootstrap "hero" area on the page (good for a home
    page)

### Adding Content
Look at all of the `.html` files in the `content` directory for an example of
how to begin adding your own content.

### Adding CSS
To extend the CSS of a given page, use the `{% block css %}{% endblock %}`
block. You can do this with a `<style>` block or a `<link>` to a CSS file.

[hyde/hyde]: https://github.com/hyde/hyde
[twitter/bootstrap]: https://github.com/twitter/bootstrap
[aims-group/webshooter]: https://github.com/aims-group/webshooter
[aims-group/hyde-bootstrap]: https://github.com/aims-group/hyde-bootstrap
[auzigog/hyde-bootstrap]: https://github.com/auzigog/hyde-bootstrap
[h5bp/html5-boilerplate]: https://github.com/h5bp/html5-boilerplate
[uv-cdat.org]: http://uv-cdat.org/
