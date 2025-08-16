import re
import requests
import csv
from io import StringIO
from .models import Client
from datetime import datetime


def import_sheet(sheet_url):
    # Extract sheet ID from link
    match = re.search(r"/d/([a-zA-Z0-9-_]+)", sheet_url)
    if not match:
        raise ValueError("Invalid Google Sheet URL")
    sheet_id = match.group(1)

    # Build CSV export URL
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

    # Download
    response = requests.get(csv_url)
    response.raise_for_status()

    # Parse CSV
    f = StringIO(response.text)
    reader = csv.DictReader(f)

    # Save to database
    for row in reader:
        x = row["Address"].split(",")
        y = re.findall("\d{5}", row["Address"])
        z = re.findall("[A-Z]{2}", row["Address"])
        a = re.findall(", [A-Z]{1}.+,", row["Address"])
        street_1 = x[0].replace(",", "") if x != [] else "Empty"
        zp = y[0].replace(",", "") if y != [] else "Empty"
        state = z[0].replace(",", "") if z != [] else "Empty"
        city = a[0].replace(",", "") if a != [] else "Empty"
        Client.objects.update_or_create(
            first=row["Name"].split(" ")[0],
            last=row["Name"].split(" ")[-1],
            defaults={
                "email": row["Email"],
                "birthdate": datetime.strptime(row["DOB"], "%m/%d/%Y").date(),
                "street1": street_1,
                "street2": "Empty",
                "city": city,
                "zip": zp,
                "state": state,
                "phone": row["Phone"],
                "vaccinated": True,
                "photo_preference": True,
                "emergency_contact1": row["EmergencyName1"],
                "emergency_phone1": row["EmergencyPhone1"],
                "emergency_contact2": row["EmergencyName2"],
                "emergency_phone2": row["EmergencyPhone2"],
                "emt_info": row["EMT_Pertinent_Information"],
            },
        )
