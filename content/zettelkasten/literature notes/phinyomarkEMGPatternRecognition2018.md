---
tags:
- "Type/Note"
date:
- 1533106800000
---

**Imported: 2024-12-31**

> “however, the analysis of surface EMG signal is more challenginggiven that it is stochastic in nature” Yellow Highlight [Page ](zotero://open-pdf/library/items/QMMDN73J?page=1&annotation=R4WBVAUQ)

EMG is stochastic in nature, so it is harder to analyze without including confounding variables

> “zero crossings (ZC) andslope sign changes (SSC)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/QMMDN73J?page=3&annotation=MQFMNRLF)

commonly used EMG features

> “theoptimum threshold is highly subject- and dataset-dependent, i.e., each subject had a unique optimumthreshold value, and, even within the same subject, the optimum threshold could change over time” Yellow Highlight [Page 3](zotero://open-pdf/library/items/QMMDN73J?page=3&annotation=L9FQBQ49)

need for adaptive thresholds

> “commonly used Hudgins’ time domain features (ZC, SSC, mean absolute value(MAV) and waveform length (WL) [28]) and several additional features (autoregressive coefficients, AR; cepstral; coefficients, CC; Willison amplitude, WAMP; and sample entropy, SampEn)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/QMMDN73J?page=3&annotation=977YTYUT)

more prospective EMG features

> “identified a novel set of features that are moreaccurate and robust for emerging low-sampling rate EMG systems” Yellow Highlight [Page 3](zotero://open-pdf/library/items/QMMDN73J?page=3&annotation=A3JYPEYA)

different features to use on low-sampling rate EMG systems

> “A major limitation of themultiple-dataset investigation approach is the fact that EMG data from different data sets cannot be combined into one larger set due to experimental and equipment differences. Without largeEMG datasets being collected using a single standardized protocol, it is difficult to investigate the generality of the findings across gender, age, characteristics of the amputation, etc.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/QMMDN73J?page=4&annotation=8PV98PJY)

No standardized EMG protocol

> “Two methods of analyzing these kinds of EMG signals include the HD-sEMG map(a topographical image) and the sEMG image (an instantaneous image).” Yellow Highlight [Page 5](zotero://open-pdf/library/items/QMMDN73J?page=5&annotation=D959ZI3B)

Topographical vs. instantaneous imaging for HD-sEMG data. Topographical is less affected by confounding variables

> “Features extracted from HD-sEMG mapscan be based on intensity information (any signal magnitude and power feature [18,22]) and spatialinformation (e.g., the mean shift [42] or the coordinates of the centre of gravity and maximum values[44])” Yellow Highlight [Page 5](zotero://open-pdf/library/items/QMMDN73J?page=5&annotation=8X8EZSJB)

Intensity and spatial features

> “Without applying feature extraction methods, instantaneous sEMG images havebeen treated as an image classification problem and thus classified using deep learning approaches.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/QMMDN73J?page=6&annotation=5AU9BGSZ)

sEMG images are suited to image classification and deep learning approaches. Voting over 10s to 100s of frames for classification

> “In fact, several studies have shown that there is little need to use allEMG channels (over 100 electrodes), and instead, a properly positioned smaller set of electrodes (e.g., 9 [44] and 20–80 [45]) can provide comparable results.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/QMMDN73J?page=6&annotation=KJ6CWXVF)

HD EMG is not necessarily more performant than a smaller number of well positioned electrodes

