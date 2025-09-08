# system_properties.py

system_props = {
    "linearity": """
## Linearity

A system is linear if it satisfies additivity and homogeneity.

### Formal Definition
$$
S[a x_1(t) + b x_2(t)] = a S[x_1(t)] + b S[x_2(t)]
$$

### Practical Example
- Combining two voltage signals in an electrical circuit: If input1 = 2V, input2 = 3V, a linear amplifier outputs a signal equal to the sum of the amplified inputs.
- Mixing audio signals: Playing two sounds simultaneously results in an output that is the sum of both sounds (no distortion).
""",

    "time_invariance": """
## Time Invariance

A system is time-invariant if shifting the input in time shifts the output by the same amount, without changing its shape.

### Formal Definition
If 
$$
x(t) \\xrightarrow{system} y(t)
$$
then for any time shift $t_0$,
$$
x(t - t_0) \\xrightarrow{system} y(t - t_0)
$$

### Practical Example
- Audio delay system: Playing a song 2 seconds later produces the same song delayed by 2 seconds.
- Traffic light controller: If input signals are delayed, the output (light sequence) is delayed by the same time.
""",

    "causality": """
## Causality

A system is causal if its output depends only on current and past inputs.

### Practical Example
- Real-time audio amplifier: The output depends only on the current and previous audio signals, not future signals.
- Thermostat system: Heating depends on the current and past temperature readings, not future temperatures.
""",

    "stability": """
## Stability

A system is stable if a bounded input produces a bounded output (BIBO).

### Practical Example
- Cruise control in a car: Speed remains within safe limits when the input throttle signal is within limits.
- Electronic filter: Input voltage of ±5V produces an output voltage that remains within ±5V.
""",

    "memory": """
## Memory

A system has memory if its output depends on past or future input values.

### Practical Example
- Moving average filter: Output at time t depends on previous input samples.
- Echo in audio system: Output sound depends on current and past sound signals.
- Memoryless system: Instant light switch; output depends only on current input.
"""
}
