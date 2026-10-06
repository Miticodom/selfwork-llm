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
                "Estrai dal testo fornito queste informazioni sulla persona: "
                "nome, età e professione. "
                "Rispondi esattamente in questo formato, una riga per campo:\n"
                "Nome: ...\n"
                "Età: ...\n"
                "Professione: ...\n"
                "Se un'informazione non è presente nel testo, scrivi 'non indicato'. "
                "Non inventare dati e non aggiungere altro testo."
            ),
        },
        {"role": "user", "content": input_text},
    ],
)

print(completion.choices[0].message.content)