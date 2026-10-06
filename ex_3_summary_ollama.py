import ollama

MODEL = "llama3.2"

input_text = input("Enter text: ")

response = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": (
                "Riassumi il testo fornito in un unico paragrafo di massimo "
                "255 caratteri, spazi inclusi. Mantieni solo i punti essenziali "
                "(chi, cosa, dove, quando). Scrivi in italiano corretto e fluido. "
                "Rispondi solo con il riassunto, senza aggiungere altro testo."
            ),
        },
        {"role": "user", "content": input_text},
    ],
)

risposta = response["message"]["content"]
print(risposta)
print(f"[{len(risposta)} caratteri]")