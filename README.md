# 📝 AI Meeting Minutes Generator

Convierte transcripciones o notas de reuniones en actas estructuradas en Markdown usando inteligencia artificial.

Este proyecto usa el modelo Mistral-7B-Instruct y una interfaz con Gradio para generar actas automáticamente sin inventar información.

## 🚀 Características

- Genera actas en Markdown con secciones claras:

  - Participantes
  
  - Temas tratados
  
  - Decisiones
  
  - Acciones
  
  - Próximos pasos

- Detección automática de idioma (Español / Inglés)

- Interfaz sencilla basada en Gradio

- Configuración determinista para resultados consistentes

## 🧠 Modelo

- mistralai/Mistral-7B-Instruct-v0.2

- Inferencia mediante transformers.pipeline

- Configuración:

  - temperature = 0
  
  - do_sample = False
  
  - max_new_tokens = 600

Esto asegura que no se invente información y se mantenga coherencia.

## 🖥️ Uso local

Clona este repositorio:

git clone https://github.com/Kevin-2099/AI-Meeting-Minutes-Generator.git

cd AI-Meeting-Minutes-Generator

Crea un entorno virtual e instala dependencias:

python -m venv venv

source venv/bin/activate  # Linux / Mac

venv\Scripts\activate     # Windows

pip install -r requirements.txt

Ejecuta la aplicación:

python app.py

Abre el enlace que aparece en la terminal para usar la interfaz Gradio.

## 🧩 Estructura del acta

El acta generada tendrá las siguientes secciones:

- Participantes

- Temas tratados

- Decisiones

- Acciones

- Próximos pasos

(Si el texto está en inglés, la acta también estará en inglés)

## ⏳ Recomendaciones de uso

Reuniones cortas: ≈ 2–3 min

Reuniones largas: ≈ 4–5 min

Evita subir texto con errores graves de transcripción para mejores resultados

## ⚠️ Limitaciones

No corrige errores del texto original

No inventa información

Calidad depende de claridad de la transcripción

## 📜 Licencia

Este proyecto se distribuye bajo la MIT License.

Consulta el archivo LICENSE para más información.

## 🙌 Autor

Creado por Kevin para automatizar la generación de actas de reuniones usando IA.
Optimizado para claridad, precisión y cero invención.
