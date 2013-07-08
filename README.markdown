# hyde-bootstrap
A modification of [twitter/bootstrap][] for use with [hyde/hyde][].

This is a fork of [auzigog/hyde-bootstrap][] with some additions and
modifications to cooperate with [aims-group/webshooter][].

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

### Bootstrap dropdown menus
Generating Bootstrap's native dropdown menus programmatically is supported in
`site.yaml`. To make a navigation link a dropdown menu, just put a list of links
where you'd normally put a URL:

    context:
        data:
            menu:
                - title: Home
                  url: index.html
                - title: About
                  url: about.html
                - title: Related projects
                  url:
                    - title: Project Red
                      url: project_red.html
                    - title: Project Blue
                      url: project_blue.html

Currently this is not supported recursively.

### Custom Templates
To make real use of this package, you will need to create your own templates.

You can subclass `topbar.j2` or `base.j2` to cover most use cases. All of the
templates that are provided serve as a starting point and as an example of
possible approaches you can use.

### Adding Content
Look at all of the `.html` files in the `content` directory for an example of
how to begin adding your own content.

### Adding CSS
To extend the CSS of a given page, use the `{% block css %}{% endblock %}`
block. You can do this with a `<style>` block or a `<link>` to a CSS file.

### Publishing
To publish the site, first edit site.yaml to match your preferred publishing
(github, sftp, etc). See the Hyde README for details. Then run

    hyde publish -c prod.yaml

Use prod.yaml makes it easy to switch your `site.config.mode` variable to
`"production"` which can enable production-only elements of your site. In the
default hyde-bootstrap setup, analytics is only rendered in production mode.

## Versions
Built using:

  * [Hyde][hyde/hyde] [0.8.7](http://github.com/hyde/hyde/tree/696adac061ff040d5c5be1c629c94975c146f32a)
  * [Bootstrap][twitter/bootstrap] [2.3.2](http://github.com/twitter/bootstrap/tree/d9b502dfb876c40b0735008bac18049c7ee7b6d2)


## Notes
* There's a bit of code mixed in from the [h5bp/html5-boilerplate][] project for
  jQuery and and IE PNG fix.
* To update the js and css files of bootstrap to newer versions, run
  `./update-bootstrap-libs.sh`


## Credits
Built by [Jeremy Blanchard](http://blanchardjeremy.com).
Contributions by [Anand S](https://github.com/anandtrex).

[hyde/hyde]: https://github.com/hyde/hyde
[twitter/bootstrap]: https://github.com/twitter/bootstrap
[aims-group/webshooter]: https://github.com/aims-group/webshooter
[auzigog/hyde-bootstrap]: https://github.com/auzigog/hyde-bootstrap
[h5bp/html5-boilerplate]: https://github.com/h5bp/html5-boilerplate
