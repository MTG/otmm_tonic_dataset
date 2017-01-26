[![DOI](https://zenodo.org/badge/23745687.svg)](https://zenodo.org/badge/latestdoi/23745687) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/) [![Build Status](https://travis-ci.org/MTG/otmm_tonic_dataset.svg?branch=master)](https://travis-ci.org/MTG/otmm_tonic_dataset)

otmm_tonic_dataset
=================================

The tonic test datasets for classical Ottoman-Turkish makam music

Introduction
------------

This repository contains datasets of annotated tonic frequencies of the audio recordings of Ottoman-Turkish makam music.

If you use the dataset in your work, please cite:

> Şentürk, S. (2016). Computational Analysis of Audio Recordings and Music Scores for the Description and Discovery of Ottoman-Turkish Makam Music. PhD thesis, Universitat Pompeu Fabra, Barcelona, Spain.

The annotations are compiled from several [research papers](#AnnotationSources) published under the CompMusic project. For more information about the original datasets, please refer to the relevant paper.

There are approximately 2000 recordings annotated in the latest version. Each recording is annotated by at least one expert and half of the recordings are annotated by at least two annotators. When the score is available, score-informed tonic identification _(Şentürk, S., 2016)_ is applied to the recording. The result is included in the dataset after it is verified by a human. 

For detailed statistics, please refer to the the Jupyter notebook, [extras/statistics.ipynb](https://github.com/MTG/otmm_tonic_dataset/blob/master/extras/statistics.ipynb).

Erratum
------------
In November 2016, we discovered several errors in the tonic annotations. Since then, approximately 45 percent of the recordings have been verified by a human annotator and/or by the score-informed tonic identification method proposed in (Şentürk, S., Gulati, S., and Serra, X., 2013). This method is reported to provide near perfect results (>99% on paper's dataset). In addition, the annotations of each recording are cross-validated automatically among each other using continous integration (see: the section [Automatic Validation](#automatic-validation) for details). 

So far, we have validated 2000 annotations and changed around 100 of them. This correspond to a human error of 5%, which is acceptable given the rigor of the task. Note that most of the fixes have been simply adjusting the annotated tonic frequency into a finer precision (<20 cents). 

Annotation structure
------------

The data is stored in the JSON file, [annotations.json](https://github.com/MTG/otmm_tonic_dataset/blob/master/annotations.json) and organized as a dictionary of recordings. Each annotated recording is uniquely identified with a [MusicBrainz MBID](https://musicbrainz.org/doc/MusicBrainz_Identifier). The annotations are stored as a list of dictionaries. Each annotation (in the list) includes the annotated frequency, source dataset, relevant publication, time interval, tonic symbol, observations of the annotator and if the octave of the annotated value is considered (for example, the octave is ambiguous in orchestral instrumental recordings).

An example recording is displayed below:

```json
"ed189797-5c50-4fde-abfa-cb1c8a2a2571": {
  "mbid": "http://musicbrainz.org/recording/ed189797-5c50-4fde-abfa-cb1c8a2a2571", 
  "verified": true, 
  "annotations": [
    {
      "time_interval": [
        1, 
        244
      ], 
      "citation": "\u015eent\u00fcrk, S., Gulati, S., and Serra, X. (2013). Score Informed Tonic Identification for Makam Music of Turkey. In Proceedings of 14th International Society for Music Information Retrieval Conference (ISMIR 2013), pages 175\u2013180, Curitiba, Brazil.", 
      "tonic_symbol": "A4", 
      "source": "https://github.com/MTG/otmm_tonic_dataset/blob/7f28c1a3261b9146042155ee5e0f9e644d9ebcfa/senturk2013karar_ismir/tonic_annotations.csv", 
      "value": 175.7, 
      "octave_wrapped": true, 
      "observations": "The musicians start playing (in Isfahan Pe\u015frev) the tonic approximately at 175Hz."
    }, 
    {
      "time_interval": [
        1, 
        244
      ], 
      "citation": "Atl\u0131, H. S., Bozkurt, B., \u015eent\u00fcrk, S. (2015). A Method for Tonic Frequency Identification of Turkish Makam Music Recordings. In Proceedings of 5th International Workshop on Folk Music Analysis (FMA 2015), pages 119\u2013122, Paris, France.", 
      "tonic_symbol": "A4", 
      "source": "https://github.com/MTG/otmm_tonic_dataset/blob/7f28c1a3261b9146042155ee5e0f9e644d9ebcfa/atli2015tonic_fma/TD2.csv", 
      "value": 175.0, 
      "octave_wrapped": true, 
      "observations": "The musicians start playing (in Isfahan Pe\u015frev) the tonic approximately at 175Hz."
    }, 
    {
      "time_interval": [
        245, 
        324
      ], 
      "citation": "\u015eent\u00fcrk, S. (2016). Computational Analysis of Audio Recordings and Music Scores for the Description and Discovery of Ottoman-Turkish Makam Music. PhD thesis, Universitat Pompeu Fabra, Barcelona, Spain.", 
      "tonic_symbol": "A4", 
      "source": "https://github.com/MTG/otmm_tonic_dataset/tree/senturk2016thesis", 
      "value": 185.0, 
      "octave_wrapped": true, 
      "observations": "At the 245th second mark, the virtuosos somehow lose their coordination and the melodic intervals are mixed. The tonic played at the conclusion (e.g. the karar note) of the first performance (Isfahan Pe\u015frev) is around 185 Hz."
    }, 
    {
      "time_interval": [
        326, 
        866
      ], 
      "citation": "\u015eent\u00fcrk, S. (2016). Computational Analysis of Audio Recordings and Music Scores for the Description and Discovery of Ottoman-Turkish Makam Music. PhD thesis, Universitat Pompeu Fabra, Barcelona, Spain.", 
      "tonic_symbol": "A4", 
      "source": "https://github.com/MTG/otmm_tonic_dataset/tree/senturk2016thesis", 
      "value": 169.0, 
      "octave_wrapped": true, 
      "observations": "Isfahan Sazsemaisi has a relatively stable tonic frequency at around 169Hz. Note that the historical recordings tend to have local pitch shifts which makes it hard to identify a precise or correct tonic frequency."
    }, 
    {
      "time_interval": [], 
      "music_score": "https://github.com/MTG/SymbTr/tree/v2.4.3/txt/isfahan--pesrev--devrikebir----tanburi_cemil_bey", 
      "citation": "\u015eent\u00fcrk, S. (2016). Computational Analysis of Audio Recordings and Music Scores for the Description and Discovery of Ottoman-Turkish Makam Music. PhD thesis, Universitat Pompeu Fabra, Barcelona, Spain.", 
      "value": 88.0, 
      "source": "https://github.com/sertansenturk/tomato/blob/v0.9.1/tomato/joint/jointanalyzer.py#L90", 
      "observations": "Tonic identified from the note models obtained by joint audio-score analysis", 
      "tonic_symbol": "A4", 
      "octave_wrapped": true
    }, 
    {
      "time_interval": [], 
      "music_score": "https://github.com/MTG/SymbTr/tree/v2.4.3/txt/isfahan--sazsemaisi--aksaksemai----tanburi_cemil_bey", 
      "citation": "\u015eent\u00fcrk, S. (2016). Computational Analysis of Audio Recordings and Music Scores for the Description and Discovery of Ottoman-Turkish Makam Music. PhD thesis, Universitat Pompeu Fabra, Barcelona, Spain.", 
      "value": 167.3, 
      "source": "https://github.com/sertansenturk/tomato/blob/v0.9.1/tomato/joint/jointanalyzer.py#L90", 
      "observations": "Tonic identified from the note models obtained by joint audio-score analysis", 
      "tonic_symbol": "A4", 
      "octave_wrapped": true
    }
  ]
}
```

Below, each dictionary key is explained in detail:

__mbid__: String. The URL of the recording MBID in [MusicBrainz](musicbrainz.org)  
__verified__: Boolean. _True_ means all annotations in the recording have been verified by another person within a window of 20 cents to the actual tonic frequency. See _Seeger, C. (1958)_ for the musicological justification of the cent precision.  
__annotations__: List. Holds the list of annotation dictionaries  
__time_interval__: 2 x 1 list of floats. The start and end time stamp of the tonic annotation in the recording. It is used when the tonic frequency (or symbol) changes within the performance. If there is no change, its value is empty.  
__citation__: String. Relevant research paper the annotation is taken from.  
__value__: Float. The annotation frequency in Hz.  
__source__: String. The URL where the annotation is originally taken from. It point to the relevant commit/tag and file, where applicable. Note that the value might be different from the original by the final verifier.  
__tonic_symbol__: String. Symbol of the tonic note according to the AEU theory. It is given in the [SymbTr](https://github.com/MTG/SymbTr) format, i.e. [letter][octave][accidental][comma]. Example: *B4b1*.  
__octave_wrapped__: Boolean. _True_, if the annotator did/could not consider the octave information.  
__observations__: String. The comments provided by the annotator.  
__music_score__: String (joint audio-score analysis only). The name of the SymbTr-score used in the joint analysis

Additional resources
------------
Most of the recordings in this dataset cannot be shared due to copyright. However relevant features are already computed and they can be downloaded from the [Dunya-makam](dunya.compmusic.upf.edu/makam) after registration. Please refer to the API documentation (http://dunya.compmusic.upf.edu/docs/makam.html) to how to access the data. 

During verification, several annotations are removed from time to time due to practical reasons. These recordings are listed in [removed.json](https://github.com/MTG/otmm_tonic_dataset/blob/master/removed.json). You can inspect the json file to see why each particular recording is removed.

Automatic validation
------------
After each commit the annotations in the dataset are validated automatically by running several tests using Travis CI ([link](https://travis-ci.org/MTG/otmm_tonic_dataset)). Currently the tests are:

1. Cross-checking whether all annotations of a recording are at maximum 20 cents apart from each other. Recordings with tonic varying over time are omitted.  
2. The removed annotations in [removed.json](https://github.com/MTG/otmm_tonic_dataset/blob/master/removed.json) are not re-introduced by mistake.  

The tests also report several warnings:

1. The recordings with annotations, which do not have the tonic symbol written.  
2. The number of recordings, which only have a single annotation, hence not cross-checked.  
3. The number of recordings, which have not been verified by a final human.  

These warning will only be shown in Travis CI, if there is a validation error separately. If you'd like to produce the warnings, you have to run the test manually in Python 2.7. To do so:

- Open a terminal  
- Clone the Github repository to your local machine into the current directory  (or wherever you want)
```bash
clone https://github.com/MTG/otmm_tonic_dataset.git
```
- Enter to the folder of the repository  
```bash
cd otmm_tonic_dataset
```
- run "python"  
```bash
python
```
- Then in the Python shell, run:  
```python
from unittests.validate_annotations import test_annotations
test_annotations()
```

<a name="References"></a>References
--------------------

> Seeger, C. (1958). Prescriptive and descriptive music-writing. Music Quarterly, 64(2):184–195.

<a name="AnnotationSources"></a>Annotation Sources
--------------------
> Şentürk, S. (2016). Computational Analysis of Audio Recordings and Music Scores for the Description and Discovery of Ottoman-Turkish Makam Music. PhD thesis, Universitat Pompeu Fabra, Barcelona, Spain.

> Şentürk, S., & Serra X. (2016). Composition Identification in Ottoman-Turkish Makam Music Using Transposition-Invariant Partial Audio-Score Alignment. In Proceedings of 13th Sound and Music Computing Conference (SMC 2016). pages 434-441, Hamburg, Germany

> Karakurt, A., Şentürk S., & Serra X. (2016). MORTY: A Toolbox for Mode Recognition and Tonic Identification. In Proceedings of 3rd International Digital Libraries for Musicology Workshop (DLfM 2016). pages 9-16, New York, NY, USA

> Atlı, H. S., Bozkurt, B., Şentürk, S. (2015). A Method for Tonic Frequency Identification of Turkish Makam Music Recordings. In Proceedings of 5th International Workshop on Folk Music Analysis (FMA 2015), pages 119–122, Paris, France.

> Şentürk, S., Gulati, S., and Serra, X. (2013). Score informed tonic identification for makam music of Turkey. In Proceedings of 14th International Society for Music Information Retrieval Conference (ISMIR 2013), pages 175–180, Curitiba, Brazil.

<a name="License"></a>License
--------------------
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
