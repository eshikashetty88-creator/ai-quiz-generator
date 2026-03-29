from openai import OpenAI

client = OpenAI(api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def generate_quiz(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": f"generate ""
Generate:
1. 5 MCQs with options and answers
2. 3 short questions

Content:
{text}
"""}
        ]
    )
    return response.choices[0].message.content


def generate_flashcards(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": f"""
Create 5 flashcards in Q/A format from this:

{text}
"""}
        ]
    )
    return response.choices[0].message.content
    }
    ]
    )