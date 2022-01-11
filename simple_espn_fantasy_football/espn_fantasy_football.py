
import requests

from datetime import datetime
from typing import Union


class EspnFantasyFootball:

    def __init__(self, swid: str=None, espn_s2: str=None, league_id: Union[int, str]=None):
        self.new_url     = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{id}'
        self.old_url     = 'https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/{id}?seasonId={year}'
        self.cookies     = {'swid': swid, 'espn_s2': espn_s2}
        self.league_id   = str(league_id)

    """
        https://www.reddit.com/r/fantasyfootball/comments/ct4hf3/new_espn_api/ -- contains views we can ideally support
        mTeam: returns a list of members and teams (with record for the season)
        mSettings: returns league settings, including previous seasons
        mRoster: returns a list of team IDs with their current(?) roster
        mStandings: returns a list of all scores for the chosen season
        mMatchup: returns a more detailed schedule for the chosen season, but without rosters
        mMatchupScore: returns a more detailed schedule for the chosen season, including rosters(?)
        mScoreboard
        mStatus
        mPendingTransactions
        mLiveScoring
        mPositionalRatings
    """

    def get_view_data(self, year: int=datetime.now().year - 1, param: str=None):
        """
        :param year: year for which we are pulling data
        :param param: view which we are retrieving.
        """

        # Make the callout
        if year > 2018:
            # Responses come back as dicts
            espn_api_response = requests.get(self.new_url.format(id=self.league_id, year=year), cookies=self.cookies, params={'view': param})
            # Convert the response to json for easier parsing
            espn_resp_json = espn_api_response.json()
            return espn_resp_json
        else:
            # Responses come back as list size of one
            espn_api_response = requests.get(self.old_url.format(year=year, id=self.league_id), cookies=self.cookies, params={'view': param})
            espn_resp_json = espn_api_response.json()
            return espn_resp_json[0]
