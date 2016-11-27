from django.conf.urls import url
from qa.views import test
#from qa.views import question_ask, question_answer, question_list, question_detail, popular
#from qa.views import user_signup, user_login, user_logout

urlpatterns = [
    url(r'^$', test, name='question_list'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/(?P<pk>\d+)/', test, name='question_detail'),
    url(r'^ask/', test, name='question_ask'),
    url(r'^popular/', test, name='popular'),
    url(r'^new/', test, name='new'),
]
