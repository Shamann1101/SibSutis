from copy import copy
from re import findall, sub

_MAX_CHAIN_LENGTH = 5


class CFG:
    def __init__(self):
        self._terminal = list()
        self._non_terminal = list()
        self._rules = dict()
        self._target = str()

    @property
    def terminal(self):
        return self._terminal

    @terminal.setter
    def terminal(self, value: list):
        for item in value:
            if not isinstance(item, str):
                raise ValueError
            item = item.lower()
            if item not in self._terminal:
                self._terminal.append(item)

    @property
    def non_terminal(self):
        return self._non_terminal

    @non_terminal.setter
    def non_terminal(self, value: list):
        for item in value:
            if not isinstance(item, str):
                raise ValueError
            item = item.upper()
            if item not in self._non_terminal:
                self._non_terminal.append(item)

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value: dict):
        for k, v in value:
            if not isinstance(v, list) \
                    or k not in self._non_terminal:
                raise ValueError
        self._rules = value

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value: str):
        value = value.upper()
        if value not in self._non_terminal:
            raise ValueError
        self._target = value


class Rule:
    def __init__(self, cfg: CFG, non_terminal: str, rules: list):
        self._cfg = cfg
        self._rules = list(set(rules))

        if non_terminal not in self._cfg.non_terminal:
            print(non_terminal)
            print(self._cfg.non_terminal)
            raise ValueError
        self._non_terminal = non_terminal

        for rule in rules:
            r = findall('([A-Z])', rule)
            if 0 == len(r) > 1 \
                    or (r and r[0] not in self._cfg.non_terminal):
                raise ValueError

        self._cfg.rules[self._non_terminal] = self._rules

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        pass

    def __str__(self):
        return '{}: {}'.format(self._non_terminal, self._rules)

    def __repr__(self):
        return str(self)


class Chain:
    def __init__(self, target: str, max_len: int):
        if not isinstance(target, str):
            raise TypeError
        elif len(target) > 1:
            raise ValueError
        if not isinstance(max_len, int):
            raise TypeError

        self.max_len = max_len
        self._can_be_changed = True if self.max_len > 0 else False
        self._history = list()
        self._string = target

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
        if self._can_be_changed:
            rule = rule.strip()
            self._string = sub('([A-Z])', rule, self._string)
            self._history.append(rule)

        if len(findall('([A-Z])', self._string)) > 0 \
                and len(self._string) <= self.max_len + 1:
            self._can_be_changed = True
        else:
            self._can_be_changed = False

    def get_target_symbol(self) -> str or bool:
        r = findall('([A-Z])', self._string)
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


def _iterate(chains: list, rules: dict) -> list:
    work_list = list()
    done_list = list()

    for chain in chains:
        if chain.can_be_changed:
            symbol = chain.get_target_symbol()
            for j in range(len(rules[symbol].rules)):
                c = copy(chain)
                c.action(rules[symbol].rules[int(j)])
                if c.can_be_changed:
                    work_list.append(c)
                else:
                    done_list.append(c)
        else:
            done_list.append(chain)

    if len(work_list) != 0:
        a = _iterate(work_list, rules)
        done_list.extend(a)

    for chain in done_list:
        r = findall('([A-Z])', chain.string)
        if len(r) > 0:
            done_list.remove(chain)

    return done_list


def _auto(chains: list, rules: dict) -> list:
    result = _iterate(chains, rules)
    for chain in result:
        r = findall('([A-Z])', chain.string)
        if len(r) > 0:
            result.remove(chain)

    return result


def _main():
    rules = dict()
    # Mock
    cfg = CFG()
    cfg.terminal = ['0', '1', '']
    cfg.non_terminal = ['S', 'A', 'E']
    cfg.target = 'S'
    while True:
        current_rules = list()
        symbol = input('Non terminal symbol: ')
        symbol = symbol.upper()
        if bool(symbol) is False:
            break
        elif symbol in cfg.non_terminal \
                or symbol not in findall('([A-Z])', symbol) \
                or len(symbol) > 1:
            continue
        while True:
            rule = input('Input rule: ')
            if bool(rule) is False:
                break
            else:
                r = findall('([A-Z])', rule)
                if len(r) <= 1:
                    current_rules.append(rule)
        if len(current_rules) > 0:
            cfg.non_terminal.append(symbol)
            rules[symbol] = Rule(cfg, symbol, current_rules)

    # Mock
    if len(rules) == 0:
        # rules['S'] = Rule('S', ['0', '1', 'S0', 'S1', 'Sa', 'Sb', 'Sc'])
        rules['S'] = Rule(cfg, 'S', ['0A', '1A', ' '])
        rules['A'] = Rule(cfg, 'A', ['0E', '1E'])
        rules['E'] = Rule(cfg, 'E', ['0S', '1S'])

    try:
        r = list()
        for rule in rules:
            for cur in rules[rule].rules:
                r.extend(findall('([A-Z])', cur))
        if len(set(r) - set(cfg.non_terminal)) > 0:
            raise ValueError
    except ValueError:
        print('Non terminal letter error')
        exit(1)

    print(cfg.non_terminal)
    target = input('Input target symbol: ') or cfg.non_terminal[0]
    print(rules)
    chain_length = input('Chain length: ') or _MAX_CHAIN_LENGTH
    # c = _manual(target=target, rules=rules, max_len=int(chain_length))
    # print('chain:')
    # print(c)
    # print('history:')
    # print(c.history)

    chains = list()
    c = Chain(target, int(chain_length))
    chains.append(c)
    cs = _auto(chains=chains, rules=rules)
    print('cs:')
    print(cs)


if __name__ == '__main__':
    _main()
