from django.test import TestCase

# Create your tests here.
try:
    from ..utilities import translator
    print("Módulo translator importado:", dir(translator))
except ImportError as e:
    print("Error al importar translator:", e)