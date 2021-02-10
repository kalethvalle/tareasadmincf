from rest_framework import routers
from .viewsets import TaskManagerViewsets, PrefijoViewsets
# from task import viewsets

router = routers.SimpleRouter()
router.register('task', TaskManagerViewsets)
router.register('prefijos', PrefijoViewsets)

urlpatterns = router.urls 
