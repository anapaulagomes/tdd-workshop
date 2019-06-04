from datetime import datetime
from freezegun import freeze_time
from message import scheduled_for_message


@freeze_time('2018-01-20 09:01:38')
def test_display_today_message():
    today = datetime(2018, 1, 20, 10, 16, 50)
    expected_message = 'today 10:16'

    assert scheduled_for_message(today) == expected_message


@freeze_time('2018-01-20 09:01:38')
def test_display_tomorrow_message():
    tomorrow = datetime(2018, 1, 21, 10, 16, 50)
    expected_message = 'tomorrow 10:16'

    assert scheduled_for_message(tomorrow) == expected_message


@freeze_time('2019-06-03 09:01:38')
def test_display_same_week_message():
    wednesday = datetime(2019, 6, 5, 10, 16, 50)
    expected_message = 'Wednesday 10:16'

    assert scheduled_for_message(wednesday) == expected_message


@freeze_time('2019-06-02 09:01:38')
def test_display_next_week_message():
    next_week_date = datetime(2019, 6, 14, 10, 16, 50)
    expected_message = '14.06.2019 10:16'

    assert scheduled_for_message(next_week_date) == expected_message
