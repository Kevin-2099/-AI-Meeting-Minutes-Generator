import gradio as gr
from transformers import pipeline
from langdetect import detect

# =========================
# MODEL
# =========================
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

generator = pipeline(
    "text-generation",
    model=MODEL_NAME,
    device_map="auto",
    torch_dtype="auto",
)

# =========================
# PROMPT (ULTRA DIRECTO)
# =========================
def build_prompt(text, lang):
    if lang == "es":
        return f"""Crea un acta en Markdown con:
Participantes, Temas tratados, Decisiones, Acciones, Próximos pasos.
No inventes información.
Texto:
{text}
"""
    else:
        return f"""Create meeting minutes in Markdown with:
Participants, Topics discussed, Decisions, Action items, Next steps.
Do not invent information.
Text:
{text}
"""

# =========================
# CORE FUNCTION CON MENSAJE DE ESPERA
# =========================
def generate_minutes_with_feedback(meeting_text):
    if not meeting_text.strip():
        return "⚠️ Please paste the meeting text.", ""

    # Mensaje de espera inicial
    status_text = "⚡ Generando acta, esto puede tardar unos minutos…\n≈4–5 minutos según longitud de la reunión"

    try:
        lang = detect(meeting_text)
    except:
        lang = "es"

    prompt = build_prompt(meeting_text, lang)

    output = generator(
        prompt,
        max_new_tokens=600,  
        temperature=0,       
        do_sample=False,     
    )

    result = output[0]["generated_text"].replace(prompt, "").strip()

    # Mensaje final
    final_status = "✅ Acta generada con éxito"
    return result, final_status

# =========================
# UI
# =========================
with gr.Blocks(title="AI Meeting Minutes Generator") as app:
    gr.Markdown(
        """
        # 📝 AI Meeting Minutes Generator
        Convierte transcripciones de reuniones en **actas estructuradas**
        """
    )

    meeting_input = gr.Textbox(
        label="🗣️ Texto de la reunión",
        lines=15,
        placeholder="Pega aquí la transcripción o notas..."
    )

    generate_btn = gr.Button("🚀 Generar acta")

    output = gr.Markdown(label="📄 Acta generada")
    status = gr.Textbox(label="🟡 Estado", interactive=False)

    generate_btn.click(
        fn=generate_minutes_with_feedback,
        inputs=[meeting_input],
        outputs=[output, status]
    )

if __name__ == "__main__":
    app.launch()
