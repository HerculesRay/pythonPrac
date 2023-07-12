import spacy
import networkx as nx
import matplotlib.pyplot as plt


class ComplexFunc:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def find_obj(self, sentence):
        objects = []
        buffer_obj = None
        for word in sentence:
            if word.dep_ in ('obj', 'dobj', 'pobj'):
                buffer_obj = word
                objects.append(word)
        return objects, buffer_obj

    def build_graph(self, sentence):
        doc = self.nlp(sentence)
        graph = nx.Graph()
        objects, buffer_obj = self.find_obj(doc)

        for word in doc:
            if word is buffer_obj:
                graph.add_node(word.text, type='object')
            else:
                graph.add_node(word.text, type='other')

        for word in doc:
            if word.dep_ != 'ROOT' and word.head != buffer_obj and word.head.text != buffer_obj.text:
                graph.add_edge(word.head.text, word.text, relationship=word.dep_)

        return graph


# Example usage
sentence = "I ate an apple and drank a glass of water."
complex_func = ComplexFunc()
graph = complex_func.build_graph(sentence)
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos, with_labels=True)
plt.show()
