"""
Problem:

You are writing a feature that schedules emails.
As part of this feature, you should write a method
that receives a date (when the email should be sent)
and returns a friendly message for your user.

If the email was scheduled for today, you should return
"today at 10:30:00", for instance. The same goes for tomorrow.
If the email is scheduled for any day in the current week, you
should return the weekday. If the email is scheduled for next
week on, you should return the full date. Examples:

"The email is scheduled for today at 10:50."
"The email is scheduled for tomorrow at 10:50."
"The email is scheduled for Wednesday at 10:50."
"The email is scheduled for April 14, 2020 at 10:50."

You can ignore "The email is scheduled for" part. :)
"""
from datetime import datetime
from datetime import timedelta


def scheduled_for_message(when: datetime) -> str:
    today = datetime.now().date()
    at = when.strftime("%H:%M")
    if when.date() == today:
        label = "today"
        return "{} {}".format(label, at)

    tomorrow = today + timedelta(days=1)
    if when.date() == tomorrow:
        label = "tomorrow"
        return "{} {}".format(label, at)

    current_week = today.isocalendar()[1]
    if when.isocalendar()[1] == current_week:
        label = when.strftime("%A")
        return "{} {}".format(label, at)

    return when.strftime("%d.%m.%Y %H:%M")
