"""Track electricity meter readings and calculate tiered utility bills."""

import json
from datetime import datetime
from pathlib import Path

RATE_TIER_1 = 3.5
RATE_TIER_2 = 5.0
RATE_TIER_3 = 7.5
SPIKE_LIMIT = 500
DEFAULT_DATA_FILE = "meters.json"

meters = {}
reading_history = []
tier_rates = [RATE_TIER_1, RATE_TIER_2, RATE_TIER_3]


def record_reading(meter_id, units, history=None):
    """Record a non-negative meter reading and return the reading history."""
    if not isinstance(units, (int, float)) or isinstance(units, bool):
        raise TypeError("Units must be a number.")

    if units < 0:
        raise ValueError("Units cannot be negative.")

    if history is None:
        history = reading_history

    history.append((meter_id, units, datetime.now().isoformat()))
    meters[meter_id] = meters.get(meter_id, 0) + units
    return history


def compute_bill(meter_id, rates=None):
    """Calculate a meter's bill using three consumption tiers."""
    if meter_id not in meters:
        raise KeyError(f"Unknown meter: {meter_id}")

    if rates is None:
        rates = tier_rates

    if len(rates) != 3:
        raise ValueError("Exactly three tariff rates are required.")

    if any(rate < 0 for rate in rates):
        raise ValueError("Tariff rates cannot be negative.")

    units = meters[meter_id]

    if units <= 100:
        return units * rates[0]

    if units <= 300:
        return 100 * rates[0] + (units - 100) * rates[1]

    return (
        100 * rates[0]
        + 200 * rates[1]
        + (units - 300) * rates[2]
    )


def raise_rates(percent):
    """Increase all three tariff rates by the given percentage."""
    if percent < 0:
        raise ValueError("The rate increase cannot be negative.")

    multiplier = 1 + percent / 100
    tier_rates[:] = [rate * multiplier for rate in tier_rates]


def flag_spikes():
    """Return meter IDs whose accumulated usage exceeds the spike limit."""
    return [
        meter_id
        for meter_id, units in meters.items()
        if units > SPIKE_LIMIT
    ]


def load_meter_data(file=DEFAULT_DATA_FILE):
    """Load meter totals from a JSON file when it exists."""
    data_file = Path(file)

    if not data_file.exists():
        meters.clear()
        return

    try:
        with data_file.open("r", encoding="utf-8") as data_handle:
            loaded_data = json.load(data_handle)

        if not isinstance(loaded_data, dict):
            raise ValueError("Meter data must be a JSON object.")

        if any(
            not isinstance(units, (int, float))
            or isinstance(units, bool)
            or units < 0
            for units in loaded_data.values()
        ):
            raise ValueError("Meter totals must be non-negative numbers.")

        meters.clear()
        meters.update(loaded_data)

    except (json.JSONDecodeError, OSError, ValueError) as error:
        raise ValueError(
            f"Could not load valid meter data from {data_file}: {error}"
        ) from error


def save_meter_data(file=DEFAULT_DATA_FILE):
    """Save current meter totals to a JSON file."""
    with Path(file).open("w", encoding="utf-8") as data_handle:
        json.dump(meters, data_handle, indent=2)


def main():
    """Demonstrate meter recording, tariff calculation, and persistence."""
    meters.clear()
    reading_history.clear()
    tier_rates[:] = [RATE_TIER_1, RATE_TIER_2, RATE_TIER_3]

    record_reading("M-01", 120)
    record_reading("M-02", 640)
    record_reading("M-03", 50)

    print(f"Readings stored so far: {len(reading_history)}")

    raise_rates(10)

    print(f"Bill M-01: {compute_bill('M-01'):.2f}")
    print(f"Bill M-03: {compute_bill('M-03'):.2f}")
    print(f"Spikes: {flag_spikes()}")

    adjustment_text = (
        input("Extra non-negative units for M-01 (Enter for 0): ").strip()
        or "0"
    )

    try:
        adjustment = float(adjustment_text)
        record_reading("M-01", adjustment)
    except (ValueError, TypeError) as error:
        print(f"Invalid reading: {error}")
        return

    save_meter_data()
    load_meter_data()
    print(f"Bill M-01 after reload: {compute_bill('M-01'):.2f}")


if __name__ == "__main__":
    main()
