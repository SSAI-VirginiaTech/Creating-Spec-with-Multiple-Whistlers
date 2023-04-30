# Data Augmentation

We agumented the provided data files to generate the following whistler patterns: multiple whistlers, time-shifted whistlers, half-whistlers, and overlapping whistlers. This was made easy since when generating the spectrogram of the whistler data from the S3 bucket, each whistler showed up in the same time interval. The following code was generated assuming that the original data had the whistler in the same spot throughout.

## Types of Augmented Whistlers

### Time-Shifted Whistler Spectrogram

This code generates a spectrogram with a whistler shifted to show up in another part of the spectrorgam. It functions by copying the section of the spectrogram with the whistler and then pasting it in another part of the spectrogram. Then, the original position of the whistler is filled with background noise. It can be found within shift_whistler.py

### Half-Whistler Spectrogram

This code generates a spectrogram with a half-whistler in the very front or the back of the spectrogram. It functions by copying the section of the spectrogram with the whistler, halving it, and moving the data to the very front or back of the spectrogram. The original section of the whistler is replaced with background noise. This can be found in half_whistler.py

### Multiple Whistler Spectrogram

This code generates a spectrogram with multiple whistlers. It functions by copying the section of the spectrogram with the whistler and then pasting it in another part of the spectrogram. It can be found within add_whistler.py

### Overlapping Whistler Spectrogram

This code generates a spectrogram with overlapping whistlers. It uses the add_whistler() method used in the previous agumentation, but adds the whistler atop the original whistler. This code can be found within overlap_whistler.py