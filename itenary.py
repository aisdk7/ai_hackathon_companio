"""
ADA Itinerary Agent

This agent combines ADA-compliant hotel and attraction recommendations to build a summarized itinerary for the user, including options for rest, meals, and activities.
"""


# Step 2: Get user input

def get_user_inputs():
    user_input = input("Describe your accessibility needs (e.g., wheelchair, braille, etc): ")
    locations = input("Enter locations (comma-separated): ")
    return user_input, [loc.strip() for loc in locations.split(",")]

# Step 3: Use LLM to summarize into an itinerary (mocked for now)
def build_ada_itenary(hotels, attractions):
    # In production, use LLM to generate a natural language summary
    hotel = hotels[0] if hotels else None
    summary = "Your ADA-compliant itinerary:\n"
    if hotel:
        summary += f"- Stay at {hotel['name']} ({hotel['address']}, Rating: {hotel['rating']}, Services: {hotel['services']}). Meals: {hotel.get('meals', 'Not specified')}.\n"
    if attractions:
        for attraction in attractions:
            summary += f"- Visit {attraction['name']} ({attraction['address']}, Rating: {attraction['rating']}, Services: {attraction['services_provided']}).\n"
    summary += "- Rest periods and meal breaks are included at your hotel.\n- Activities are selected for accessibility.\n"
    return summary

# Step 4: Display the itinerary
def display_itenary(summary):
    print("\n===== ADA-Compliant Itinerary =====")
    print(summary)



def get_hotel_dicts(location, user_input):
    # ada_booking_agent_workflow now returns a list of dicts, not a DataFrame
    hotels_raw = ada_booking_agent_workflow(location, user_input)
    hotels = []
    for row in hotels_raw:
        hotels.append({
            "name": row.get("title", "N/A"),
            "address": row.get("location", "N/A"),
            "rating": row.get("review_score", "N/A"),
            "services": row.get("property_highlights", "N/A")
        })
    return hotels



# Main workflow
def main():
    user_input, locations = get_user_inputs()
    location = locations[0]
    hotels = get_hotel_dicts(location, user_input)
    
    attractions = attraction_list(user_input, locations)

    
    summary = build_ada_itenary(hotels, attractions)
    display_itenary(summary)

if __name__ == "__main__":
    main()
