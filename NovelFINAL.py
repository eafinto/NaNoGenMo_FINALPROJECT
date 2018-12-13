import random
import markovify
import dominate
from dominate.tags import*
import pdfkit

novel = ' '

with open("AllBooks.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(3500):
    novel += str(text_model.make_sentence())
    
    r = random.randint(0,100)
    
    if (r<36):
        novel += "\n\n"
        
sectioned = novel.split("\n\n")
doc = dominate.document(title = 'The Banned Ones')
with doc.head:
    style("body {background-color: white; color: black; font-size: 25pt}")

with doc: 
    h1("The Banned Ones")
    p("A Final Project by Elizabeth Finto")
    
    for s in sectioned: 
        p(s)

pdfkit.from_string(str(doc.render()), 'the_banned_ones.pdf')

print(doc)

len(novel.split(" "))