> “big volume” Yellow Highlight [Page 7](zotero://open-pdf/library/items/QMMDN73J?page=7&annotation=KM3UN3PR)

large datasets

> “big variety” Yellow Highlight [Page 7](zotero://open-pdf/library/items/QMMDN73J?page=7&annotation=XL434Y8W)

diversity of data and characteristics within and between datasets

> “Big veracity” Yellow Highlight [Page 8](zotero://open-pdf/library/items/QMMDN73J?page=8&annotation=V38CQGS2)

data problems

> “Big velocity” Yellow Highlight [Page 8](zotero://open-pdf/library/items/QMMDN73J?page=8&annotation=9HBK9HQJ)

data generation and analysis rates (i.e. real time or after?)

> “Novel methodscapable of analyzing such data could be developed either by modifying traditional methods to run in parallel computing environments or by proposing new methods that natively leverage parallelcomputing. These methods will become very important in turning any collected big EMG dataset into a meaningful resource.” Yellow Highlight [Page 14](zotero://open-pdf/library/items/QMMDN73J?page=14&annotation=P93UYCJ9)

Leveraging parallel computing for big EMG data

> “EMG pattern recognition systems typically consist of several inter-connected components: data pre-processing, feature extraction, dimensionality reduction, and classification [1,2]” Yellow Highlight [Page 14](zotero://open-pdf/library/items/QMMDN73J?page=14&annotation=5FKS64XA)

Standard steps for EMG pattern recognition systems

> “The stochasticand non-stationary characteristics of the EMG signal make the instantaneous value unsuitable for conventional machine learning algorithms [86]. Feature extraction, which transforms short time windows of the raw EMG signal to generate additional information and improve information density,is thus required before a classification output can be computed.” Yellow Highlight [Page 14](zotero://open-pdf/library/items/QMMDN73J?page=14&annotation=PMIUCQ4Y)

Transformations are required for ML techniques to account for randomness

> “During the past several decades,numerous different EMG feature extraction methods based on time domain, frequency domain,and time–frequency domain information have been proposed and explored [7,8,18–20,22,26,28–30].  Interesting EMG feature extraction methods include a set of ZC, SSC, MAV, and WL (the most commonly used features [28]); AR and CC (the robust features for EMG electrode location shift, variation in muscle contraction effort, and muscle fatigue [8]); WAMP (a robust feature against noise [64,65]); SampEn (a robust feature against between-day variability [7]); and L-scale (an optimalfeature for wearable EMG devices [26]), to name a few” Yellow Highlight [Page 14](zotero://open-pdf/library/items/QMMDN73J?page=14&annotation=I6JZJ5V6)

Prominent EMG features

> “More often than not, however, classical dimensionality reduction techniques cannot beapplied to big data, and it is therefore necessary to re-design and change the way the traditional methods are computed.” Yellow Highlight [Page 14](zotero://open-pdf/library/items/QMMDN73J?page=14&annotation=SUCQ5EN5)

Problem with traditional dimensionality reduction techniques and big data

> “For feature selection, somepotential and well-known population-based metaheuristic methods, such as genetic algorithm (GA),particle swarm optimization (PSO), and ant colony optimization (ACO), have been found to be effective in selecting an optimal EMG feature set (e.g., [67–69]).” Yellow Highlight [Page 14](zotero://open-pdf/library/items/QMMDN73J?page=14&annotation=X6VYWZU6)

Optimized feature selection methods

> “Similarly, novel approaches have been proposed to run standard feature projection (e.g., principal component analysis (PCA)) in parallel or on GPUs for big data dimensionality reduction [89,90].” Yellow Highlight [Page 14](zotero://open-pdf/library/items/QMMDN73J?page=14&annotation=ZPALHSNI)

Standard feature projection techniques can be run in parallel or on GPUs using novel techniques

> “These properties make Mapper a very good tool for the analysis of big data asthis approach can be naturally performed in a framework of big data analysis such as the Google’s MapReduce paradigm.” Yellow Highlight [Page 15](zotero://open-pdf/library/items/QMMDN73J?page=15&annotation=HUJDU323)

Mapper and Google MapReduce algorithm for topologically simplifying big data problems

> “For EMG pattern recognition, this approach has been successfully used to create charts of EMG features spaces that are robust and generalize well across three different EMG data sets containing 58 individual subjects and 27,360 separate contractions [22]. These charts highlight four functionalgroups of state-of-the-art EMG features that describe meaningful non-redundant information allowing for a principled and interpretable choice of EMG features for further classification.” Yellow Highlight [Page 15](zotero://open-pdf/library/items/QMMDN73J?page=15&annotation=SKV6T4YZ)

Mapping can create non redundant and generalizable features across datasets

> “In the problem of EMG pattern recognition, commonly used classification algorithms include SVM [26,94], linear discriminant analysis (LDA) [7,8], k-nearest neighbors (KNN) [20,95], multi-layerperceptron neural network (MLP) [28,66], and random forests (RF) [7,96], to name a few.” Yellow Highlight [Page 15](zotero://open-pdf/library/items/QMMDN73J?page=15&annotation=N4GHFGK5)

Commonly used classification algorithms for EMG pattern recognition

> “In general, though, deep learning models can be roughly grouped into three main categories:unsupervised pre-trained networks, convolutional neural networks, and recurrent neural networks.  Although their application to surface EMG is relatively new, these three categories of models have already been used to analyze the EMG signal. Table 5 details each of the previous EMG research works utilizing deep learning methods.” Yellow Highlight [Page 16](zotero://open-pdf/library/items/QMMDN73J?page=16&annotation=IAL2Y22Y)

Applications of various DL methods to EMG

> “One of the most widely usedpre-extracted features for deep learning is the spectrogram. Côté-Allard et al. [111,112], for example,used CNNs with spectrograms as the input. Their results showed that CNN is not only accurate enough to recognize complex motions, but is also robust to many confounding factors, such as shortterm muscle fatigue, small displacement of electrodes, inter-subject variability, and long term use, without the need for recalibration.” Yellow Highlight [Page 17](zotero://open-pdf/library/items/QMMDN73J?page=17&annotation=9EEBVFDR)

Spectrogram is a useful feature for CNNs

> “In contrast to other deep learning models, RNNs take time series information into account,i.e., rather than completely feed-forward connections, RNN might have connections that feed backinto prior layers. This feedback path allows RNNs to store the information from previous inputs andmodel problems in time.” Yellow Highlight [Page 17](zotero://open-pdf/library/items/QMMDN73J?page=17&annotation=VGY8TDY6)

RNNs are particularly suited to time series data such as EMG

> “No comparison between different types of pre-extracted EMG features involvingwindow-based time domain features, time–frequency representation features, and EMG images,has been made yet.” Yellow Highlight [Page 18](zotero://open-pdf/library/items/QMMDN73J?page=18&annotation=UQC4KWJ7)

Further research needed to compare types of pre-extracted features

> “Another key challenge for the clinical use of deep learning methods for myoelectric prostheticcontrol is the use of unsupervised domain adaptation or transfer learning methods [117] to reduce theeffect of confounding factors that affect the characteristics of surface EMG signals. Inter-subject andinter-session variability are two main factors that have been studied so far (Table 5). These techniqueshave been used to significantly reduce the amount of training data required for a new subject as wellas to alleviate the need for periodic re-calibration” Yellow Highlight [Page 18](zotero://open-pdf/library/items/QMMDN73J?page=18&annotation=3D2FULYF)

Unsupervised domain adaptation and transfer learning provide solutions to variability between patients and sessions in the clinical setting

> “Nevertheless, there are other real-life conditions thatmust be addressed, including but not limited to, electrode location shift, muscle fatigue, variations in muscle contraction intensit as well as variations in limb position and forearm orientation” Yellow Highlight [Page 18](zotero://open-pdf/library/items/QMMDN73J?page=18&annotation=MWHLULD2)

Additional limitations