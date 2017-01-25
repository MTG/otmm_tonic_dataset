from morty.evaluator import Evaluator
import json
import numpy as np
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def test_annotations():
    # load the tonic annotations
    all_annos = json.load(open('annotations.json'))
    eval_dict = {}
    mismatch_mbid = []
    time_ignored_mbid = []  # ignored recordings due to tonic changing in time
    num_verified = 0
    num_single_anno = 0
    rec_missing_symbol = []

    logger.info("- Validating {:d} recordings".format(len(all_annos)))

    for rec_mbid, rec_annos in all_annos.items():
        num_verified += rec_annos['verified']

        # get annotated frequency and time interval
        anno_freqs = [anno['value'] for anno in rec_annos['annotations']]
        anno_times = [anno['time_interval']
                      for anno in rec_annos['annotations']]

        if len(anno_freqs) == 1:
            # cannot validate with a single annotation
            num_single_anno += 1
        else:
            # evaluate annotations wrt each other
            evals = cross_evaluate_annotations(anno_freqs)

            eval_dict[rec_mbid] = {'all': evals.all(), 'eval': evals}
            if not evals.all():
                check_mismatches(rec_mbid, anno_times, mismatch_mbid,
                                 time_ignored_mbid)

        # warn missing tonic symbols
        rec_missing_symbol = check_missing_tonic_symbol(rec_annos, rec_mbid,
                                                        rec_missing_symbol)

    # report recordings with a single annotation
    if num_single_anno != 0:
        logging.warning(u"- {:d}/{:d} recordings have a single annotation. "
                        u"They can not be validated.".format(num_single_anno,
                                                             len(all_annos)))

    # report missing tonic symbols
    logging.error(len(rec_missing_symbol))
    if rec_missing_symbol:
        for rr in rec_missing_symbol:
            logging.warning(u"* Missing tonic symbol for http://dunya."
                            u"compmusic.upf.edu/makam/recording/{}".format(rr))
        logging.warning(
            u"- Annotations in {:d}/{:d} recordings have missing "
            u"tonic symbol.".format(len(rec_missing_symbol),
                                    len(all_annos)))

    # report not verified recordings
    if num_verified != len(all_annos):
        logging.warning(u"- {:d}/{:d} recordings are not verified".format(
            len(all_annos) - num_verified, len(all_annos)))

    assert not mismatch_mbid, u"Annotations in {:d} recording(s) are " \
                              u"inconsistent".format(len(mismatch_mbid))


def check_missing_tonic_symbol(rec_annos, rec_mbid, rec_missing_symbol):
    anno_symbols = [anno['tonic_symbol']
                    for anno in rec_annos['annotations']]

    if not all(anno_sym for anno_sym in anno_symbols):
        rec_missing_symbol.append(rec_mbid)

    return rec_missing_symbol


def cross_evaluate_annotations(anno_freqs):
    evaluator = Evaluator(tonic_tolerance=20)  # cents

    evals = np.zeros((len(anno_freqs), len(anno_freqs)), dtype=bool)
    for i1, v1 in enumerate(anno_freqs):
        for i2, v2 in enumerate(anno_freqs):
            evals[i1, i2] = evaluator.evaluate_tonic(v1, v2)['tonic_eval']

    return evals


def check_mismatches(rec_mbid, anno_times, mismatch_mbid, time_ignored_mbid):
    # the annotations, which do not have the "time_interval" key set (i.e.
    # it is an empty list) imply the annotation holds for the complete
    # recording. IF the time_interval is set, the recording should be
    # ignored and checked manually.
    if any(anno_times):
        warnstr = u"* Ignored http://dunya.compmusic.upf.edu/" \
                  u"makam/recording/{} due to tonic changing in " \
                  u"time. Please check the recording manually".format(rec_mbid)
        logging.warning(warnstr)
        time_ignored_mbid.append(rec_mbid)
    else:
        errstr = u"> Mismatch in http://dunya.compmusic.upf.edu/makam/" \
                 u"recording/{}".format(rec_mbid)
        logging.error(errstr)
        mismatch_mbid.append(rec_mbid)


def test_removed():
    """
    This test checks whether one of the removed recordings are re-introduced
    to the test dataset by mistake. If yes, it prompts to recheck the
    recording(s) manually
    """
    all_annos = json.load(open('annotations.json'))
    removed_annos = json.load(open('removed.json'))

    all_mbids = all_annos.keys()
    removed_mbids = removed_annos.keys()

    num_removed = 0
    for am in all_mbids:
        if am in removed_mbids:
            logging.error(u"http://dunya.compmusic.upf.edu/makam/recording/{} "
                          u"was removed from annotations in  the past. "
                          u"Please recheck the comment given in removed.json "
                          u"for the explanation. If you think, the removal "
                          u"was a mistake, please re-annotate and remove the "
                          u"recording from removed.json".format(am))
            num_removed += 1

    assert_str = u"There are {:d}/{:d} recordings, which were removed from " \
                 u"annotations in the past and later re-introduced again " \
                 u"without revising removed.json".format(num_removed,
                                                         len(all_annos))
    assert num_removed == 0, assert_str
