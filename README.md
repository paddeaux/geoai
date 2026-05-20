# Integrating LLM-based workflows into GIS classroom learning activities

This repository contains some of the work and outputs relating to the above named GeoAI submission 3192. This abstract serves as a brief evaluation of the use of LLM frameworks in GIS classroom settings. This work evalutes a number of state-of-the-art LLMs with regards to their abilities as synthetic spatial data generators, comparing their performance to that of RADIAN (Gorry, Mooney., [2025](https://doi.org/10.1080/15230406.2024.2377981)), an open-source software tool for spatial data generation. 

## Experimental Scenarios & Prompts
In order to test and evaluate the performance of LLMs for synthetic spatial data generation, three distinct scenarios were devised, for which appropriate prompts where then written as input for each model. For all models and for each task, the scenario was tested in the regions of *London, UK*, and *Berlin, Germany*. The exact prompts and parameters for each task can be found in `/prompts`. 

### Task A (Synthetic Data)
Generate a *synthetic dataset*, consisting of 500 point objects representing restaurants, within both given polygon boundaries.

### Task B (Open Synthetic Data)
Using *publicly available data, such as Open Street Map*, generate a synthetic dataset, consisting of 500 point objects representing restaurant, within the given boundaries.

### Task C (Random Data)
Generate a dataset of 500 point objects, which are *randomly distributed* within the given boundaries.

## Models Evaluated

There were *six* distinct LLMs evaluated in this work, along with the aformentioned Python-based software **RADIAN**

* gpt-4.1
* claude-4.7-opus
* gemini-3.1-pro
* gpt-oss-120b
* gpt-oss-20b
* llama-3.1-8b-instruct

## Summary of Results

This work evaluates these models by using Cross-L and Cross-K functions to compare spatial characteristics and observe any apparent similarities in the underlying distribution of model outputs and real-world data (in the form of Open Street Map), as well as procedurally generated data from RADIAN. Of the models tested, only `claude-4.7-opus` was capable of achieving reasonable results for Task A and B, with the other LLMs being prone to isolated coordinate memorization and a failure to replicate natural geographical distributions.

The full discussion and analyis is available at *link pending*[blank.com]

