import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_persona(product, audience):
    prompt = f'''
    Create a detailed customer persona.

    Product: {product}
    Target Audience: {audience}

    Include:
    - Persona Name
    - Age Range
    - Occupation
    - Goals
    - Pain Points
    - Purchasing Motivation
    - Social Media Behavior
    '''
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
