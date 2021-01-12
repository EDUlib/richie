# -*- coding: utf-8 -*-
"""
Unit tests for the user menu
"""
import re

from django.test.utils import override_settings
from django.utils.translation import gettext_lazy as _

from cms.api import create_page
from cms.test_utils.testcases import CMSTestCase


class UserMenuTests(CMSTestCase):
    """Test the user menu according to AUTHENTICATION_DELEGATION settings"""

    @override_settings(AUTHENTICATION_DELEGATION=None)
    def test_user_menu_without_authentication_delegation(self):
        """
        If AUTHENTICATION_DELEGATION is not defined, user menu should not be rendered
        """
        page = create_page(
            title="Home",
            language="en",
            published=True,
            template="richie/single_column.html",
        )
        response = self.client.get(page.get_public_url())

        self.assertNotContains(response, "richie-react richie-react--user-login")
        self.assertNotContains(
            response,
            r'"authentication": {{"endpoint": "{}", "backend": "{}"}}'.format(
                "https://richie.education:9999",
                "richie.apps.courses.lms.base.BaseLMSBackend",
            ),
        )
