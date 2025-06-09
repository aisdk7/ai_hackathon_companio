import pandas as pd
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_databricks import ChatDatabricks
from databricks.sdk import WorkspaceClient
import os

# Configure workspace tokens
w = WorkspaceClient()
os.environ["DATABRICKS_HOST"] = w.config.host
os.environ["DATABRICKS_TOKEN"] = w.tokens.create(comment="for model serving", lifetime_seconds=1200).token_value

llm = ChatDatabricks(endpoint="databricks-llama-4-maverick")

def format_context(df: pd.DataFrame) -> str:
    """
    Converts the DataFrame into a JSON string for structured LLM input.
    """
    return df.to_json(orient='records', indent=2)

def generate_dynamic_sql(location: str, user_input: str) -> str:
    """
    Dynamically generates SQL for ADA booking agent workflow based on user input and location.
    """
    ada_keywords = ["disability", "disabled", "wheel chair", "wheelchair", "ADA", "ADA compliant", "ADA compilant"]
    ada_filter = any(kw.lower() in user_input.lower() for kw in ada_keywords)


    sql = f"""
        SELECT
            title,
            city,
            property_highlights,
            review_score,
            location,
            availability
        FROM `hackathon`.`bright_initiative`.`booking_hotel_listings_csv`
        WHERE city ILIKE '%{location}%'
    """
    if ada_filter:
        sql += " AND ("
        sql += " OR ".join([f"property_highlights ILIKE '%{kw}%'" for kw in ada_keywords])
        sql += ")"
    sql += " ORDER BY review_score DESC LIMIT 5"
    #print(sql)
    return sql

def ada_booking_agent_workflow(location: str, user_input: str) -> list:
    """
    Step 1: Filter listings for location and ADA compliance (if needed).
    Step 2: Pick top 5 recommendations by review_score.
    Step 3: Display results in structured format as a list of dicts.
    """
    query = generate_dynamic_sql(location, user_input)
    df = spark.sql(query).toPandas()
    # Convert DataFrame to list of dicts for iteration
    result_list = df.to_dict(orient='records')
    return result_list
    # If you want to keep the LLM summary, you can return both:
    # return {"list": result_list, "summary": summary}

# Example usage:
if __name__ == "__main__":
    user_location = "Chicago"
    user_input = "Wheelchair"
    result = ada_booking_agent_workflow(user_location, user_input)
    print(result)
