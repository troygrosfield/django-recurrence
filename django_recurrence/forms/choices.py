# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from ..constants import Frequency
from ..constants import Day

FREQUENCY_CHOICES = (
    (Frequency.ONCE, _('Never')),
    (Frequency.DAILY, _('Daily')),
    (Frequency.WEEKLY, _('Weekly')),
    (Frequency.MONTHLY, _('Monthly')),
    ('semi_annual', _('Semi-Annual')),
    (Frequency.YEARLY, _('Yearly')),
    ('every_other_week', _('Every Other Week')),
    ('last_day_of_month', _('Last Day of the Month')),
)

WEEKDAY_CHOICES = (
    (Day.SUNDAY, 'Sunday'),
    (Day.MONDAY, 'Monday'),
    (Day.TUESDAY, 'Tuesday'),
    (Day.WEDNESDAY, 'Wednesday'),
    (Day.THURSDAY, 'Thursday'),
    (Day.FRIDAY, 'Friday'),
    (Day.SATURDAY, 'Saturday'),
)


class FrequencyChoices(object):
    NEVER = 'NEVER'  # never recur
    NUM_OCCURRENCES = 'NUM_OCCURRENCES'  # stop after number of occurrences
    STOP_AFTER_DATE = 'STOP_AFTER_DATE'  # after after a date
    ALL = ((NEVER, NEVER),
           (NUM_OCCURRENCES, NUM_OCCURRENCES),
           (STOP_AFTER_DATE, STOP_AFTER_DATE)
           )