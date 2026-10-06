import ollama

MODEL = "llama3.2"

input_text = input("Enter text: ")

response = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": (
                "Genera 3 domande di comprensione sul testo fornito. "
                "Le risposte alle domande devono trovarsi nel testo, non "
                "inventare domande su informazioni assenti. "
                "Rispondi con un elenco numerato (1., 2., 3.), solo le domande, "
                "senza risposte né altro testo."
            ),
        },
        {"role": "user", "content": input_text},
    ],
)

print(response["message"]["content"])