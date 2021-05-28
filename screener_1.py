"""
This program runs a single test that is currently failing.
It is throwing a common exception. Your goal is to make it pass
by only editing the get_display_data() function. Use the
expected output from the test function as a clue.

You can work locally if you have Python 3.7+ installed or feel free to use
a web based solution. Here is one option: https://replit.com/languages/python3


Please provide your updated get_display_data() function
by responding to the email you received.
"""

from dataclasses import dataclass
import unittest


# specify what a feed looks like
@dataclass
class Feed:
    title: str
    href: str
    is_active: bool
    ttl: int


# specify what an episode looks like
@dataclass
class Episode:
    title: str
    feed: Feed = None


def get_display_data(episodes):
    data = []
    for episode in episodes:
        data.append(f"{episode.title} on {episode.feed.title}")
    return data


class DisplayTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # create the feed and episodes
        feed = Feed("The Daily", "https://feeds.simplecast.com/54nAGcIl", True, 300)
        self.ep1 = Episode("Today", feed)
        self.ep2 = Episode("Yesterday")

    def test_get_display_data(self):
        actual = get_display_data([self.ep1, self.ep2])
        expected = [
            "Today on The Daily",
            "Yesterday on _unknown_"
        ]
        self.assertEqual(actual, expected)

unittest.main(exit=False)
