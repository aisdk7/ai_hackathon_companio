"""
ADA-Compliant Attraction List Agent

Workflow:
1. Receive user input and locations.
2. Use LLM to dynamically generate SQL for ADA-compliant attractions.
3. Query the database (mocked here).
4. Use LLM to select top 5 recommendations based on ratings and review count.
5. Display results in a structured format.
"""

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("ADAAttractionAgent").getOrCreate()

# Step 1: Receive user input and locations
def get_user_inputs():
    user_input = input("Describe your accessibility needs (e.g., wheelchair, braille, etc): ")
    locations = input("Enter locations (comma-separated): ")
    return user_input, [loc.strip() for loc in locations.split(",")]

# Step 2: Use LLM to generate dynamic SQL query
def generate_sql_query(user_input, locations):
    # In production, replace this with an LLM call
    location_filter = " OR ".join([f"address ILIKE '%{loc}%'" for loc in locations])
    sql = f'''
    SELECT name, address, reviews_count, rating, services_provided, category
    FROM `hackathon`.`bright_initiative`.`google_maps_businesses_csv`
    WHERE category ILIKE '%attraction%'
      AND ({location_filter})
      AND services_provided ILIKE '%{user_input}%'
    '''
    return sql

# Step 3: Query the database (mocked for this example)
def query_database(sql):
    try:
        df = spark.sql(sql).toPandas()
        data = df.to_dict(orient='records')
        if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
            print("Query did not return valid data.")
            return []
        return data
    except Exception as e:
        print(f"Database query failed: {e}")
        return []

# Step 4: Use LLM to select top 5 recommendations
def get_top_5_recommendations(data):
    if not data or not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
        print("No valid data to recommend.")
        return []
    sorted_data = sorted(data, key=lambda x: (x.get('rating', 0), x.get('reviews_count', 0)), reverse=True)
    return sorted_data[:5]

# Step 5: Display results in structured format
def display_results(results):
    print("\nTop 5 ADA-Compliant Attractions:")
    for idx, item in enumerate(results, 1):
        print(f"{idx}. {item['name']} | Address: {item['address']} | Rating: {item['rating']} | Reviews: {item['reviews_count']} | Services: {item['services_provided']}")

# Main workflow
def attraction_list(user_input, locations ):
    #user_input, locations = get_user_inputs()
    sql = generate_sql_query(user_input, locations)
    #print("\nGenerated SQL Query:\n", sql)
    data = query_database(sql)
    recommendations = get_top_5_recommendations(data)
    #display_results(recommendations)
    return recommendations

if __name__ == "__main__":
    print(attraction_list(*get_user_inputs()))
