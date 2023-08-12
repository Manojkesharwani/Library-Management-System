from django.urls import path, include
from .import views
from .views import Addbook
from .views import Memberview
from .views import Transactionview
from .views import post_delete
from .views import edit_data
from .views import BlogSearchView
urlpatterns = [
    path("", views.indexx, name='home'),
    path("data/", views.import_books, name='data'),
    path('book-list/', views.book_list, name='book-list'),
    path('memberlist/', views.membersview, name='memberlist'),
    path('transactionlist/', views.transactionlistview, name='transactionlist'),
    path("bookform/", Addbook.as_view(), name='bookformm'),
    path("memberform/", Memberview.as_view(), name='memberform'),
    path("transactionform/", Transactionview.as_view(), name='transactionformm'),
    path("edit/data/<int:id>/", views.edit_data, name='edit_data'),
    path("delete_data/<int:id>/", views.post_delete, name='delete_data'),
    path('search-blogs/', views.BlogSearchView.as_view(), name='search_blogs')
]
