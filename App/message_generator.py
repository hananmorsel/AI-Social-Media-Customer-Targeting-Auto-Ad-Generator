import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_message(product, audience, tone, platform):
    prompt = f'''
    Write a {tone} outreach message for {platform}.

    Product: {product}
    Target Audience: {audience}

    Make it:
    - Engaging
    - Short
    - Action-driven
    '''
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
