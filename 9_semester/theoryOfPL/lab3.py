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
    def __init__(self, smm: SMM):
        self._smm = smm
        self.state_current = str()
        self.chain_current = str()
        self.stack_current = str()
        self.state_new = str()
        self.stack_new = str()


def _main():
    smm = SMM()
    smm.state_list = ['p', 'q']
    smm.alphabet = ['0', '1']
    smm.stack_alphabet = ['Z', '0']
    smm.state_initial = 'p'
    smm.stack_initial = 'Z'
    smm.final_state_list = ['p']


if __name__ == '__main__':
    _main()
