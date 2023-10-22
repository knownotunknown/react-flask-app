from sentence_transformers import SentenceTransformer, util
import torch
import re

'''
creates a list of sentences for sem_search to query
'''
def split_text(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence]

    return sentences

'''
returns relevant sentences to be highlighted
@param text    the benefits document
'''
def sem_search(text):
    # Creates corpus
    corpus = split_text(text)
    embedder = SentenceTransformer('all-MiniLM-L6-v2')

    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

    # Query sentences:
#     question_queries = [
#     "What kind of health insurance does the company provide?",
#     "Are dental and vision coverage included in our health benefits?",
#     "Is there mental health support as part of our insurance package?",
#     "Does the company offer a 401(k) plan?",
#     "What is the company match for the 401(k)?",
#     "How does the unlimited paid time off work?",
#     "Do we accrue vacation days or is it unlimited?",
#     "Can I work from home or remotely?",
#     "Does the company offer flexible working hours?",
#     "Is there an on-site childcare facility?",
#     "What are the credentials of the educators at the childcare center?",
#     "Is there a budget for continuous learning?",
#     "Can I get reimbursed for attending conferences or buying books?",
#     "Are there any wellness programs or benefits?",
#     "Does the company subsidize gym memberships?",
#     "Are there transportation subsidies or benefits?",
#     "Does the company offer a shuttle service?",
#     "What is the Employee Assistance Program about?",
#     "How can I access counseling or support services?",
#     "How often are company retreats organized?",
#     "Where was the last company retreat held?",
#     "Are meals catered for at the office?",
#     "What kind of cuisines are typically offered?",
#     "Can I purchase company stock at a discount?",
#     "How does the Employee Stock Purchase Plan work?",
#     "What is the company policy on parental leave?",
#     "How long can mothers and fathers take off for the birth/adoption of a child?",
#     "Is this a pet-friendly office?",
#     "Can I bring my dog to work?",
#     "How often are performance bonuses awarded?",
#     "What criteria are used to determine bonus eligibility?"
# ]

    employee_benefits = [
        "comprehensive health coverage",
        "401(k) retirement plan with company match up",
        "unlimited paid time off",
        "flexible work schedules with remote work options and flex hours",
        "free on-site childcare with certified educators",
        "continuous learning allowance annually",
        "wellness programs including gym memberships, meditation sessions, and monthly massages",
        "transportation subsidies and free company shuttle services",
        "employee assistance program (eap) with access to counseling and various support resources",
        "annual company retreats in exotic locations",
        "free daily catered meals with diverse cuisines",
        "employee stock purchase plan (espp) with discounted rates",
        "paid parental leave for mothers and fathers",
        "pet-friendly office",
        "regular performance bonuses"
    ]


    thresh = 0.65 # arbitrary for rn
    for query in queries:
        query_embedding = embedder.encode(query, convert_to_tensor=True)

        cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
        matching_sentences = [(corpus[idx], score) for idx, score in enumerate(cos_scores) if score > thresh]

        print("\n\n======================\n\n")
        print("Query:", query)
        if matching_sentences:
            print("\nSentences in corpus with cosine similarity over 0.65:")
        for sentence, score in matching_sentences:
            print(sentence, "(Score: {:.4f})".format(score))
        else:
            print("\nNo sentences found with cosine similarity over 0.65.")

