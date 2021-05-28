from rest_framework.permissions import BasePermission
from django.utils.translation import ugettext_lazy as _
from MV.quickstart.models import UserStatus
import logging

logger = logging.getLogger(__name__)
error_message = _("Improper Login. Attempted to log in as Anonymous User.")

class IsHR(BasePermission):

    def has_permission(self, request, view):
        try:
            user_status = UserStatus.object.filter(user=request.user, role_name='HR')
            return any([user_status.active for user_status in user_status])
        except Exception as e:
            logger.exception(e)
            logger.debug(error_message, exc_info=True)


class IsDepartamentManager(BasePermission):

    def has_permission(self, request, view):
        try:
            user_status = UserStatus.object.filter(user=request.user, role_name='Departament Manager')
            return any([user_status.active for user_status in user_status])
        except Exception as e:
            logger.exception(e)
            logger.debug(error_message, exc_info=True)


class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        try:
            user_status = UserStatus.object.filter(user=request.user, role_name='Employee')
            return any([user_status.active for user_status in user_status])
        except Exception as e:
            logger.exception(e)
            logger.debug(error_message, exc_info=True)