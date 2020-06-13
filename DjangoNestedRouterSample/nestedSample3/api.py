from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet

from rest_framework_extensions.routers import NestedRouterMixin

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

#router = DefaultRouter()

#router.register('authors', AuthorViewSet)
#router.register('books', BookViewSet)

router = NestedDefaultRouter()

authors_router = router.register('authors', AuthorViewSet)
authors_router.register(
    'books', BookViewSet,
    basename='author-books',
    parents_query_lookups=['author'])
