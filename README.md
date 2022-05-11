# Magno-Parvo CNN: Emulating Magnocellular and Parvocellular Parallel Stream Processing in Deep Neural Networks


![alt text](https://github.com/nelsonalbertohj/Magno-Parvo-CNN/blob/main/Model%20Diagram.png?raw=true)

# Introduction
We inspire our architecture on the magnocellular and parvocellular streams in the visual cortex in order to make it more robust to blurs, occlusions, and other out-of-distribution test images. The magnocellular stream is color-blind and carries coarse-grained information about slight brightness changes, while the parvocellular stream carries more fine-grained details that are informative about local color differences (\cite{bear2007central}). These parallel processes interact through complex feed-forward, lateral, and top-down connectivity in the brain (\cite{medathati2016bio}), but we will simplify our approach and consider the feed-forward aspects of this neural circuit. We will simulate the magnocellular and parvocellular streams by using two parallel CNNs, the outputs of which are merged through an averaging layer and passed on to a fully-connected network that produces a classification of images. Architectures similar to our implementation have been used to identify gestures by \cite{khurana2019delving}. We will assess the performance of people on a subset of the testing set that our algorithm is tested on as a benchmark for optimal results. We hypothesize that our Dual-stream CNN will be more robust to occlusions and blurriness that are partly out-of-distribution compared to traditional CNNs. We also expect our algorithm to achieve closer to human performance.

# Research Report
The following research report was submitted as part of the final project in 9.60 Machine Motivated Human Vision.
[Mango-Parvo CNN Research Report](https://github.com/nelsonalbertohj/Magno-Parvo-CNN/blob/main/Machine_Motivated_Vison_Final_Report.pdf).

Please, if using the algorithms developed in this repository, please cite our work as:

```
@inproceedings
{960magnoparvo,
    author = {Hidalgo, Nelson and Umoren, Aniekan and Aidan Cook},
    year = {2022},
    title = {Emulating Magnocellular and Parvocellular Parallel Stream Processing in Deep Neural Networks},
    booktitle = {Preprint}
}
```

# Environment Configuration
The following dependencies versions were used in this project:

```
tensorflow                         2.8.0
Python                             3.9.12
```