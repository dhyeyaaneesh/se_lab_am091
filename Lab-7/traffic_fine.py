import re


def _require_string(value, field_name):
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string")
    return value.strip()


def parse_ticket_id(ticket_id):
    """Parse IDs in PREFIX-YYYY-SERIAL format."""
    ticket_id = _require_string(ticket_id, "ticket_id")
    match = re.fullmatch(r"([A-Za-z]+)-([0-9]{4})-([0-9]+)", ticket_id)
    if not match:
        raise ValueError("ticket_id must use PREFIX-YYYY-SERIAL format")
    prefix, year, serial = match.groups()
    return prefix.upper(), int(year), int(serial)


def total_fines(amounts_csv):
    """Sum comma-separated non-negative integer fines, capped at 10000."""
    amounts_csv = _require_string(amounts_csv, "amounts_csv")
    if not amounts_csv:
        raise ValueError("at least one fine amount is required")

    tokens = amounts_csv.split(",")
    amounts = []
    for token in tokens:
        token = token.strip()
        if not re.fullmatch(r"[0-9]+", token):
            raise ValueError("fine amounts must be non-negative integers")
        amounts.append(int(token))

    return min(sum(amounts), 10000)


def speed_excess(reading):
    """Return integer percentage difference between speed and a positive limit."""
    reading = _require_string(reading, "reading")
    match = re.fullmatch(r"([0-9]+)/([0-9]+)", reading)
    if not match:
        raise ValueError("reading must use speed/limit format with non-negative integers")

    speed, limit = map(int, match.groups())
    if limit == 0:
        raise ValueError("speed limit must be greater than zero")

    return (speed - limit) * 100 // limit


def main():
    print("==== Running parse_ticket_id ====")
    user_input = input("Enter a ticket ID (e.g. TF-2024-0456): ")
    try:
        result = parse_ticket_id(user_input)
        print("Ticket Prefix, Year and Serial:", result)
    except ValueError as exc:
        print("Invalid ticket ID:", exc)

    print("\n==== Running total_fines ====")
    user_input = input("Enter fine amounts as CSV (e.g. 500,1200,300): ")
    try:
        result = total_fines(user_input)
        print("Total Fines:", result)
    except ValueError as exc:
        print("Invalid fine amounts:", exc)

    print("\n==== Running speed_excess ====")
    user_input = input("Enter speed/limit (e.g. 72/60): ")
    try:
        result = speed_excess(user_input)
        print("Percent Over Limit:", result)
    except ValueError as exc:
        print("Invalid speed reading:", exc)


if __name__ == "__main__":
    main()
