from flask import Flask, request, render_template
from random import randint, choice, sample

from stories import story

# from mystories import Story


app = Flask(__name__) #,template_folder="Templets") can look for html file in another folder if needed



#MY HARD CODED MADLIB

# @app.route("/")
# def form:
#     return render_template("form.html")

# @app.route("/madlib")
# def generate_madlib():
#     place = request.args['place']
#     noun = request.args['noun']
#     adjective = request.args['adjective']
#     plural_noun = request.args['plural_noun']
#     verb = request.args['verb']
#     return render_template('madlib.html', place=place, noun=noun, adjective=adjective, plural_noun=plural_noun, verb=verb)

#MY HARD CODED MADLIB



@app.route("/")
def ask_questions():
    """Generate and show form to ask words."""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)




