### **Passo a passo para criação de uma API com Django REST Framework**

#### **1. Criar e ativar o ambiente virtual**

```bash
python3 -m venv venv
```

* No Windows:

```bash
venv\Scripts\activate
```

* No Linux/Mac:

```bash
source venv/bin/activate
```

---

#### **2. Instalar as dependências**

```bash
pip install django
pip install djangorestframework
```

---

#### **3. Criar o projeto Django**

```bash
django-admin startproject nome_do_projeto
```

---

#### **4. Criar o app**

```bash
django-admin startapp nome_do_app
```

---

#### **5. Configurar o `settings.py`**

No arquivo `settings.py` do projeto, adicione o app criado e o `rest_framework` na lista `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'nome_do_app',
    'rest_framework',
]
```

---

#### **6. Criar arquivos essenciais no app**

Na pasta do seu app, crie os arquivos `serializers.py` e `urls.py` se ainda não existirem.

---

### **Criando um endpoint**

#### **Modelos (`models.py`)**

Exemplo com dois modelos:

```python
from django.db import models

class GeneroLiterario(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Livros(models.Model):
    nome = models.CharField(max_length=150)
    genero_literario = models.ForeignKey(GeneroLiterario, on_delete=models.SET_NULL, null=True, blank=True)
    categoria_principal = models.CharField(max_length=50, null=True, blank=True)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
```

> ⚠️ Após criar os modelos, execute os comandos para gerar e aplicar as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

#### **Serializers (`serializers.py`)**

```python
from rest_framework import serializers
from .models import GeneroLiterario, Livros

class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'

class GeneroLiterarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroLiterario
        fields = '__all__'
```

---

#### **Views (`views.py`)**

```python
from rest_framework.viewsets import ModelViewSet
from .models import GeneroLiterario, Livros
from .serializers import GeneroLiterarioSerializer, LivrosSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class GeneroLiterarioViewSet(ModelViewSet):
    queryset = GeneroLiterario.objects.all()
    serializer_class = GeneroLiterarioSerializer
```

---

#### **Rotas do app (`urls.py` do app)**

```python
from rest_framework.routers import DefaultRouter
from .views import GeneroLiterarioViewSet, LivroViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'generos', GeneroLiterarioViewSet)

urlpatterns = router.urls
```

---

#### **Registrar rotas do app no projeto (`urls.py` do projeto)**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('nome_do_app.urls')),
]
```