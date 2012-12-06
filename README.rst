Speaker Watch!
==============
Just a simple script to watch the `Texas Ethics Commission`_ website for
changes to the `list of declared speakers`_ and SMS a list of people when it
happens.


About this Code
---------------
This is just a quick hack job.  Its being offered up as example code for the
purpose of learning and shouldn't be used for anything other than learning.

That said...


Installation & Configuration
----------------------------
Install the requirements:

::

    pip install -r requirements.txt

Add the following values to your environment variables:

::

    TWILIO_ACCOUNT_SID={{ your Twilio account ID }}
    TWILIO_AUTH_TOKEN={{ your Twilio auth token }}
    FROM_PHONE_NUMBER={{ your Twilio phone # }}
    NUMBERS_TO_NOTIFY={{ a comma separated list of numbers to call }}

The ``NUMBERS_TO_NOTIFY`` value assumes that all numbers are US and in the
format of ``AAABBBCCCC`` and are comma-separated.

Note, you do need a `Twilio`_ account for this to all work.


.. _Texas Ethics Commission: http://www.ethics.state.tx.us/
.. _list of declared speakers: http://www.ethics.state.tx.us/dfs/spk_lists.htm
.. _Twilio: http://www.twilio.com/
