import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ad(product, audience, platform, cta):
    prompt = f'''
    Create a high-converting ad for {platform}.

    Product: {product}
    Target Audience: {audience}
    Call to Action: {cta}

    Include:
    - Headline
    - Ad Caption
    - Value Proposition
    - Hashtags
    - Creative Image Concept
    '''
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
