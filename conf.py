# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

# Configuration, please edit

# Data about this site
BLOG_AUTHOR = "The MATE Team"
BLOG_TITLE = "MATE"
BLOG_LOGO = "/assets/img/icons/mate.png"
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "http://mate-desktop.org/"
# This is the URL where nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://mate-desktop.org"
BLOG_EMAIL = "webmaster@mate-desktop.org"
BLOG_DESCRIPTION = "The traditional Desktop Environment"

# Nikola is multilingual!
#
# Currently supported languages are:
# bg     Bulgarian
# ca     Catalan
# de     German
# el     Greek [NOT gr!]
# en     English
# eo     Esperanto
# es     Spanish
# fa     Persian
# fr     French
# hr     Croatian
# it     Italian
# jp     Japanese
# nl     Dutch
# pt_br  Portuguese (Brasil)
# pl     Polish
# ru     Russian
# tr_tr  Turkish (Turkey)
# zh_cn  Chinese (Simplified)
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (p.e. look at the modules at: ./nikola/data/themes/default/messages/fr.py).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
		('/blog/', 'Blog'),
		('/install/', 'Install'),		
		('/gallery/1.6/', 'Screenshots'),		
		('/development/', 'Development'),		
		('/community/', 'Community'),
		('/team/', 'Team'),		
		('/donate/', 'Donate'),
    ),
}

# Below this point, everything is optional

# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and opcionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.
#

POSTS = (
	    ("blog/*.rst", "blog", "post.tmpl"),
            ("blog/*.md", "blog", "post.tmpl"),
        )
PAGES = (
            ("pages/*.rst", "", "story.tmpl"),
            ("pages/*.md", "", "story.tmpl"),
        )

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of "source" "relative destination".
# Default is:
FILES_FOLDERS = {'files': '' }
# Which means copy 'files' into 'output'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is html and just copies it
COMPILERS = {
        "rest": ('.txt', '.rst'),
        "markdown": ('.md', '.mdown', '.markdown'),
        "html": ('.html', '.htm')
}        

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
ONE_FILE_POSTS = True

# If this is set to True, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# If set to False, the DEFAULT_LANG version will be displayed for
# untranslated posts.
HIDE_UNTRANSLATED_POSTS = False

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
TAG_PATH = "tags"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = True

# Final location is output / TRANSLATION[lang] / INDEX_PATH / index-*.html
INDEX_PATH = "blog"

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
ARCHIVE_PATH = "archive"
#ARCHIVE_FILENAME = "archive.html"

# Final locations are:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Number of posts in RSS feeds
# FEED_LENGTH = 10

# Slug the Tag URL easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [
    (u'2011/12/05/hello-world/index.html', u'/blog/2011-12-05-introducing-mate-desktop/index.html'),
    (u'2011/12/24/new-wiki-and-other-info/index.html', u'/blog/2011-12-24-new-wiki-and-new-distributions-supported/index.html'),
    (u'2012/01/18/reporting-bugs/index.html', u'/blog/2012-01-18-reporting-bugs/index.html'),
    (u'2012/04/16/mate-1-2-released/index.html', u'/blog/2012-04-16-mate-1-2-released/index.html'),
    (u'2012/07/28/packages-mate-desktop-org-repo/index.html', u'/index.html'),
    (u'2012/07/30/mate-1-4-released/index.html', u'/blog/2012-07-30-mate-1-4-released/index.html'),
    (u'2012/10/16/mate-quantal-repo-available/index.html', u'/blog/2012-10-16-mate-package-repository-for-ubuntu-quantal/index.html'),
    (u'2012/11/10/fedora-repo/index.html', u'/blog/2012-11-10-mate-package-repository-for-fedora/index.html'),
    (u'2012/12/27/thank-you-first-colo/index.html', u'/blog/20121227thank-you-first-colo/index.html'),
    (u'2013/01/20/changes-to-mate-notification-daemon/index.html', u'/blog/2013-01-20-changes-to-mate-notification-daemon/index.html'),
    (u'2013/03/12/mate-university/index.html', u'/blog/2013-03-12-mate-university/index.html'), 
    (u'2013/03/20/mate-and-ltsp/index.html', u'/blog/2013-03-20-mate-and-ltsp/index.html'), 
    (u'2013/03/26/new-themes/index.html', u'/blog/2013-03-26-new-themes/index.html'), 
    (u'2013/04/02/mate-1-6-released/index.html', u'/blog/2013-04-02-mate-1-6-released/index.html'),
    (u'2013/07/21/stefano-at-opensuse-conference/index.html', u'/blog/2013-07-21-stefano-presents-at-opensuse-conference/index.html'),     
    (u'2013/08/10/new-repositories-for-opensuse/index.html', u'/blog/2013-08-10-mate-package-repository-for-opensuse/index.html'),
    (u'feedback/index.html', u'/index.html'),	
    (u'applications/index.html', u'/index.html'),
    (u'support/index.html', u'/community/index.html'),    
    (u'about/index.html', u'/index.html'),
    (u'feed/index.html', u'/rss.xml')]
    
# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav output/* joe@my.site:/srv/www/site"
# And then do a backup, or ping pingomatic.
# To do manual deployment, set it to []
DEPLOY_COMMANDS = [
	'rsync -a --delete output/ /var/www/new-site/',
]

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, there are no filters.
#
# Many filters are shipped with Nikola.  A list is available in the manual:
# <http://getnikola.com/handbook.html#post-processing-filters>
# FILTERS = {
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Create a gzipped copy of each generated file. Cheap server-side optimization.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None

# #############################################################################
# Image Gallery Options
# #############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
GALLERY_PATH = "gallery"
THUMBNAIL_SIZE = 360
MAX_IMAGE_SIZE = 1280
USE_FILENAME_AS_TITLE = True
#
# If set to False, it will sort by filename instead. Defaults to True
GALLERY_SORT_BY_DATE = False

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes
# INDEXES_TITLE = ""  # If this is empty, the default is BLOG_TITLE
# INDEXES_PAGES = ""  # If this is empty, the default is 'old posts page %d'
# translated

# Name of the theme to use.
THEME = "MATE"

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni
# monokai murphy native pastie perldoc rrt tango trac vim vs
# CODE_COLOR_SCHEME = 'default'

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# date format used to display post dates.
# (str used by datetime.datetime.strftime)
DATE_FORMAT = '%Y-%m-%d'

# FAVICONS contains (name, file, size) tuples.
# Used for create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# For creating favicons, take a look at:
# http://www.netmagazine.com/features/create-perfect-favicon
FAVICONS = {
    ("icon", "/favicon.ico", "16x16"),	
    ("icon", "/mate-128.png", "128x128"),
}

# Show only teasers in the index pages? Defaults to False.
INDEX_TEASERS = False

# A HTML fragment with the Read more... link.
# The following tags exist and are replaced for you:
# {link}        A link to the full post page.
# {read_more}   The string “Read more” in the current language.
# {{            A literal { (U+007B LEFT CURLY BRACKET)
# }}            A literal } (U+007D RIGHT CURLY BRACKET)
# READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'

# A HTML fragment describing the license, for the sidebar.
#LICENSE = ""
# I recommend using the Creative Commons' wizard:
# http://creativecommons.org/choose/
LICENSE = """
<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">mate-desktop.org</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US" target="_blank">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.<br/>
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US" target="_blank"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a>
"""

# A small copyright notice for the page footer (in HTML).
# Default is ''
CONTENT_FOOTER = '<div align="center"><small>Contents &copy; {date} <a href="mailto:{email}">{author}</a>. {license}</small></div>'
CONTENT_FOOTER = CONTENT_FOOTER.format(email=BLOG_EMAIL,
                                       author=BLOG_AUTHOR,
                                       date=time.gmtime().tm_year,
                                       license=LICENSE)

# To use comments, you can choose between different third party comment
# systems, one of "disqus", "livefyre", "intensedebate", "moot",
#                 "googleplus" or "facebook"
COMMENT_SYSTEM = False
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = False

# Enable annotations using annotateit.org?
# If set to False, you can still enable them for individual posts and pages
# setting the "annotations" metadata.
# If set to True, you can disable them for individual posts and pages using
# the "noannotations" metadata.
# ANNOTATIONS = False

# Create index.html for story folders?
STORY_INDEX = False
# Enable comments on story pages?
COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
# Default = False
STRIP_INDEXES = True

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
SITEMAP_INCLUDE_FILELESS_DIRS = True

# Instead of putting files in <slug>.html, put them in
# <slug>/index.html. Also enables STRIP_INDEXES
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata
PRETTY_URLS = True

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
DEPLOY_DRAFTS = False

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False
# If True, schedules post to today if possible, even if scheduled hour is over
# SCHEDULE_FORCE_TODAY = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
#MATHJAX_CONFIG = """
#<script type="text/x-mathjax-config">
#MathJax.Hub.Config({
#    tex2jax: {
#        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ]
#    },
#    displayAlign: 'left', // Change this to 'center' to center equations.
#    "HTML-CSS": {
#        styles: {'.MathJax_Display': {"margin": 0}}
#    }
#});
#</script>
#"""

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuracion you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What MarkDown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
MARKDOWN_EXTENSIONS = ['extra', 'codehilite', 'toc']

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty.
SOCIAL_BUTTONS_CODE = ""
#SOCIAL_BUTTONS_CODE = """
#<!-- Social buttons -->
#<div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
#<a class="addthis_button_more">Share</a>
#<ul><li><a class="addthis_button_facebook"></a>
#<li><a class="addthis_button_google_plusone_share"></a>
#<li><a class="addthis_button_linkedin"></a>
#<li><a class="addthis_button_twitter"></a>
#</ul>
#</div>
#<script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
#<!-- End of social buttons -->
"""

# Hide link to source for the posts?
HIDE_SOURCELINK = True
# Copy the source files for your pages?
# Setting it to False implies HIDE_SOURCELINK = True
COPY_SOURCES = False

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.
# RSS_LINK = None

# Show only teasers in the RSS feed? Default to True
RSS_TEASERS = False

# There is a local search plugin you can use, based on Tipue, but it requires setting several
# options:

#<form class="form-search" method="get" id="s" action="/">
#    <div class="input-append">
#        <input type="text" class="input-medium search-query" name="s" placeholder="Search" value="">
#        <button type="submit" class="add-on"><i class="icon-search"></i></button>
#    </div>
#</form>

SEARCH_FORM = """
<span class="navbar-search pull-right">
	<input class="input-medium search-query search-margin" type="search" placeholder="Search" id="tipue_search_input"></input>
