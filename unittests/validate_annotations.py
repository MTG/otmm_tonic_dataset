from morty.evaluator import Evaluator
import json


def test_annotations():
    annos = json.load(open('annotations.json'))
    evaluator = Evaluator()

    print("yay")
    raise TypeError
