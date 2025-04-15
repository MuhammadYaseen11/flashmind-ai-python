from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_facts(text):
    prompt = f"""
    Extract 5 important factual statements from the following text:

    {text}
    """
    response = generator(prompt, max_length=256, do_sample=False, temperature=0.3)
    return response[0]['generated_text']

def generate_flashcards(text):
    facts = generate_facts(text).split('\n')
    qna_pairs = []

    for i, fact in enumerate(facts[:5]):
        prompt = f"""
        Convert this fact into a flashcard:

        Fact: {fact.strip()}
        Format:
        Q{i+1}: [Question]
        A{i+1}: [Answer]
        """
        result = generator(prompt, max_length=128, do_sample=False, temperature=0.3)
        qna_pairs.append(result[0]['generated_text'])

    return "\n".join(qna_pairs)
