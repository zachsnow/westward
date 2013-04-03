# Whistling Westward

**This is not actually done. At all.**

The Tumblr theme for [Whistling Westward](http://whistlingwestward.com/), by
[Zach Snow](http://zachsnow.com/).

**Note** If you just want to use the theme as-is, simply download the
[main theme](https://github.com/zachsnow/whistlingwestward/tree/master/output/index.html)
and [iphone theme](https://github.com/zachsnow/whistlingwestward/tree/master/output/iphone-theme.html).
For instructions on how to install these files, see [Installation](#installing),
below.

## <a name="dependencies"></a>Dependencies

To build the theme manually -- for instance, if you'd like to tweak
it -- you'll need to install the following dependencies:

  * [Sass](http://sass-lang.com/)
  * [Jinja2](http://www.pocoo.org/projects/jinja2/#jinja2)

Assuming you have [Homebrew](http://mxcl.github.com/homebrew/) and
[Pip](http://www.pip-installer.org/en/latest/) installed, you should
be able to simply run the following:

    $ brew install sass
    $ pip install jinja2

## <a name="building"></a>Building

To build the theme first make sure you've installed all of the
[Dependencies](#dependencies). Then, run the following command from the
root of this repository.

    $ python build.py
    
This will generate 2 files: `output/index.html` and `output/iphone-theme.html`.

## <a name="installing"></a>Installing

Once you have `index.html` and `iphone-theme.html` in hand, you just
need to install them on [Tumblr](http://tumblr.com). Login to Tumblr
and go to **Settings**. Select the blog you'd like to edit from the left
column, then click **Customize**.

First you need to setup your main theme. Click **Edit HTML** and overwrite
the existing HTML with the contents of `index.html`, then **Update Preview**
to see how it looks. Assuming you are happy with the result, **Save** it.

Next you need to set up a the custom mobile theme by creating a page with
the URL `/iphone-theme/`. Click **Add a page** and select **Custom Layout**
from the dropdown menu. Give the page a URL of `/iphone-theme/`, and then
set the **Custom HTML** to the contents of `iphone-theme.html`.
