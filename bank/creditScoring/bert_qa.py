# python  bert_qa.py
from   transformers  import  pipeline 

# The task "question-answering" will return a QuestionAnsweringPipeline object
question_answerer = pipeline(task="question-answering", model="distilbert-base-cased-distilled-squad")
context = """
Tea is an aromatic beverage prepared by pouring hot or boiling water over cured or fresh leaves of Camellia sinensis,
an evergreen shrub native to China and East Asia. After water, it is the most widely consumed drink in the world. 
There are many different types of tea; some, like Chinese greens and Darjeeling, have a cooling, slightly bitter, 
and astringent flavour, while others have vastly different profiles that include sweet, nutty, floral, or grassy 
notes. Tea has a stimulating effect in humans primarily due to its caffeine content.

The tea plant originated in the region encompassing today's Southwest China, Tibet, north Myanmar and Northeast India,
where it was used as a medicinal drink by various ethnic groups. An early credible record of tea drinking dates to 
the 3rd century AD, in a medical text written by Hua Tuo. It was popularised as a recreational drink during the 
Chinese Tang dynasty, and tea drinking spread to other East Asian countries. Portuguese priests and merchants 
introduced it to Europe during the 16th century. During the 17th century, drinking tea became fashionable among the 
English, who started to plant tea on a large scale in India.

The term herbal tea refers to drinks not made from Camellia sinensis: infusions of fruit, leaves, or other plant 
parts, such as steeps of rosehip, chamomile, or rooibos. These may be called tisanes or herbal infusions to prevent
confusion with 'tea' made from the tea plant.
"""

result = question_answerer(question="Where is tea native to?", context=context)
print(result['answer'])


questions = ["Where is tea native to?",
             "When was tea discovered?",
             "What is the species name for tea?"]

results = question_answerer(question=questions, context=context)

for q, r in zip(questions, results):
    print(q, "\n>> " + r['answer'])



