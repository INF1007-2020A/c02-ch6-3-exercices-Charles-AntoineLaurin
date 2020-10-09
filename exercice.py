#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_brackets(text, brackets):
	#TODO Associer les ouvrantes et fermantes a l'aide d'un dic
	opening_brackets = dict(zip(brackets[0::2], brackets[1::2]))
	closing_brackets = dict(zip(brackets[1::2], brackets[0::2]))
	bracket_stack = []
	# Verifier les ouvertures / fermetures
	for chr in text:
		# si ouvrant
		if chr in opening_brackets:
			#j'empile
			bracket_stack.append(chr)
		elif chr in closing_brackets:
			if len(bracket_stack) == 0 or bracket_stack[-1] != closing_brackets[chr]:
				return False
			bracket_stack.pop()


	return len(bracket_stack) == 0

def remove_comments(full_text, comment_start, comment_end):
	while True:
		debut =  full_text.find(comment_start)
		fin = full_text.find(comment_end)
		# Trouver le prochain debut de commentaire
		# trouver la prochaine fin de commentaire
		# si aucun des deux trouver
			#c'est bon 
		# Si 

		if debut  == -1 and fin ==  -1:
			return full_text
		elif fin < debut or (debut == -1) != (fin == -1):
			return None
		else: 
			return full_text[:debut] + full_text[fin + len(comment_end):]

def get_tag_prefix(text, opening_tags, closing_tags):
	for t in zip(opening_tags, closing_tags):
		if text.startswith(t[0]):
			return (t[0], None)
		elif text.startswith(t[1]):
			return (None, t[1])
		else :
			return (None, None)


def check_tags(full_text, tag_names, comment_tags):
	text = remove_comments(full_text, *comment_tags)
	if  text is None:
		return False

	otags = {f"<{name}>" : f"</{name}>" for name in tag_names}
	ctags = dict((v, k) for k, v in otags.items())

	tag_stack = []

	while len(text) != 0:
		tags = get_tag_prefix(text, otags, ctags)
		#si ouvrant
		if tags[0] is not None:
			# on empile
			tag_stack.append(tags[0])
			text = text[len(tags[0]):]
		# si fermant
		elif tags[1] is not None:
		# si la pile est vide ou mal fait
			# si  pas  bon 
			if len(tag_stack) == 0 or tag_stack[-1] != ctags[tags[1]]:
				return False 
			# on depile
			tag_stack.pop()
			text = text[len(tags[1]):]
		else:
			text = text[1:]
			
	return len(tag_stack) == 0


if __name__ == "__main__":
	brackets = ("(", ")", "{", "}")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, /* OOGAH BOOGAH */world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()

