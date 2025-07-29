import openai

# Prompt examples to condition GPT-4o with few-shot learning
FEW_SHOT_PROMPT = """
You are a helpful assistant that generates a "gold" given a query. The gold consists of:
- a table (structured as a JSON object, with URL, title, headers, data, section text, etc.)
- a few passages (paragraphs of relevant text)

Here are a few examples:

---

query: What is the full birth name of the Bradford A.F.C player that only played for the team in 2011 ?

table: { "url": "https://en.wikipedia.org/wiki/Bradford_City_A.F.C.", "title": "Bradford City A.F.C.", "header": [ [ "Name", [] ], [ "Nation", [] ], [ "Years", [] ] ], "data": [ [ [ "Guy Branston", [ "/wiki/Guy_Branston" ] ], [ "England", [] ], [ "2011", [] ] ] ], "section_title": "Captains", "section_text": "This section needs expansion...", "uid": "Bradford_City_A.F.C._0", "intro": "Bradford City Association Football Club is a professional..." }

passage: Guy Peter Bromley Branston (born 9 January 1979) is an English former professional footballer who played as a centre back...

---

query: The Argentinian Primera B Metropolitana club in the city that won the 1969 Metropolitano plays in what division?

table: { "url": "https://en.wikipedia.org/wiki/1969_Torneo_Metropolitano", "title": "1969 Torneo Metropolitano", "header": [ [ "Position", [] ], [ "Team", [] ], [ "City", [] ], [ "Points", [] ] ], "data": [ [ [ "1", [] ], [ "Chacarita Juniors", [ "/wiki/Chacarita_Juniors" ] ], [ "Buenos Aires", [] ], [ "25", [] ] ] ], "section_title": "Final standings", "section_text": "The 1969 Torneo Metropolitano was a top-level...", "uid": "1969_Torneo_Metropolitano_0", "intro": "The 1969 Torneo Metropolitano was part of the 1969 Argentine Primera División..." }

passage: Primera B Metropolitana is one of the regionalized third divisions of the Argentine football league system...
passage: Club Comunicaciones is a football club from Buenos Aires...
passage: Chacarita Juniors, the winner of the 1969 Metropolitano...

---

Now generate a gold table and passages for the following query:

query: {query}
"""

def generate_gold_table_by_query(query):
    openai.api_key = input("Enter your OpenAI API key: ")

    prompt = FEW_SHOT_PROMPT.format(query=query)

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You generate tables and passages from Wikipedia-like structured data for complex QA tasks."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=2000
    )

    result = response['choices'][0]['message']['content']
    print("\n--- GENERATED OUTPUT ---\n")
    print(result)
    return result

# Example usage
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    generate_gold_table_by_query(user_query)
