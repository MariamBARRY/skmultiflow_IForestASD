# skmultiflow_IForestASD
 IForestASD for Anomaly Detection in Scikit-MultiFLow.

This code is related to the publication IForestASD for Anomaly Detection in Scikit-MultiFLow.
Code source and notebooks provided have been used to compute results mentionned in the experimental evaluation.

## Algorithm implemented (IForestASD by Ding & Fei, 2013)
This code provide an open source implementation of Isolation Forest ASD algoritm by Ding & Fei [1] based on Isolation Forest [2].

This implementation is built on top of scikit-multiflow [3], an open source machine learning framework for data streams https://scikit-multiflow.github.io/. It provide a variety of streaming methods : Incremental & Adaptive learning, from both supervised, unsupervised algorithms to multi-outpout and data stream generators.

<img src= "https://github.com/MariamBARRY/skmultiflow_IForestASD/blob/master/figures/algorithm_IForest_ASD_Ding_Fei_2013.png">


## Results on Real Datasets 

[Comparison of IForest ASD vs Half Space Trees performance (output from Scikit-multiflow prequential evaluator metrics)]

<img src= "https://github.com/MariamBARRY/skmultiflow_IForestASD/blob/master/figures/Results_Metrics_IForestASD_HSTrees.PNG">

[Running Time & Model size comparison on SHUTTLE & Forest Cover Datasets]

<img src="https://github.com/MariamBARRY/skmultiflow_IForestASD/blob/master/figures/Results_Experiments_Paper.PNG">

## References

An Implementation of Unsupervised Anomaly Detection with Isolation Forest in Scikit-MultiFlow with Sliding Windows \& drift detection


## References :

 -[1] [Algorithm Implemented] An Anomaly Detection Approach Based on Isolation Forest  for Streaming Data using Sliding Window (Ding \& Fei, 2013) https://www.sciencedirect.com/science/article/pii/S1474667016314999

 - [2] Original implementation of Isolation Forest (Isolation-based Anomaly Detection  - Liu, Ting \& Zhou, 2011 - https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/tkdd11.pdf
 available on  https://github.com/Divya-Bhargavi/isolation-forest 
 
  - [3] Scikit MultiFlow https://scikit-multiflow.github.io/ HalfSpace Trees Implementation is available here  - “Fast anomaly detection for streaming data,” in IJCAI Proceedings - S.C.Tan, K.M.Ting, and T.F.Liu https://github.com/scikit-multiflow/scikit-multiflow/blob/a7e316d/src/skmultiflow/anomaly_detection/half_space_trees.py#L11

