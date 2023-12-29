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
        "You get comprehensive health coverage.",
        "You get 401(k) retirement plan with company match up.",
        "You get unlimited paid time off.",
        "You get flexible work schedules with remote work options and flex hours.",
        "You get free on-site childcare with certified educators.",
        "You get continuous learning allowance annually.",
        "You get wellness programs including gym memberships, meditation sessions, and monthly massages.",
        "You get transportation subsidies and free company shuttle services.",
        "You are provided life insurance and disability coverage.",
        "You have access to professional development and training programs.",
        "You get performance bonuses and stock options.",
        "You have access to employee assistance programs for mental health support.",
        "You get maternity and paternity leave benefits.",
        "You have options for telecommuting and work-from-home arrangements.",
        "You are offered tuition reimbursement for further education.",
        "You receive discounts on company products and services.",
        "You have access to on-site fitness centers or fitness-related reimbursements.",
        "You get annual health checkups and health care spending accounts.",
        "You are provided with meal allowances or free meals.",
        "You have access to legal assistance services.",
        "You get relocation assistance for moving for work.",
        "You are offered pet-friendly workplaces and pet insurance.",
        "You receive holiday bonuses and gifts.",
        "You get employee referral bonuses.",
        "You have access to company cars or transportation benefits.",
        "You receive anniversary rewards for years of service.",
        "You get regular team-building events and company retreats.",
        "You have access to on-site wellness facilities like massage therapy.",
        "You are provided with technology stipends for personal devices.",
        "You receive subsidized memberships for clubs or associations.",
        "You get early access to new products or services.",
        "You are eligible for sabbatical leave after a certain period.",
        "You have access to employee recognition and rewards programs.",
        "You get regular career progression and promotion opportunities.",
        "You receive special offers and benefits from partner companies.",
        "You have access to on-site amenities like cafes and lounges.",
        "You get childcare and eldercare assistance benefits.",
        "You are offered custom career planning and mentorship programs.",
        "You get environmentally friendly workplace initiatives.",
        "You receive emergency fund assistance for unforeseen circumstances."
    ]


    sentences = {}
    thresh = 0.575 # arbitrary for rn
    for query in employee_benefits:
        query_embedding = embedder.encode(query, convert_to_tensor=True)

        cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
        matching_sentences = [(corpus[idx], score) for idx, score in enumerate(cos_scores) if score > thresh]
        

        print("\n\n======================\n\n")
        print("Query:", query)
        if matching_sentences:
            print("\nSentences in corpus with cosine similarity over {}:".format(thresh))
            answers = []
            for sentence, score in matching_sentences:
                print(sentence, "(Score: {:.4f})".format(score))
                answers.append(sentence)
            sentences[query] = answers
            #sentences.append(matching_sentences)
        else:
            print("\nNo sentences found with cosine similarity over {}.".format(thresh))
    print(len(sentences.keys()))
    return sentences