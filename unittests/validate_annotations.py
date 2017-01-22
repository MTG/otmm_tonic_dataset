from morty.evaluator import Evaluator
import json
import numpy as np


def test_annotations():
    evaluator = Evaluator()

    # load the tonic annotations
    annos = json.load(open('annotations.json'))
    eval_dict = {}
    mismatch_mbid = []
    for rm, av in annos.items():
        # evaluate
        vals = [ava['value'] for ava in av['annotations']]
        evals = np.zeros((len(vals), len(vals)), dtype=bool)
        for i1, v1 in enumerate(vals):
            for i2, v2 in enumerate(vals):
                evals[i1, i2] = evaluator.evaluate_tonic(v1, v2)['tonic_eval']

        eval_dict[rm] = {'all': evals.all(), 'eval': evals}
        if not evals.all():
            print('http://dunya.compmusic.upf.edu/makam/recording/' + rm)
            mismatch_mbid.append(rm)

    assert not mismatch_mbid, "There are inconsistent annotations in %d " \
                              "recordings" % len(mismatch_mbid)
