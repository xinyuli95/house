import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

while True:
    address = input("Enter the address of the property: ")

    property_info = client.models.generate_content(
        model='gemini-2.0-flash-exp',
        contents=f"property details of {address}. must include overview, lot size, number of bedrooms, number of bathrooms, year built. if address is invalid or not found, stop searching and just print: INVALID ADDRESS",
        config=types.GenerateContentConfig(
            temperature=1,
            top_p=0.95,
            top_k=20,
            max_output_tokens=8192,
            response_mime_type='text/plain',
            tools = [
                types.Tool(
                google_search = types.GoogleSearch(),
                ),
            ],
        )
    )

    if "INVALID ADDRESS" in property_info.text:
        print("Invalid address. Please re-enter")
    else:
        # Write the response to a .txt file
        with open("property_info.txt", "w", encoding="utf-8") as file:
            file.write(property_info.text)

        print("Response written to property_info.txt")

        school_info = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            #contents=f"find a list of schools near property at {address} on Zillow.com. must include name, and rating of each school. For each school, find its coordinates in Google Maps and calculate its distance to the property. Use multiple sources if needed",
            
            contents=f"find a list of schools near property at {address} on Zillow.com. must include name, distance to the property, and rating of each school. use other sources if needed",
            config=types.GenerateContentConfig(
                temperature=1,
                top_p=0.95,
                top_k=20,
                max_output_tokens=8192,
                response_mime_type='text/plain',
                tools = [
                    types.Tool(
                    google_search = types.GoogleSearch(),
                    ),
                ],
            )
        )

        # Write the response to a .txt file
        with open("school_info.txt", "w", encoding="utf-8") as file:
            file.write(school_info.text)

        print("Response written to school_info.txt")
        break