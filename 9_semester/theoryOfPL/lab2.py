class DFSM:
    def __init__(self):
        self.alphabet = list()
        self.state_name_list = list()
        self._state_list = dict()
        self._initial_state = None
        self._final_state = None
        # self._rules = list()

    @property
    def initial_state(self):
        return self._initial_state

    @initial_state.setter
    def initial_state(self, value):
        if value in self.state_name_list:
            self._initial_state = value

    @property
    def final_state(self):
        return self._final_state

    @final_state.setter
    def final_state(self, value):
        if value in self.state_name_list:
            self._final_state = value

    def set_alphabet(self):
        alphabet_list = list()
        while True:
            alphabet = input('Input alphabet: ')
            if bool(alphabet) is False:
                break
            elif len(alphabet) > 1 \
                    or alphabet in alphabet_list:
                continue
            alphabet_list.append(alphabet.strip())

        self.alphabet = alphabet_list if len(alphabet_list) > 0 else ['0', '1', 'a']

    def set_state_list(self):
        state_name_list = list()
        while True:
            state = input('Input state: ')
            if bool(state) is False:
                self._state_list = None
                break
            elif len(state) > 1 \
                    or state in state_name_list:
                continue
            state_name_list.append(state)
            self._state_list = None

        self.state_name_list = state_name_list if len(state_name_list) > 0 else ['p', 'q', 'r']

    def set_initial_state(self):
        while True:
            value = input('Input initial state: ')
            if bool(value) is False \
                    or len(value) > 1 \
                    or value not in self.state_name_list:
                continue
            self.initial_state = value
            break

    def set_final_state(self):
        while True:
            value = input('Input final state: ')
            if bool(value) is False \
                    or len(value) > 1 \
                    or value not in self.state_name_list:
                continue
            self.final_state = value
            break

    def set_rules(self) -> dict:
        self._state_list = dict()
        for st in self.state_name_list:
            print('{}:'.format(st))
            state = State(self, st)
            for target in self.alphabet:
                while True:
                    action = input('Action [{}]: '.format(target))
                    if len(action) > 1 \
                            or (action not in self.state_name_list and action != ' '):
                        continue
                    state.set_rule(target, action)
                    break
            self._state_list[state.state] = state.rules
        print(self._state_list)  # FIXME
        return self._state_list

    def get_rule(self, initial, target: str):
        return self._state_list[initial][target]


class State:
    def __init__(self, dfsm: DFSM, state: str):
        try:
            if not isinstance(state, str):
                raise TypeError
        except TypeError:
            print('Value is wrong type')

        self._dfsm = dfsm
        self._state = state
        self._rules = dict()

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

    def set_rule(self, literal, value: str):
        self._rules[literal] = value


class Chain:
    def __init__(self, dfsm: DFSM, row=None):
        self._dfsm = dfsm
        self._current_state = dfsm.initial_state
        self._history = list(self._current_state)
        if not row:
            self.row = list()
            self._is_filled = False
        else:
            self.row = row
            self._is_filled = True

    def __str__(self):
        row = ''
        for r in self.row:
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

    def fill(self):
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
                self.row.append(item.strip())
            self._is_filled = True

    def check(self) -> bool:
        for i in self.row:
            # print('current_state: {}'.format(self._current_state))  # FIXME
            # print('i: {}'.format(i))  # FIXME
            rule = self._dfsm.get_rule(self._current_state, i)
            # print('get_rule: {}'.format(rule))  # FIXME
            self._current_state = rule
            self._history.append(self._current_state)
        if self._current_state == self._dfsm.final_state:
            # print('Done')  # FIXME
            return True
        else:
            # print('Fail')  # FIXME
            return False


def _main():
    dfsm = DFSM()
    dfsm.set_state_list()
    dfsm.set_alphabet()
    dfsm.set_initial_state()
    dfsm.set_final_state()
    dfsm.set_rules()

    chain = Chain(dfsm)
    chain.fill()

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
