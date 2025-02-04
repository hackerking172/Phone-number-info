import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_number_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)

        # Get country and location
        country = geocoder.description_for_number(parsed_number, "en")

        # Get carrier
        sim_carrier = carrier.name_for_number(parsed_number, "en")

        # Get timezone
        time_zones = timezone.time_zones_for_number(parsed_number)

        # Check validity
        is_valid = phonenumbers.is_valid_number(parsed_number)

        return {
            "Number": phone_number,
            "Country": country,
            "Carrier": sim_carrier,
            "Time Zones": time_zones,
            "Valid Number": is_valid
        }
    except Exception as e:
        return {"Error": str(e)}

# Example Usage
phone_number = "+14155552671"  # Replace with any phone number
info = get_phone_number_info(phone_number)
print(info)