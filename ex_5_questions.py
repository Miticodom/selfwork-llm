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
                "Genera 3 domande di comprensione sul testo fornito. "
                "Le risposte alle domande devono trovarsi nel testo, quindi "
                "niente domande su informazioni che il testo non dice. "
                "Rispondi con un elenco numerato (1., 2., 3.), solo le domande, "
                "senza risposte né altro testo."
            ),
        },
        {"role": "user", "content": input_text},
    ],
)
risposta = completion.choices[0].message.content
print(risposta)
print(f"[{len(risposta)} caratteri]")