HEADERS = ('Team', 'MP', 'W', 'D', 'L', 'P')
JUSTIFICATION = 31
ROW_TEMPLATE = '| {} |  {} |  {} |  {} |  {}'


def get_row(items):
    return str(items[0]) + ''.rjust(JUSTIFICATION - len(str(items[0]))) + ROW_TEMPLATE.format(
        *tuple(str(items[i]).rjust(2 if i == 1 else 1) for i in range(1, len(items)))
    )


class Team(object):

    _played = 0
    _wins = 0
    _draws = 0
    _losses = 0
    _points = 0
    _name = ''

    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return get_row(items=(self._name, self._played, self._wins, self._draws, self._losses, self._points))


    @property
    def name(self):
        return self._name

    @property
    def points(self):
        return self._points

    def set_match_result(self, result, reverse=False):
        assert result in ('win', 'draw', 'loss')
        self._played += 1
        if result == 'win':
            self._wins += 1 if not reverse else 0
            self._losses += 1 if reverse else 0
            self._points += 3 if not reverse else 0
        elif result == 'draw':
            self._draws += 1
            self._points += 1
        elif result == 'loss':
            self._wins += 1 if reverse else 0
            self._losses += 1 if not reverse else 0
            self._points += 0 if not reverse else 3


def tally(rows):
    teams = {}
    for row in rows:
        first_team_name, second_team_name, match_result = row.split(';')
        for team_name in (first_team_name, second_team_name):
            teams[team_name] = teams.get(team_name, Team(name=team_name))
            teams[team_name].set_match_result(result=match_result, reverse=team_name == second_team_name)
    return [get_row(items=HEADERS)] + [
        str(team) for team in sorted(teams.values(), key=lambda x: (x.points * -1, x.name))
    ]
