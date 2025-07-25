import embedding_distances as ed
import os

query = 'The Argentinian Primera B Metropolitana club in the city that won the 1969 Metropolitano plays in what division ?'
gold_passage_1 = 'Club Atl\u00e9tico Chacarita Juniors ( usually known simply as Chacarita ) is an Argentine football club headquartered in Villa Crespo , Buenos Aires , while the stadium is located in Villa Maip\u00fa , General San Mart\u00edn Partido of Gran Buenos Aires . The squad currently plays at Argentine Primera Divisi\u00f3n , the top division of the Argentine football league system .'
gold_passage_2 = 'Club Atl\u00e9tico Los Andes is an Argentine sports club based in the Lomas de Zamora district of Greater Buenos Aires . The football team currently plays in the Primera B , the third division of the Argentine football league system . The club was founded by a group of young people in 1917 , and its name was chosen to commemorate the first balloon flight across the Andes mountain , which had happened in 1916 . Los Andes has had three runs in the Argentine Primera Divisi\u00f3n : the first was in 1961 , the second time was between the 1968 and 1971 Metropolitano championships . Los Andes best ever final position was an 8\u00b0 position overall in 1968 Nacional . The third run in Primera Divisi\u00f3n was in 2000-01 and lasted only one season : Los Andes finished 19th out of 20 teams and was relegated to Primera B Nacional with the worst points average in the division . After some seasons in the lower divisions , in 2014 Los Andes returned to B Nacional after winning a championship of the Primera B Metropolitana , but be relegated in the 2018-19 season .'
gold_passage_3 = 'Club Atl\u00e9tico Platense is an Argentine sports club based in Florida , Buenos Aires . The club nickname is Calamar ( Squid ) after the journalist Palacio Zino said that the team moved like a squid in its ink . Although the club hosts many activities , Platense is mostly known for its football team . Despite being relegated from the Primera Divisi\u00f3n in 1999 , it still remains on the top 20 of the All-time Argentine Primera Divisi\u00f3n table . Platense currently competes in the Primera B Nacional , the second level of the Argentine league system .'
generated_paasage_1 = 'Primera B Metropolitana is one of the regionalized third divisions of the Argentine football league system. It features clubs from the Greater Buenos Aires area and surrounding regions. It is below Primera Nacional and above Primera C in the hierarchy.'
generated_paasage_2 = 'Club Comunicaciones is a football club from Buenos Aires that plays in the Primera B Metropolitana. It is one of several teams in the capital competing at that tier.'
generated_paasage_3 = 'Chacarita Juniors, the winner of the 1969 Metropolitano, is based in Villa Maipú, Buenos Aires. However, in recent years, Chacarita Juniors has fluctuated between the second and third divisions of Argentine football.'

text_list = [query, gold_passage_1, gold_passage_2, gold_passage_3, generated_paasage_1, generated_paasage_2, generated_paasage_3]
passage_list = []
random_passages_file_path = "/shared/mrkouch/OTT-QA/work-with-OTT-QA/passages/ottqa_50_random_passages.txt"
with open(random_passages_file_path, "r", encoding="utf-8") as f:
    passage_list = [line.strip() for line in f if line.strip()]

text_list = text_list + passage_list
embedded_texts = ed.interface.encode_text_list(text_list)
labels = ['query', 'gold 1', 'gold 2', 'gold 3', 'modified 1', 'modified 2', 'modified 3'] + [str(i) for i in range(len(passage_list))]
fig = ed.visualization.plot_embeddings_2d_with_distances(embedded_texts, labels, hover_texts=text_list, highlight_index=0)
fig.show()




