import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL") or None,
)
MODEL = os.getenv("MODEL")

input_text = input("Enter text: ")

completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": (
                "Sei un traduttore professionista. Se il testo è in italiano, "
                "traducilo in inglese; se è in inglese, traducilo in italiano. "
                "Mantieni il tono e il significato originali. "
                "Rispondi solo con la traduzione, senza commenti né spiegazioni."
            ),
        },
        {"role": "user", "content": input_text},
    ],
)

print(completion.choices[0].message.content)