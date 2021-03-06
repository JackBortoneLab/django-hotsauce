from django.conf.urls.defaults import *
import product
from signals_ahoy.signals import collect_urls

urlpatterns = patterns('product.views',
    (r'^(?P<product_slug>[-\w]+)/$', 
        'get_product', {}, 'satchmo_product'),
    (r'^(?P<product_slug>[-\w]+)/prices/$', 
        'get_price', {}, 'satchmo_product_prices'),
    (r'^(?P<product_slug>[-\w]+)/price_detail/$', 
        'get_price_detail', {}, 'satchmo_product_price_detail'),
)

urlpatterns += patterns('product.views.filters',
    (r'^view/recent/$', 
        'display_recent', {}, 'satchmo_product_recently_added'),
    (r'^view/bestsellers/$', 
        'display_bestsellers', {}, 'satchmo_product_best_selling'),
)


# here we are sending a signal to add patterns to the base of the shop.
# collect_urls.send(sender=product, patterns=urlpatterns, section="product")
