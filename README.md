# Westward

**Westward** is the Tumblr theme for [Whistling Westward](http://whistlingwestward.com/),
photography by Molly Peppel Snow. It was made by [Zach Snow](http://zachsnow.com/).
Westward is still very much a work in progress; for an example that shows how it looks
so far, for various post types, see [that's me](http://therealzachsnow.tumblr.com).

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
set the **Custom HTML** to the contents of `iphone-theme.html`. Note
that as of now the mobile theme is the exact same as the main theme, so
you really don't need to do this step for now.

## <a name="configuring"></a>Configuring

Now that the theme is installed, you need to configure it.  The colors
are pretty obvious, but here's some information about the rest.

### Byline

The **Byline** settings change how the footer looks.  In the example
at [that's me](http://therealzachsnow.tumblr.com) the **Byline Prefix**
is set to "Theme by", the **Byline** is set to "Zach Snow", and the
**Byline Link** is set to "[http://zachsnow.com/](http://zachsnow.com/)".
If you want, you can use a `mailto:` link.  And if you don't want a link
at all, just don't set **Byline Link**. In fact, all of the **Byline** settings
are optional.

### Google Analytics

Google Analytics integration is as per usual, just grab your account
ID and set ** Google Analytics ID**.

### Typekit

There are two customizable Typekit fonts, one for headers and one for
all the rest of the text. To set these up, first create a new kit and
grab the kit "identifier" (the basename of the embed code Javascript file)
and set **Typekit ID**.

Next, pick your fonts. For the header font add the selector `.font-headers`.
For the other all-around font add the selector `.font-text`. Of course,
you can add all kinds of other selectors, too, if you want to get crazy.
