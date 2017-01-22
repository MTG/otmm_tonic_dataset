[![DOI](https://zenodo.org/badge/23745687.svg)](https://zenodo.org/badge/latestdoi/23745687) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-ff69b4.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/) [![Build Status](https://travis-ci.org/MTG/otmm_tonic_dataset.svg?branch=master)](https://travis-ci.org/MTG/otmm_tonic_dataset)

otmm_tonic_dataset
=================================

**Erratum:** We have recently discovered a few errors in the tonic annotations listed in atli2015tonic_fma. The annotations are currently being revised.

The tonic test datasets for classical Ottoman-Turkish makam music

Introduction
------------

This repository contains datasets of annotated tonic frequencies of the audio recordings of Ottoman-Turkish makam music. If you use the dataset in your work, please cite:

> Şentürk, S. (2016). Computational Analysis of Audio Recordings and Music Scores for the Description and Discovery of Ottoman-Turkish Makam Music. PhD thesis, Universitat Pompeu Fabra, Barcelona, Spain.

Note that the annotations are compiled from several [research papers](#References) published under the CompMusic project. For more information about the original datasets, please refer to the relevant paper.

Each annotated recording is uniquely identified with a [MusicBrainz MBID](https://musicbrainz.org/doc/MusicBrainz_Identifier). The tonic symbol is also for each recording given in the format [letter][octave][accidental][comma], e.g. *B4b1* (according to AEU theory).

Each recording is annotated by at least expert musician or musicologists. The annotations are stored as a list with each annotation including the annotated frequency, source dataset, relevant publication, additional observations written by the annotator and whether the octave of the annotated value is considered (for example, the octave is ambiguous in orchestral instrumental recordings).

Annotation structure
------------

The data is stored as JSON file and organized as a dictionary of recordings. An example recording is displayed below:

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
      "citation": "Şentürk, S., Gulati, S., and Serra, X. (2013). Score Informed Tonic Identification for Makam Music of Turkey. In Proceedings of 14th International Society for Music Information Retrieval Conference (ISMIR 2013), pages 175–180, Curitiba, Brazil.", 
      "value": 175.7, 
      "source": "https://github.com/MTG/otmm_tonic_dataset/blob/7f28c1a3261b9146042155ee5e0f9e644d9ebcfa/senturk2013karar_ismir/tonic_annotations.csv", 
      "tonic_symbol": "A4", 
      "octave_wrapped": true, 
      "observations": "The musicians start playing (in Isfahan Peşrev) the tonic approximately at 175Hz."
    },
    {
      "time_interval": [
        245, 
        324
      ], 
      "citation": "Şentürk, S. (2016). Computational Analysis of Audio Recordings and Music Scores for the Description and Discovery of Ottoman-Turkish Makam Music. PhD thesis, Universitat Pompeu Fabra, Barcelona, Spain.", 
      "value": 185.0, 
      "source": "https://github.com/MTG/otmm_tonic_dataset/", 
      "tonic_symbol": "A4", 
      "octave_wrapped": true, 
      "observations": "At the 245th second mark, the virtuosos somehow lose their coordination and the melodic intervals are mixed. The tonic played at the conclusion (e.g. the karar note) of the first performance (Isfahan Peşrev) is around 185 Hz."
    }, 
    {
      "time_interval": [
        326, 
        866
      ], 
      "citation": "Şentürk, S. (2016). Computational Analysis of Audio Recordings and Music Scores for the Description and Discovery of Ottoman-Turkish Makam Music. PhD thesis, Universitat Pompeu Fabra, Barcelona, Spain.", 
      "value": 169.0, 
      "source": "https://github.com/MTG/otmm_tonic_dataset/", 
      "tonic_symbol": "A4", 
      "octave_wrapped": true, 
      "observations": "Isfahan Sazsemaisi has a relatively stable tonic frequency at around 169Hz. Note that the historical recordings tend to have local pitch shifts which makes it hard to identify a precise or correct tonic frequency."
    }
}
```

Additional resources
------------
Most of the recordings in this dataset cannot be shared due to copyright. However relevant features are already computed and they can be downloaded from the [Dunya-makam](dunya.compmusic.upf.edu/makam) after registration. Please refer to the API documentation (http://dunya.compmusic.upf.edu/docs/makam.html) to how to access the data. 

<a name="References"></a>References
--------------------

> Şentürk, S. (2016). Computational Analysis of Audio Recordings and Music Scores for the Description and Discovery of Ottoman-Turkish Makam Music. PhD thesis, Universitat Pompeu Fabra, Barcelona, Spain.

> Şentürk, S., & Serra X. (2016). Composition Identification in Ottoman-Turkish Makam Music Using Transposition-Invariant Partial Audio-Score Alignment. In Proceedings of 13th Sound and Music Computing Conference (SMC 2016). pages 434-441, Hamburg, Germany

> Karakurt, A., Şentürk S., & Serra X. (2016). MORTY: A Toolbox for Mode Recognition and Tonic Identification. In Proceedings of 3rd International Digital Libraries for Musicology Workshop (DLfM 2016). pages 9-16, New York, NY, USA

> Atlı, H. S., Bozkurt, B., Şentürk, S. (2015). A Method for Tonic Frequency Identification of Turkish Makam Music Recordings. In Proceedings of 5th International Workshop on Folk Music Analysis (FMA 2015), pages 119–122, Paris, France.

> Şentürk, S., Gulati, S., and Serra, X. (2013). Score informed tonic identification for makam music of Turkey. In Proceedings of 14th International Society for Music Information Retrieval Conference (ISMIR 2013), pages 175–180, Curitiba, Brazil.

<a name="License"></a>License
--------------------
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
