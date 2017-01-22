from morty.evaluator import Evaluator
import json
import numpy as np
import warnings


def test_annotations():
    # load the tonic annotations
    all_annos = json.load(open('annotations.json'))
    eval_dict = {}
    mismatch_mbid = []
    num_verified = 0
    for rec_mbid, rec_annos in all_annos.items():
        num_verified += rec_annos['verified']
        anno_freqs = [anno['value'] for anno in rec_annos['annotations']]

        # evaluate
        evals = cross_evaluate_annotations(anno_freqs)

        eval_dict[rec_mbid] = {'all': evals.all(), 'eval': evals}
        if not evals.all():
            print('http://dunya.compmusic.upf.edu/makam/recording/' + rec_mbid)
            mismatch_mbid.append(rec_mbid)

    if num_verified != len(all_annos):
        warnings.warn(RuntimeWarning,
                      "{:d}/{:d} recordings are not verified".format(
                          len(all_annos) - num_verified, len(all_annos)))
        
    assert not mismatch_mbid, "There are inconsistent annotations in %d " \
                              "recordings" % len(mismatch_mbid)


def cross_evaluate_annotations(anno_freqs):
    evaluator = Evaluator()

    evals = np.zeros((len(anno_freqs), len(anno_freqs)), dtype=bool)
    for i1, v1 in enumerate(anno_freqs):
        for i2, v2 in enumerate(anno_freqs):
            evals[i1, i2] = evaluator.evaluate_tonic(v1, v2)['tonic_eval']

    return evals
