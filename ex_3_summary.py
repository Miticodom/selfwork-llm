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
                "riassumi il testo in un unico paragarfo"
                "massimo 255 caratteri. "
                "tieni solo i punti essenziali (chi, cosa, dove, quando)"
                "rispondi solo col riassunto, nient'altro"
            ),
        },
        {"role": "user", "content": input_text},
    ],
)
risposta = completion.choices[0].message.content
print(risposta)
print(f"[{len(risposta)} caratteri]")