import csv
import json
import re


def extract_budget(message):
    patterns = [
        r"AED\s?[\d,]+(?:\.\d+)?\s?(?:million|m|k)?",
        r"\b\d+(?:\.\d+)?\s?(?:million|m|k)\b",
        r"\b\d{5,9}\b"
    ]

    for pattern in patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            return match.group(0)

    return "Not specified"


def extract_bedrooms(message):
    match = re.search(r"\b(\d+)\s?(?:bed|bedroom|br)\b", message, re.IGNORECASE)
    if match:
        return match.group(1)

    if re.search(r"\bstudio\b", message, re.IGNORECASE):
        return "Studio"

    return "Not specified"


def extract_property_type(message):
    property_types = ["villa", "apartment", "townhouse", "studio", "penthouse", "office"]

    for property_type in property_types:
        if property_type in message.lower():
            return property_type.title()

    return "Not specified"


def extract_location(message):
    locations = [
        "Dubai Marina",
        "Downtown Dubai",
        "Business Bay",
        "JVC",
        "Palm Jumeirah",
        "Dubai Hills",
        "Arabian Ranches",
        "Jumeirah"
    ]

    for location in locations:
        if location.lower() in message.lower():
            return location

    return "Not specified"


def extract_inquiry_type(message):
    text = message.lower()

    if "rent" in text or "lease" in text:
        return "Rent"
    if "buy" in text or "purchase" in text:
        return "Buy"
    if "sell" in text:
        return "Sell"
    if "invest" in text or "investment" in text:
        return "Investment"

    return "General Inquiry"


def extract_urgency(message):
    text = message.lower()

    if any(word in text for word in ["urgent", "asap", "today", "immediately"]):
        return "High"
    if any(word in text for word in ["this week", "soon", "next few days"]):
        return "Medium"

    return "Normal"


def extract_client_name(message):
    patterns = [
        r"my name is ([A-Za-z ]+)",
        r"this is ([A-Za-z ]+)",
        r"i am ([A-Za-z ]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            name = match.group(1).strip()
            return name.split(".")[0].strip()

    return "Unknown"


def parse_message(message):
    return {
        "client_name": extract_client_name(message),
        "inquiry_type": extract_inquiry_type(message),
        "property_type": extract_property_type(message),
        "location": extract_location(message),
        "budget": extract_budget(message),
        "bedrooms": extract_bedrooms(message),
        "urgency": extract_urgency(message),
        "notes": message
    }


def main():
    input_file = "sample_messages.csv"
    csv_output_file = "structured_leads.csv"
    json_output_file = "structured_records.json"

    structured_records = []

    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            message = row["message"]
            structured_record = parse_message(message)
            structured_records.append(structured_record)

    with open(csv_output_file, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "client_name",
            "inquiry_type",
            "property_type",
            "location",
            "budget",
            "bedrooms",
            "urgency",
            "notes"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(structured_records)

    with open(json_output_file, "w", encoding="utf-8") as file:
        json.dump(structured_records, file, indent=4)

    print("Structured records created successfully.")
    print(json.dumps(structured_records, indent=4))


if __name__ == "__main__":
    main()
