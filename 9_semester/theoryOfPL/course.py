import lab1 as l_cfg
import lab2 as l_dfsm


def _main():
    dfsm = l_dfsm.DFSM()
    dfsm.set_state_name_list()
    dfsm.set_alphabet()
    dfsm.set_initial_state()
    dfsm.set_final_state()
    rules = dfsm.set_rules_via_cli()

    print('state_name_list')
    print(dfsm.state_name_list)
    print('alphabet')
    print(dfsm.alphabet)
    print('initial_state')
    print(dfsm.initial_state)
    print('final_state')
    print(dfsm.final_state)

    cfg = l_cfg.CFG()
    cfg.non_terminal = rules.keys()

    for rule in rules:
        cfg.terminal = rules[rule].keys()
        rules_list = list()
        for target in rules[rule]:
            r = rules[rule][target].strip()
            if len(r) > 0:
                rules_list.append('{}{}'.format(target, r))
        cfg.rules[rule] = l_cfg.Rule(cfg, rule, rules_list)

    cfg.target = dfsm.initial_state.upper()
    print(cfg.rules)
    chain_length = input('Chain length: ') or l_cfg.MAX_CHAIN_LENGTH

    cfg_chains = cfg.generate_chains(chain_length)
    print('cfg_chains:')
    print(cfg_chains)

    print('rules')
    print(rules)
    print('terminal')
    print(cfg.terminal)
    print('non_terminal')
    print(cfg.non_terminal)

    for chain in cfg_chains:
        chain_items = list(chain.string)
        chain_items.append('')
        dfsm_chain = l_dfsm.Chain(dfsm, chain_items)
        print(dfsm_chain)
        print(dfsm_chain.check())
        print('history')
        print(dfsm_chain.history)


if __name__ == '__main__':
    _main()
