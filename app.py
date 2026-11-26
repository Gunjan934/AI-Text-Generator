from flask import Flask,render_template,request
from services.text_generator import generate_content

app=Flask(__name__)
CONTENT_TYPES=[
    "Article",
    "Blog",
    "Eductational Explanation",
    "Story",
    "Summary"
]
WRITING_STYLES = [
    "Beginner Friendly",
    "Professional",
    "Conversational",
    "Academic",
    "Creative"
]
WORD_LIMITS=[100,200,300,500,700,1000]

@app.route("/")
def home():
    return render_template(
        "index.html",
        content_types=CONTENT_TYPES,
        writing_styles=WRITING_STYLES,
        word_limits=WORD_LIMITS,
        topic="",
        content_type="Article",
        style="Beginner Friendly",
        word_limit=300,
        generated_text=None,
        error=None
    )
@app.route("/generate",methods=["POST"])
def generate():
    topic=request.form.get("topic","").strip()
    content_type=request.form.get("content_type","")
    style=request.form.get("style","")
    word_limit=request.form.get("word_limit","")
    generated_text=None
    error=None

    try: 
        if not topic:  
            raise ValueError("Please enter a topic")  
        if content_type not in CONTENT_TYPES:
            raise ValueError ("Invalid content type.")
        if style not in WRITING_STYLES:
            raise ValueError("Invalid Writing Style.")
        if word_limit not in [str(x)for x in WORD_LIMITS]:
            raise ValueError("Invalid Word limit.")  
        generated_text=generate_content(
            topic,
            content_type,
            style,
            int(word_limit)
        )
    except Exception as e:
         error=str(e)
    
    return render_template(
        "index.html",
        content_types=CONTENT_TYPES,
        writing_styles=WRITING_STYLES,
        word_limits=WORD_LIMITS,
        topic=topic,
        content_type=content_type,
        style=style,
        word_limit=word_limit,
        generated_text=generated_text,
        error=error
    )
if __name__=="__main__":
    app.run(debug=True)