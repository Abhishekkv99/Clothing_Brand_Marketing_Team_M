#!/usr/bin/env python
import sys
import os

# Add the 'src' directory to the path so 'marketing_team' can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from marketing_team.crew import MarketingTeamCrew
from dotenv import load_dotenv

load_dotenv()

def run():
    """
    Run the crew.
    """
    # Check for API keys
    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY not found in environment variables.")
    if not os.getenv("SERPER_API_KEY"):
        print("Warning: SERPER_API_KEY not found in environment variables (needed for search tool).")

    inputs = {
        'topic': 'Summer 2024 Beachwear Collection'
    }
    
    try:
        MarketingTeamCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()

