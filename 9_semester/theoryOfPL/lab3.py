class SMM:
    def __init__(self):
        self.state_list = list()
        self.alphabet = list()
        self.stack_alphabet = list()
        self.state_initial = str()
        self.stack_initial = str()
        self.final_state_list = list()
        self.rules = list()


class Rule:
    state_l = 'L'

    def __init__(self, smm: SMM, state_current: str, chain_current: str, stack_current: str, state_new: str,
                 stack_new: str):
        self._smm = smm
        self.state_current = state_current
        self.chain_current = chain_current
        self.stack_current = stack_current
        self.state_new = state_new
        self.stack_new = stack_new
        self._smm.rules.append(self)

    def __del__(self):
        self._smm.rules.remove(self)

    def __str__(self):
        return '"{%s, %s, %s} = {(%s, %s)}"' % (
            self.state_current,
            self.chain_current,
            self.stack_current,
            self.state_new,
            self.stack_new
        )

    def __repr__(self):
        return str(self)


class Chain:
    def __init__(self, smm: SMM, string: str):
        self._smm = smm
        self.string = string
        self._history = list()
        self.stack = self._smm.stack_initial
        self.state = self._smm.state_initial

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        pass

    def check(self) -> (bool, str):
        message = str()
        skip_flag = False
        rule_found = False

        while len(self.stack) > 0 and len(self.string) > 0:
            if skip_flag:
                skip_flag = False
                continue
            # else:
            #     print('Current state: {}, current chain: {}, stack: {}'.format(self.state,
            #                                                                    self.string,
            #                                                                    self.stack))
            for rule in self._smm.rules:
                rule_found = False
                if self.state == rule.state_current \
                        and self.string[0] == rule.chain_current \
                        and self.stack[0] == rule.stack_current:
                    rule_found = True
                    self.string = self.string[1:]
                    self.history.append(rule)
                    self.state = rule.state_new
                    if rule.stack_new != rule.state_l:
                        if len(rule.stack_new) == 1:
                            self.stack = rule.stack_new + self.stack
                        else:
                            self.stack = rule.stack_new[:-1] + self.stack
                    else:
                        self.stack = self.stack[1:]
                        skip_flag = True
                    break
            if not rule_found:
                message = 'Rule not found'
                break

        if self.state not in self._smm.final_state_list:
            message = 'Not in end state after chain end'
        elif len(self.string) != 0 and len(self.stack):
            message = 'Non-empty chain after stack end'
        elif message == '':
            message = 'Chain fits the machine'
        return rule_found, message


def _main():
    # Mocked
    smm = SMM()
    smm.state_list = ['p', 'q']
    smm.alphabet = ['0', '1']
    smm.stack_alphabet = ['Z', '0']
    smm.state_initial = 'p'
    smm.stack_initial = 'Z'
    smm.final_state_list = ['p']
    Rule(smm, 'p', '0', 'Z', 'p', '0Z')
    Rule(smm, 'p', '0', '0', 'p', '00')
    Rule(smm, 'p', '1', '0', 'q', 'L')
    Rule(smm, 'p', 'L', 'Z', 'L', 'L')
    Rule(smm, 'q', 'L', 'Z', 'q', 'L')
    Rule(smm, 'q', '1', '0', 'p', 'L')
    # print(smm.rules)
    chain = Chain(smm, '00001111')
    print(chain.check())
    print(chain.history)


if __name__ == '__main__':
    _main()
