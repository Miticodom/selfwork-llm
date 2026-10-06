import ollama

MODEL = "llama3.2"

data = {"name": "Giovanni", "age": 30, "city": "Roma", "profession": "Ingegnere"}

response = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": (
                "Trasforma i dati strutturati forniti in una descrizione in "
                "italiano, scorrevole e in terza persona, di una o due frasi. "
                "Non elencare le chiavi e i valori, scrivi una frase naturale. "
                "Non aggiungere informazioni che non sono presenti nei dati."
            ),
        },
        {"role": "user", "content": str(data)},
    ],
)

print(response["message"]["content"])