</span>"""

SEARCH_RESULTS = """
<div id="tipue_search_content" style="margin-left: auto; margin-right: auto; padding: 20px;"></div>
"""

# Use content distribution networks for jquery and twitter-bootstrap css and js
# If this is True, jquery is served from the Google CDN and twitter-bootstrap
# is served from the NetDNA CDN
# Set this to False if you want to host your site without requiring access to
# external resources.
USE_CDN = False

# Extra things you want in the pages HEAD tag. This will be added right
# before </HEAD>

EXTRA_HEAD_DATA = """
<link rel="stylesheet" type="text/css" href="/assets/css/custom.css">
"""
# Google analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).

BODY_END = """
<script type="text/javascript" src="/assets/js/tipuesearch_set.js"></script>
<script type="text/javascript" src="/assets/js/tipuesearch.js"></script>
<script type="text/javascript">
$(document).ready(function() {
    $('#tipue_search_input').tipuesearch({
        'show': 5,
        'mode': 'json',
        'contentLocation': '/assets/js/tipuesearch_content.json',
        'showUrl': false
    });
});
</script>
"""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# Additional metadata that is added to a post when creating a new_post
ADDITIONAL_METADATA = {
    'author': 'Webmaster'
}

# Nikola supports Twitter Card summaries / Open Graph.
# Twitter cards make it possible for you to attach media to Tweets
# that link to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit
# https://dev.twitter.com/form/participate-twitter-cards
#
# Uncomment and modify to following lines to match your accounts.
# Specifying the id for either 'site' or 'creator' will be preferred
# over the cleartext username. Specifying an ID is not necessary.
# Displaying images is currently not supported.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards / Open Graph
#     # 'site': '@website',  # twitter nick for the website
#     # 'site:id': 123456,  # Same as site, but the website's Twitter user ID
#                           # instead.
#     # 'creator': '@username',  # Username for the content creator / author.
#     # 'creator:id': 654321,  # Same as creator, but the Twitter user's ID.
# }


# Post's dates are considered in GMT by default, if you want to use 
# another timezone, please set TIMEZONE to match. Check the available 
# list from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Also, if you want to use a different timezone in some of your posts, 
# you can use W3C-DTF Format (ex. 2012-03-30T23:00:00+02:00)
#
TIMEZONE = 'Europe/London'

# If webassets is installed, bundle JS and CSS to make site loading faster
USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Experimental plugins - use at your own risk.
# They probably need some manual adjustments - please see their respective
# readme.
ENABLED_EXTRAS = [
	'local_search'
]

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# HYPHENATE = False

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.

SOCIAL_ICONS="""
<a class="social-icon" href="/rss.xml" title="MATE RSS feed"><img src="/assets/img/icons/rss.png" alt="RSS" class="small-margin"></a>
<a class="social-icon" href="http://wiki.mate-desktop.org/" title="MATE Wiki"><img src="/assets/img/icons/wiki.png" alt="Wiki" class="small-margin"></a>
<a class="social-icon" href="https://github.com/mate-desktop/" title="MATE GitHub"><img src="/assets/img/icons/github.png" alt="GitHub" class="small-margin"></a>
<a class="social-icon" href="https://twitter.com/Mate_desktop" title="@Mate_Desktop Twitter"><img src="/assets/img/icons/twitter.png" alt="Twitter" class="small-margin"></a>
<a class="social-icon" href="https://plus.google.com/u/0/communities/103904770310171205536" title="MATE Google+ Community"><img src="/assets/img/icons/gplus.png" alt="Google+" class="small-margin"></a>
<a class="social-icon" href="https://plus.google.com/105251070079435964338/posts" title="MATE Google+ Page"><img src="/assets/img/icons/gplus.png" alt="Google+" class="small-margin"></a>
"""

GLOBAL_CONTEXT = {
    'blog_logo': BLOG_LOGO,
    'search_results': SEARCH_RESULTS,
    'social_icons': SOCIAL_ICONS
}
