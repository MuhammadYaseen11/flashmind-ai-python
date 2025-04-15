from transformers import pipeline

question_gen = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_flashcards(text):
    prompt = f"""
    You are an AI that generates flashcards. Read the text below and create 5 Q&A flashcards in this format:

    Q1: [question]
    A1: [answer]
    Q2: ...
    A2: ...
    
    Text:
    {text}
    """
    result = question_gen(prompt, max_length=512, do_sample=True, temperature=0.7)
    return result[0]['generated_text']
