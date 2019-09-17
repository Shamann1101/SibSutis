import re
# from copy import copy

_MAX_CHAIN_LENGTH = 10


class Rule:
    _ntl = list()

    def __init__(self, non_terminal, rules):
        try:
            if not isinstance(non_terminal, str):
                raise TypeError
            if not isinstance(rules, list):
                raise TypeError
        except TypeError:
            print('Value is wrong type')

        self._nt = non_terminal
        self._rules = list(set(rules))
        self._ntl.append(non_terminal)

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        pass

    @staticmethod
    def get_ntl():
        return Rule._ntl

    def __str__(self):
        return '{}: {}'.format(self._nt, self._rules)

    def __repr__(self):
        return str(self)


class Chain:
    def __init__(self, target, max_len):
        if not isinstance(target, str):
            raise TypeError
        elif len(target) > 1:
            raise ValueError
        if not isinstance(max_len, int):
            raise TypeError

        self.max_len = max_len
        self._history = list()
        self._string = target
        self._can_be_changed = True

    @property
    def can_be_changed(self):
        return self._can_be_changed

    @can_be_changed.setter
    def can_be_changed(self, value):
        pass

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        pass

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        pass

    def __str__(self):
        return self._string

    def __repr__(self):
        return str(self)

    def action(self, rule: str):
        rule = rule.strip()
        self._string = re.sub('([A-Z])', rule, self._string)
        self._history.append(rule)

        if len(re.findall('([A-Z])', self._string)) > 0 \
                and len(self._string) < self.max_len:
            self._can_be_changed = True
        else:
            self._can_be_changed = False

    def get_target_symbol(self) -> str or bool:
        r = re.findall('([A-Z])', self._string)
        if len(r) == 1:
            return r[0]
        elif len(r) < 1:
            return False
        else:
            raise ValueError


def _manual(target: str, rules: dict, max_len=_MAX_CHAIN_LENGTH) -> Chain:
    chain = Chain(target, max_len)
    while chain.can_be_changed:
        symbol = chain.get_target_symbol()
        if symbol is False:
            break
        for j in range(len(rules[symbol].rules)):
            print('[{}]: {}'.format(j, rules[symbol].rules[j]))
        print(chain)
        n = input('Choose: ')
        chain.action(rules[symbol].rules[int(n)])
    return chain


# TODO: Fix
def _auto(chains: list, rules: dict, max_len=_MAX_CHAIN_LENGTH) -> list:
    for chain in chains:
        pass

    return chains


def _main():
    rules = dict()
    while True:
        current_rules = list()
        symbol = input('Non terminal symbol: ')
        if bool(symbol) is False:
            break
        elif symbol in Rule.get_ntl() \
                or symbol not in re.findall('([A-Z])', symbol) \
                or len(symbol) > 1:
            continue
        while True:
            rule = input('Input rule: ')
            if bool(rule) is False:
                break
            else:
                r = re.findall('([A-Z])', rule)
                if len(r) <= 1:
                    current_rules.append(rule)
        if len(current_rules) > 0:
            rules[symbol] = Rule(symbol, current_rules)

    # Mock
    if len(rules) == 0:
        rules['S'] = Rule('S', ['0', '1', 'S0', 'S1', 'Sa', 'Sb', 'Sc'])

    try:
        r = list()
        for rule in rules:
            for cur in rules[rule].rules:
                r.extend(re.findall('([A-Z])', cur))
        if len(set(r) - set(Rule.get_ntl())) > 0:
            raise ValueError
    except ValueError:
        print('Non terminal letter error')
        exit(1)

    print(Rule.get_ntl())
    target = input('Input target symbol: ') or Rule.get_ntl()[0]
    print(rules)
    # c = _manual(target=target, rules=rules)
    # print('chain:')
    # print(c)
    # print('history:')
    # print(c.history)

    chains = list()
    c = Chain(target, _MAX_CHAIN_LENGTH)
    chains.append(c)
    cs = _auto(chains=chains, rules=rules, max_len=_MAX_CHAIN_LENGTH)
    print('cs:')
    print(cs)


if __name__ == '__main__':
    _main()
