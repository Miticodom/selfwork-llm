import ollama

MODEL = "llama3.2"

input_text = input("Enter text: ")

response = ollama.chat(
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

print(response["message"]["content"])