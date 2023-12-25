import os

import pytest
from if_this_then_that.api.caldav.caldav import Caldav
from dotenv import load_dotenv


class TestCaldav:
    @pytest.fixture
    def caldav(self):
        load_dotenv()

        url = os.getenv('NAVERCORP_CALDAV_URL')
        id = os.getenv('NAVERCORP_CALDAV_ID')
        password = os.getenv('NAVERCORP_CALDAV_PASSWORD')

        return Caldav(url, id, password)

    def test_get(self, caldav):
        print(caldav.get())
