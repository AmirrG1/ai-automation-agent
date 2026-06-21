# AI Automation Agent

Clean demo of a Python AI automation workflow that converts unstructured messages into structured records.

> Note: This is a sanitized demo inspired by a real internship automation workflow. Real company data, client names, messages, phone numbers, property details, and private files are not included.

## Project Overview

This project demonstrates how an AI-style automation workflow can process unstructured client messages and convert them into structured records that can be stored in a CSV file or database.

The goal is to simulate a real business automation use case where incoming messages are cleaned, analyzed, and transformed into usable fields such as client name, intent, property type, location, budget, and urgency.

## Key Features

* Processes unstructured text messages
* Extracts structured information from each message
* Converts messages into JSON-style records
* Exports structured records into a CSV file
* Uses only fake sample data
* Designed as a safe public demo with no private company information

## Example Workflow

```text
Unstructured Message
→ Text Cleaning
→ Field Extraction
→ Structured JSON Record
→ CSV Export
```

## Extracted Fields

The demo extracts fields such as:

* Client name
* Inquiry type
* Property type
* Location
* Budget
* Bedrooms
* Urgency level
* Notes

## Tech Stack

* Python
* CSV
* JSON
* Regular expressions
* Data processing logic

## Why This Project Matters

Business teams often receive messy messages through WhatsApp, email, forms, and CRM systems. Manually converting these messages into structured records takes time and can lead to mistakes.

This project demonstrates how automation can reduce manual data entry and improve the quality of business records.

## Privacy Note

This repository does not include real internship files, real company data, client messages, personal names, phone numbers, or private property information. All examples are fictional and created only for demonstration purposes.

## Future Improvements

* Add LLM API integration for smarter extraction
* Add a simple Streamlit dashboard
* Store extracted records in SQLite
* Add error handling and validation
* Add CRM-style lead scoring
* Add support for email or form input

## Author

Amirali Tamizi Horzadeh
GitHub: [@AmirrG1](https://github.com/AmirrG1)
