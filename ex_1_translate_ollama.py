import ollama

MODEL = "llama3.2"

input_text = input("Enter text: ")

response = ollama.chat(
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

print(response["message"]["content"])