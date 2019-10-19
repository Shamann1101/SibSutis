class DFSM:
    def __init__(self):
        self._alphabet = list()
        self._state_name_list = list()
        self._state_dict = dict()
        self._initial_state = None
        self._final_state = None

    @property
    def alphabet(self):
        return self._alphabet

    @alphabet.setter
    def alphabet(self, value: list):
        alphabet_list = list()
        for alphabet in value:
            alphabet = alphabet.lower()
            if len(alphabet) > 1 \
                    or alphabet in alphabet_list \
                    or (self._state_name_list and alphabet.upper() in self._state_name_list):
                raise ValueError
            alphabet_list.append(alphabet.strip())

        self._alphabet = alphabet_list if len(alphabet_list) > 0 else ['0', '1', 'a']

    @property
    def state_name_list(self):
        return self._state_name_list

    @state_name_list.setter
    def state_name_list(self, value: list):
        state_name_list = list()
        for state in value:
            state = state.upper()
            if len(state) > 1 \
                    or state in state_name_list \
                    or (self._alphabet and state.lower() in self._alphabet):
                raise ValueError
            state_name_list.append(state)

        self._state_name_list = state_name_list if len(state_name_list) > 0 else ['P', 'Q', 'R']

    @property
    def state_dict(self):
        return self._state_dict

    @state_dict.setter
    def state_dict(self, value: dict):
        for state, rules in value.items():
            state = state.upper()
            if not isinstance(state, str) \
                    or not isinstance(rules, dict) \
                    or state not in self._state_name_list:
                raise ValueError
            self._state_dict[state] = dict()
            for action in rules:
                target = rules[action].upper()
                if not isinstance(action, str) \
                        or not isinstance(rules[action], str) \
                        or action.lower() not in self._alphabet \
                        or (target not in self._state_name_list
                            and target != ''):
                    raise ValueError
                self._state_dict[state][action.lower()] = target

    @property
    def initial_state(self):
        return self._initial_state

    @initial_state.setter
    def initial_state(self, value: str):
        value = value.upper()
        if len(value) > 1 \
                or value not in self._state_name_list:
            raise ValueError
        self._initial_state = value

    @property
    def final_state(self):
        return self._final_state

    @final_state.setter
    def final_state(self, value: str):
        value = value.upper()
        if len(value) > 1 \
                or value not in self._state_name_list:
            raise ValueError
        self._final_state = value

    def set_alphabet(self):
        alphabet_list = list()
        while True:
            alphabet = input('Input alphabet: ')
            alphabet = alphabet.lower()
            if bool(alphabet) is False:
                break
            elif len(alphabet) > 1 \
                    or alphabet in alphabet_list \
                    or (self._state_name_list and alphabet.upper() in self._state_name_list):
                continue
            alphabet_list.append(alphabet.strip())

        self._alphabet = alphabet_list if len(alphabet_list) > 0 else ['0', '1', 'a']

    def set_state_name_list(self):
        state_name_list = list()
        while True:
            state = input('Input state: ')
            state = state.upper()
            if bool(state) is False:
                break
            elif len(state) > 1 \
                    or state in state_name_list \
                    or (self._alphabet and state.lower() in self._alphabet):
                continue
            state_name_list.append(state)

        self._state_name_list = state_name_list if len(state_name_list) > 0 else ['P', 'Q', 'R']

    def set_initial_state(self):
        while True:
            state = input('Input initial state: ')
            state = state.upper()
            if bool(state) is False:
                self.initial_state = self._state_name_list[0]
                break
            elif len(state) > 1 \
                    or state not in self._state_name_list:
                continue
            self.initial_state = state
            break

    def set_final_state(self):
        while True:
            state = input('Input final state: ')
            state = state.upper()
            if bool(state) is False:
                self.final_state = self._state_name_list[len(self._state_name_list) - 1]
                break
            elif len(state) > 1 \
                    or state not in self._state_name_list:
                continue
            self.final_state = state
            break

    def set_rules_via_cli(self) -> dict:
        for st in self._state_name_list:
            print('{}:'.format(st))
            state = State(self, st)
            for target in self._alphabet:
                while True:
                    action = input('Action [{}]: '.format(target))
                    action = action.upper()
                    if len(action) > 1 \
                            or (action not in self._state_name_list
                                and action != ''):
                        continue
                    state.set_rule(target, action)
                    break
            self._state_dict[state.state] = state.rules
        return self._state_dict

    def get_rule(self, initial: str, target: str) -> str:
        return self._state_dict[initial][target]


class State:
    def __init__(self, dfsm: DFSM, state: str):
        self._dfsm = dfsm
        self._rules = dict()

        if state not in self._dfsm.state_name_list:
            raise ValueError
        self._state = state

    def __del__(self):
        pass

    def __str__(self):
        return '{}: {}'.format(self._state, self._rules)

    def __repr__(self):
        return str(self)

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, value):
        pass

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        pass

    def set_rule(self, literal: str, value: str):
        self._rules[literal] = value


class Chain:
    def __init__(self, dfsm: DFSM, row=None):
        """
        :type dfsm:DFSM
        :type row:list
        """
        self._dfsm = dfsm
        self._current_state = dfsm.initial_state
        self._history = list(self._current_state)
        if not row:
            self._row = list()
            self._is_filled = False
        else:
            self._row = row
            self._is_filled = True

    def __str__(self):
        row = ''
        for r in self._row:
            row += r + ' '
        return row.strip()

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, value):
        pass

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        pass

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value: list):
        if not isinstance(value, list):
            raise TypeError
        for item in value:
            if not isinstance(item, str):
                raise TypeError
            elif item not in self._dfsm.alphabet \
                    or len(item) > 1:
                raise ValueError
            self._row.append(item.strip())
        self._is_filled = True

    def fill_via_cli(self):
        if not self._is_filled:
            print('Enter the chain')
            while True:
                item = input('item: ')
                if bool(item) is False:
                    break
                elif item not in self._dfsm.alphabet:
                    print('not in alphabet')
                    continue
                elif len(item) > 1:
                    continue
                self._row.append(item.strip())
            self._is_filled = True

    def check(self) -> bool:
        for i in self._row:
            rule = self._dfsm.get_rule(self._current_state, i)
            self._current_state = rule
            self._history.append(self._current_state)

        return True if self._current_state == self._dfsm.final_state else False


def _main():
    # Mocked
    dfsm = DFSM()
    dfsm.state_name_list = ['a', 'b', 'c']
    dfsm.alphabet = ['x', 'y', 'z']
    dfsm.initial_state = 'a'
    dfsm.final_state = 'c'
    dfsm.state_dict = {'a': {'x': 'b', 'y': '', 'z': ''},
                       'b': {'x': 'c', 'y': 'c', 'z': 'c'},
                       'c': {'x': 'b', 'y': 'b', 'z': 'b'}}
    chain = Chain(dfsm, ['x', 'x', 'x', 'x'])

    # Manual
    # dfsm = DFSM()
    # dfsm.set_state_name_list()
    # dfsm.set_alphabet()
    # dfsm.set_initial_state()
    # dfsm.set_final_state()
    # dfsm.set_rules_via_cli()
    # chain = Chain(dfsm)
    # chain.fill_via_cli()

    print(dfsm.state_dict)

    print('state_name_list')
    print(dfsm.state_name_list)
    print('alphabet')
    print(dfsm.alphabet)
    print('initial_state')
    print(dfsm.initial_state)
    print('final_state')
    print(dfsm.final_state)

    print('chain')
    print(chain)

    print(chain.check())
    print('history')
    print(chain.history)


if __name__ == '__main__':
    _main()
