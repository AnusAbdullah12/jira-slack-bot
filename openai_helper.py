import openai
import json
import os
openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def categorize_and_summarize_issues(issues):
    """Uses OpenAI GPT API to categorize and summarize Jira issues."""
    categories = ["New Features", "Bug Fixes", "Improvements"]

    prompt = f"""
    You are an AI assistant that categorizes and summarizes Jira issues into structured release notes.

    ## **Instructions**:
    1. **Categorization**:
       - Classify each issue into one of the following categories:
         - **New Features**
         - **Bug Fixes**
         - **Improvements**
      
    2. **Format the Output**:  
       - Provide a structured JSON object with the following fields for each issue:
         - `Jira ticket #`
         - `Title`
         - `Short description of Fix/Feature/Value Add`
         - `Screenshots / Videos` (if available, otherwise leave empty)
         - `Content edit for review` (leave empty)
         - `Questions, Comments, Notes` (leave empty)

    3. **Example Output**:
    {json.dumps({
        "Bug Fixes": [
            {
                "Jira ticket #": "JIRA-456",
                "Title": "Bug Fix Example - Login Authentication",
                "Short description of Fix/Feature/Value Add": "Resolved bug that prevented users from logging in with their credentials",
                "Screenshots / Videos": "bug_fix.png",
                "Content edit for review": "",
                "Questions, Comments, Notes": ""
            }
        ],
        "New Features": [
            {
                "Jira ticket #": "JIRA-123",
                "Title": "New Dashboard UI",
                "Short description of Fix/Feature/Value Add": "Introduced a redesigned dashboard with enhanced filtering options",
                "Screenshots / Videos": "dashboard_feature.png",
                "Content edit for review": "",
                "Questions, Comments, Notes": ""
            }
        ]
    }, indent=2)}

    ## **Input Issues**:
    {json.dumps(issues, indent=2)}
    """

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.3,
        max_tokens=500
    )

    try:
        raw_content = response.choices[0].message.content  # The raw response from OpenAI
# Remove Markdown code block formatting (```json ... ```)
        cleaned_json = raw_content.strip("```json").strip("```").strip()
        # Now parse the JSON correctly
        parsed_data = json.loads(cleaned_json)
        return parsed_data
    except Exception as e:
        print("Error parsing OpenAI response:", e)
        return None
