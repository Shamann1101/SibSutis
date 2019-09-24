import re


class DFSM:
    def __init__(self):
        self.states = list()
        self.start = str()
        self.stack_start = str()
        self.stack_alphabet = list()
        self.alphabet = list()
        self.functions = list()
        self.end_states = list()

    def __str__(self):
        return (
                'states: {}\n' +
                'start: {}\n' +
                'stack_start: {}\n' +
                'stack_alphabet: {}\n' +
                'alphabet: {}\n' +
                'functions: {}\n' +
                'end_states: {}'
        ).format(
            self.states,
            self.start,
            self.stack_start,
            self.stack_alphabet,
            self.alphabet,
            self.functions,
            self.end_states
        )

    def check_chain(self, chain: str):
        skip_flag = False
        current_state = self.start
        current_chain = chain
        while len(self.stack_start) > 0 and len(current_chain) > 0:
            if skip_flag:
                skip_flag = False
                continue
            else:
                print('Current state: {}, current chain: {}, stack: {}'.format(current_state,
                                                                               current_chain,
                                                                               self.stack_start))
            rule_found = False
            for f in self.functions:
                rule_found = False
                # print('function:', f)  # FIXME
                if current_state == f[0] \
                        and current_chain[0] == f[1] \
                        and self.stack_start[0] == f[2]:
                    rule_found = True
                    current_chain = current_chain[1:]
                    print('Applying rule:', f)
                    current_state = f[3]
                    if f[4] != 'L':
                        if len(f[4]) == 1:
                            self.stack_start = f[4] + self.stack_start
                        else:
                            self.stack_start = f[4][:-1] + self.stack_start
                    else:
                        print('LAMBDA STEP')
                        self.stack_start = self.stack_start[1:]
                        skip_flag = True
                    break
            if rule_found is False:
                print('Rule not found')
                exit(0)
            print('New state: {}'.format(current_state))

        if current_state not in self.end_states:
            print("Not in end state after chain end")
        elif len(current_chain) != 0 and len(self.stack_start):
            print("Non-empty chain after stack end")
        else:
            print("Chain fits the machine")

    def get_machine(self):
        path = '_machine.txt'
        with open(path, "r") as f:
            contents = f.read()
            machine = re.findall('{.+?}|[aA-zZ]', contents)
            # print('machine:', machine)  # FIXME
            # ['P', '{p,q}', '{0,1}', '{Z,0}', 'S', 'p', 'Z', '{p}']
            self.states = machine[2][1:-1].split(',')
            self.alphabet = machine[1][1:-1].split(',')
            self.stack_alphabet = machine[3][1:-1].split(',')
            self.start = machine[4]
            self.stack_start = machine[5]
            if len(machine[6]) == 3:
                self.end_states = machine[6][1:-1]
            else:
                self.end_states = machine[6][1:-1].split(',')
            func = re.findall('.+', contents)
            # print('func:', func)  # FIXME
            for i in range(1, len(func)):
                self.functions.append(func[i].split(' '))


m = DFSM()
m.get_machine()
# print(m)  # FIXME
m.check_chain('00001111')
