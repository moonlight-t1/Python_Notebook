## keyword argument
weight_diff = 0.5
time_diff = 3


def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period


pounds_per_hour = flow_rate(
    weight_diff, time_diff, period=300, units_per_kg=2.2
)  # keyword argument
