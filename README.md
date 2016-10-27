turkish_makam_tonic_test_datasets
=================================

**Erratum:** We have recently discovered a few errors in the tonic annotations listed in atli2015tonic_fma. The annotations are currently being revised.

The tonic test datasets for classical Ottoman-Turkish makam music

Introduction
------------

This repository contains datasets of annotated tonic frequencies of the audio recordings of Ottoman-Turkish makam music. The annotations are compiled from several [research papers](#References) published under the CompMusic project. For more information about the original datasets, please refer to the relevant paper.

Each annotated recording is uniquely identified with a [MusicBrainz MBID](https://musicbrainz.org/doc/MusicBrainz_Identifier). The tonic symbol is also for each recording given in the format [letter][octave][accidental][comma], e.g. *B4b1* (according to AEU theory).

Each recording is annotated by at least expert musician or musicologists. The annotations are stored as a list with each annotation including the annotated frequency, source dataset, relevant publication, additional observations written by the annotator and whether the octave of the annotated value is considered (for example, the octave is ambiguous in orchestral instrumental recordings).

Annotation structure
------------

The data is stored as JSON file and organized as a dictionary of recordings. An example recording is displayed below:

```json
{
  "mbid": "http://musicbrainz.org/recording/e3a22684-d237-48b5-ac27-e9b77ddd3c18", 
  "verified": true, 
  "annotations": [
    {
      "source": "https://github.com/MTG/otmm_tonic_dataset/blob/7f28c1a3261b9146042155ee5e0f9e644d9ebcfa/senturk2013karar_ismir/tonic_annotations.csv", 
      "citation": "Şentürk, S., Gulati, S., and Serra, X. (2013). Score Informed Tonic Identification for Makam Music of Turkey. In Proceedings of 14th International Society for Music Information Retrieval Conference (ISMIR 2013), pages 175–180, Curitiba, Brazil.", 
      "octave_wrapped": true, 
      "observations": "", 
      "value": 296.9597
    }, 
    {
      "source": "https://github.com/MTG/otmm_tonic_dataset/blob/7f28c1a3261b9146042155ee5e0f9e644d9ebcfa/atli2015tonic_fma/TD2.csv", 
      "citation": "Atlı, H. S., Bozkurt, B., Şentürk, S. (2015). A Method for Tonic Frequency Identification of Turkish Makam Music Recordings. In Proceedings of 5th International Workshop on Folk Music Analysis (FMA 2015), pages 119–122, Paris, France.", 
      "octave_wrapped": true, 
      "observations": "", 
      "value": 296
    }
  ], 
  "tonic_symbol": "D4"
}
```

Additional resources
------------
Most of the recordings in this dataset cannot be shared due to copyright. However relevant features are already computed and they can be downloaded from the [Dunya-makam](dunya.compmusic.upf.edu/makam) after registration. Please refer to the API documentation (http://dunya.compmusic.upf.edu/docs/makam.html) to how to access the data. 

<a name="References"></a>References
--------------------

> Şentürk, S., & Serra X. (2016). Composition Identification in Ottoman-Turkish Makam Music Using Transposition-Invariant Partial Audio-Score Alignment. In Proceedings of 13th Sound and Music Computing Conference (SMC 2016). pages 434-441, Hamburg, Germany

> Karakurt, A., Şentürk S., & Serra X. (2016). MORTY: A Toolbox for Mode Recognition and Tonic Identification. In Proceedings of 3rd International Digital Libraries for Musicology Workshop (DLfM 2016). pages 9-16, New York, NY, USA

> Atlı, H. S., Bozkurt, B., Şentürk, S. (2015). A Method for Tonic Frequency Identification of Turkish Makam Music Recordings. In Proceedings of 5th International Workshop on Folk Music Analysis (FMA 2015), pages 119–122, Paris, France.

> Şentürk, S., Gulati, S., and Serra, X. (2013). Score informed tonic identification for makam music of Turkey. In Proceedings of 14th International Society for Music Information Retrieval Conference (ISMIR 2013), pages 175–180, Curitiba, Brazil.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
