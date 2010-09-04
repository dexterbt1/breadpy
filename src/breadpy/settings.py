BASE_URL = ""
#DATABASE_ENGINE_URL = 'mysql://viral:viralviral@localhost/viral'
DATABASE_ENGINE_URL = 'mysql://root:@localhost/spree?charset=utf8'
TEMPLATE_APP_NAME = "breadpy"
TEMPLATE_DIR_NAME = "templates"

DISPLAY_FK = {
    u'store_store' : {
        u'user_id' : [ u'auth_user.username', u'auth_user.email' ],
        },
    u'store_order' : {
        u'buyer_user_id' : [ u'auth_user.username', u'auth_user.email' ],
        },
}
