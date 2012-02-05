import os
here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

LAYOUT_DIR = here('layout')
CONTENT_DIR = here('content')
MEDIA_DIR = here('media')
DEPLOY_DIR = here('deploy')
TMP_DIR = here('deploy_tmp')

BACKUPS_DIR = here('backups')
BACKUP = False

SITE_ROOT = "/"
SITE_WWW_URL = "http://www.natalieannevans.com"
SITE_NAME = "Natalie Evans <span>Childbirth Educator &amp; Birth Doula</span>"
SITE_AUTHOR = "Natalie Evans"

GENERATE_ABSOLUTE_FS_URLS = False
GENERATE_CLEAN_URLS = False
LISTING_PAGE_NAMES = ['listing', 'index', 'default']
APPEND_SLASH = False
MEDIA_PROCESSORS = {
    '*':{
        '.css':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CSSmin',),
        '.ccss':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CleverCSS',
                'hydeengine.media_processors.CSSmin',),
        '.sass':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.SASS',
                'hydeengine.media_processors.CSSmin',),
        '.less':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.LessCSS',
                'hydeengine.media_processors.CSSmin',),
        '.styl':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.Stylus',
                'hydeengine.media_processors.CSSmin',),
        '.hss':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.HSS',
                'hydeengine.media_processors.CSSmin',),
        '.js':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.JSmin',),
        '.coffee':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CoffeeScript',
                'hydeengine.media_processors.JSmin',)
    }
}

CONTENT_PROCESSORS = {
    'prerendered/': {
        '*.*' :
            ('hydeengine.content_processors.PassthroughProcessor',)
            }
}

SITE_POST_PROCESSORS = {
    # 'media/js': {
    #        'hydeengine.site_post_processors.FolderFlattener' : {
    #                'remove_processed_folders': True,
    #                'pattern':"*.js"
    #        }
    #    }
}

CONTEXT = {
    'GENERATE_CLEAN_URLS': GENERATE_CLEAN_URLS
}

FILTER = {
    'exclude': (".*","*~")
}
GROWL = None
YUI_COMPRESSOR = None
CLOSURE_COMPRILER = None
HSS_PATH = None # if you don't want to use HSS
TEMPLATE_DIRS = (LAYOUT_DIR, CONTENT_DIR, TMP_DIR, MEDIA_DIR)

INSTALLED_APPS = (
    'hydeengine',
    'django.contrib.webdesign',
)