import sys


def parse_commands(lines):
    commands = []

    for line in lines:
        name, argument = line.split()
        argument = int(argument)
        commands.append((name, argument))

    return commands


def execute_command(command):
    name, argument = command

    if name == "acc":
        return 1, argument
    elif name == "jmp":
        return argument, 0
    elif name == "nop":
        return 1, 0
    else:
        raise ValueError("Unknown command: %s" % name)


def change_command(command):
    name, argument = command

    if name == "acc":
        return command
    elif name == "jmp":
        return "nop", argument
    elif name == "nop":
        return "jmp", argument
    else:
        raise ValueError("Uknown command: %s", name)


def execute(commands):
    accumulator = 0
    current_command_idx = 0
    executed_commands = set()

    while current_command_idx < len(commands):
        if current_command_idx in executed_commands:
            return accumulator, False, executed_commands
        
        executed_commands.add(current_command_idx)
        current_command = commands[current_command_idx]
        index_shift, accumulator_delta = execute_command(current_command)

        current_command_idx += index_shift
        accumulator += accumulator_delta

    return accumulator, True, executed_commands


def find_loop_cause(commands):
    _, _, loop_cause_candidates = execute(commands)

    for candidate in loop_cause_candidates:
        candidate_command = commands[candidate]
        if candidate_command[0] == "acc":
            continue
        fixed_commands = commands[:]
        fixed_commands[candidate] = change_command(candidate_command)
        _, success, _ = execute(fixed_commands)
        if success:
            return candidate

    raise ValueError("Cannot fix commands")


if __name__ == '__main__':
    commands = parse_commands(sys.stdin)
    accumulator, _, _ = execute(commands)
    print("Stage 1:", accumulator)

    cause_idx = find_loop_cause(commands)
    commands[cause_idx] = change_command(commands[cause_idx])
    accumulator, _, _ = execute(commands)
    print("Stage 2:", accumulator)
