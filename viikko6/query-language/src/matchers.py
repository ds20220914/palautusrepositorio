class QueryBuilder:
    def __init__(self, build = None):
        self.build_olio = build or All()
    def PlaysIn(self,team):
        return QueryBuilder(And(self.build_olio,PlaysIn(team)))
    def HasAtLeast(self,value, attr ):
        return QueryBuilder(And(self.build_olio,HasAtLeast(value, attr)))
    def Not(self, build):
        return QueryBuilder(And(self.build_olio, Not(build)))
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.build_olio, HasFewerThan(value, attr)))

    def Or(self, eka, toka):
        return QueryBuilder(Or(eka, toka))
    def build(self):
        return self.build_olio

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
        
class All:
    def __init__(self):
        pass
        
    def test(self, player):
        return True
        
class Not: 
    def __init__(self, condition):
        self.condition = condition
    def test(self, player):
        right=self.condition.test(player)
        if right==True:
            return False
        return True
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr
    
    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

