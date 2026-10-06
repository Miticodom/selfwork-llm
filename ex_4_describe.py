import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL") or None,
)
MODEL = os.getenv("MODEL")

data = {"name": "Giovanni", "age": 30, "city": "Roma", "profession": "Ingegnere"}


completion = client.chat.completions.create(
    model=MODEL,
    messages=[
                {
            "role": "system",
            "content": (
                "trasforma i dati strutturati in una descrizione in italiano, scorrevole e in terza persona, una o due frasi, senza elencare chiave: valore e senza aggiungere informazioni che non ci sono."
            ),
        },
          {"role": "user", "content": str(data)},
    ],
)
risposta = completion.choices[0].message.content
print(risposta)
print(f"[{len(risposta)} caratteri]")