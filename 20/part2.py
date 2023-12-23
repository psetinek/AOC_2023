from collections import deque
import numpy as np


class BroadcasterModule:
    def __init__(self, destination_modules):
        self.destination_modules = destination_modules


class FlipFlopModule(BroadcasterModule):
    def __init__(self, destination_modules):
        super().__init__(destination_modules)  # Initialize the parent class
        self.on = False


class ConjunctionModule(BroadcasterModule):
    def __init__(self, destination_modules):
        super().__init__(destination_modules)  # Initialize the parent class
        self.last_received = {}


modules = {}  # module_name: Module instance
# parse inputs
with open("input.txt", "r") as file:
    for line in file:
        name, to = line.strip().split(" -> ")
        to = to.split(", ")

        if name[0] == "%":
            # flip-flop
            module = FlipFlopModule(to)
            modules[name[1:]] = module

        elif name[0] == "&":
            # conjunction
            module = ConjunctionModule(to)
            modules[name[1:]] = module

        else:
            # broadcaster
            module = BroadcasterModule(to)
            modules[name] = module


# initialize last_received for conjunctions
with open("input.txt", "r") as file:
    for line in file:
        name, to = line.strip().split(" -> ")
        to = to.split(", ")

        for destination_name in to:
            module = modules.get(destination_name)
            if isinstance(module, ConjunctionModule):
                module.last_received[name[1:]] = "low"


# do a BFS over graph with a queue(): (in_module_name, dest_module_name,
# signal_incoming)
# cycles for part 2
cycles = {}


def process_button_push(num_button_push):
    q = deque([("button", "broadcaster", "low")])
    high = 0
    low = 1
    # module will be list of [type, name, state, neighbours]
    while q:
        in_module_name, module_name, signal = q.popleft()
        module = modules.get(module_name)

        if isinstance(module, FlipFlopModule):
            if signal == "low":
                module.on = not module.on
                if module.on:
                    # send high pulse
                    for destination_module in module.destination_modules:
                        q.append((module_name, destination_module, "high"))
                        high += 1
                elif not module.on:
                    # send low pulse
                    for destination_module in module.destination_modules:
                        q.append((module_name, destination_module, "low"))
                        low += 1
                else:
                    raise ValueError
            elif signal == "high":
                pass
            else:
                raise ValueError

        elif isinstance(module, ConjunctionModule):
            # update memory
            module.last_received[in_module_name] = signal
            # if all remembered signals are high, send low
            all_high = True
            for signal in module.last_received.values():
                if signal == "low":
                    all_high = False
                    break
            if all_high:
                # send low
                signal_to_send = "low"
                low += len(module.destination_modules)
            else:
                # send high
                signal_to_send = "high"
                high += len(module.destination_modules)
                # check for part 2
                if module_name in ["cm", "xf", "gc", "sz"]:
                    cycle = cycles.get(module_name)
                    if not cycle:
                        cycles[module_name] = num_button_push
                    # check if all cycles are found
                    if len(cycles) == 4:
                        return True
            # send
            for destination_module in module.destination_modules:
                q.append((module_name, destination_module, signal_to_send))

        elif isinstance(module, BroadcasterModule):
            for destination_module in module.destination_modules:
                q.append((module_name, destination_module, signal))
                low += 1

        else:
            pass
    return False


# check when we reached a circle
low_out, high_out = 0, 0
found_all_cycles = False
i = 1
while not found_all_cycles:
    found_all_cycles = process_button_push(i)
    i += 1

print(np.lcm.reduce(list(cycles.values())))
