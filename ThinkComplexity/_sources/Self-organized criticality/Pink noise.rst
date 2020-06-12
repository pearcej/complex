Pink noise
----------
The title of the original paper that presented the sand pile model is “Self-Organized Criticality: An Explanation of 1/f Noise”. You can read it at http://thinkcomplex.com/bak.

As the subtitle suggests, Bak, Tang and Wiesenfeld were trying to explain why many natural and engineered systems exhibit 1/f noise, which is also known as “flicker noise” and “pink noise”.


To understand pink noise, we have to take a detour to understand signals, power spectrums, and noise.

Signal: A **signal** is any quantity that varies in time. One example is sound, which is variation in air density. In the sand pile model, the signals we’ll consider are avalanche durations and sizes as they vary over time.

Power spectrum: Any signal can be decomposed into a set of frequency components with different levels of **power**, which is related to amplitude or volume. The **power spectrum** of a signal is a function that shows the power of each frequency component.

Noise: In common use, **noise** is usually an unwanted sound, but in the context of signal processing, it is a signal that contains many frequency components.

There are many kinds of noise. For example, “white noise” is a signal that has components with equal power over a wide range of frequencies.

Other kinds of noise have different relationships between frequency and power. In “red noise”, the power at frequency f is 1/f2, which we can write like this:

P(f) = 1/f2 
We can generalize this equation by replacing the exponent 2 with a parameter β:

P(f) = 1/fβ
When β=0, this equation describes white noise; when β=2 it describes red noise. When the parameter is near 1, the result is called 1/f noise. More generally, noise with any value between 0 and 2 is called “pink”, because it’s between white and red.

We can use this relationship to derive a test for pink noise. Taking the log of both sides yields

logP(f) = −β logf 
So if we plot P(f) versus f on a log-log scale, we expect a straight line with slope −β.

What does this have to do with the sand pile model? Suppose that every time a cell topples, it makes a sound. If we record a sand pile model while its running, what would it sound like? In the next section, we’ll simulate the sound of the sand pile model and see if it is pink noise.

