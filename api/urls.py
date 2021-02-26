from rest_framework import routers

from .api import TutorAPI, TuteeAPI

router = routers.DefaultRouter()
router.register('tutors', TutorAPI, 'tutors')
router.register('tutees', TuteeAPI, 'tutees')


urlpatterns = router.urls