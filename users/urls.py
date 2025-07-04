from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AutorViewsSet, LivroViewsSet
from .serializers import AutorSerializers, LivroSerializers
from .models import Autor,Livro


router = DefaultRouter()

router.register(r'livros', LivroViewsSet)
router.register(r'autor', AutorViewsSet)

urlpatterns = router.urls

#Criação de rota arquivo urls.py(EXEMPLO):
#from django.urls import path
#from rest_framework.routers import DefaultRouter
 
#from .views import GeneroLiterarioViewSet, LivroViewSet
 
#router = DefaultRouter()
 
#router.register(r'livros', LivroViewSet)
#router.register(r'genero', GeneroLiterarioViewSet)
 
#urlpatterns = router.urls