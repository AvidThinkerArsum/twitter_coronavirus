# Coronavirus Twitter Analysis Project

## Overview
Every day, approximately 500 million tweets are posted worldwide. Among these tweets, about 2% contain geographic location information, known as geotagging, indicating where the tweets originated. This Twitter dataset encompassed all geotagged tweets sent throughout the year 2020. In total, the dataset comprises around 1.1 billion tweets.

This project aimed to analyze geotagged tweets from 2020 to track the spread and public discourse around the coronavirus on social media. Utilizing a large-scale dataset of approximately 1.1 billion tweets, the project leveraged the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) paradigm to process and analyze the data in parallel, focusing on multilingual text processing.

## Objectives
- **Large-Scale Data Handling**: Demonstrated ability to work with a dataset comprising around 1.1 billion tweets, focusing on the 2% that were geotagged.
- **Multilingual Text Analysis**: Analyzed tweets in multiple languages to understand global discourse around the coronavirus.
- **Parallel Processing**: Implemented MapReduce for efficient, parallel data processing.

## Tools and Technologies
- **Language**: Python 3
- **Libraries**: `json` for parsing tweets, `matplotlib` for generating plots, `argparse` for command-line interface creation.
- **Techniques**: MapReduce for parallel processing, text analysis for hashtag frequency tracking.

## Process
1. **Mapping**: Processed daily tweet data to summarize hashtag frequencies by language and country, generating intermediate `.lang` and `.country` files.

2. **Reducing**: Merged daily summaries into comprehensive datasets for languages and countries.
```
$ ./src/reduce.py --input_paths outputs_1/geoTwitter*.lang --output_path=reduced.lang 
```
```
$ ./src/reduce.py --input_paths outputs_1/geoTwitter*.country --output_path=reduced.country
```
3. **Visualization**: Generated visual representations of the data to analyze the spread and impact of coronavirus-related discourse on Twitter.

## Results
The project resulted in four key visualizations, each offering insights into how different hashtags related to the coronavirus were discussed on Twitter throughout 2020.

### Language Distribution of Hashtags

```
$ ./src/visualize.py --input_path=reduced.lang --key='#coronavirus'
```

- Frequency of `#coronavirus` mentions in 2020 (Top 10 Languages).

<img src=reduced_coronavirus_language_distribution.png width=100% />

```
$ ./src/visualize.py --input_path=reduced.lang --key='#코로나바이러스'
```

- Frequency of `#코로나바이러스`  (the Korean equivalent of #coronavirus) mentions in 2020 (Top 10 Languages).

<img src=reduced_코로나바이러스_language_distribution.png width=100% />


### Country Distribution of Hashtags

```
$ ./src/visualize.py --input_path=reduced.country --key='#coronavirus'
```

- Frequency of `#coronavirus` mentions in 2020 (Top 10 Countries).

<img src=reduced_coronavirus_country_distribution.png width=100% />

```
$ ./src/visualize.py --input_path=reduced.country --key='#코로나바이러스'
```
- Frequency of `#코로나바이러스`  (the Korean equivalent of #coronavirus) mentions in 2020 (Top 10 Countries).
    
<img src=reduced_코로나바이러스_country_distribution.png width=100% />

# Time Series Analysis for Volume of Tweets

The objective was to enable the tracking of the daily usage of any given number of hashtags throughout the year 2020. To fulfill this objective, a Python script was crafted to meticulously parse the entire dataset and construct a dictionary. This dictionary associates each day of the year with the tweet volumes for each specified hashtag. Utilizing the bash scripts provided below, it becomes possible to systematically visualize the tweet volumes, thereby facilitating the examination of usage trends for a diverse array of hashtags over the course of the year.

The following bash command runs `alternative_reduce.py` for all hashtags: 

```
python3 alternative_reduce.py '#doctor' '#nurse' '#hospital' '#sneeze' '#cough' '#sick' '#flu' '#virus' '#corona' '#coronavirus' '#covid-19' '#covid19' '#covid-2019' '#covid2019' '#冠状病毒' '#コロナウイルス' '#코로나바이러스'
```
<img src=hashtag_trends_doctor_nurse_hospital_sneeze_cough_sick_flu_virus_.png width=100% />

Finding: '#corona', '#coronavirus', and '#covid19' are the most popular hashtags

<img src=hashtag_trends_corona_coronavirus_covid19.png width=100% />

If a given hashtag is not in the list of original mapped hashtags then the result will be a null line.

<img src=hashtag_trends_coronavirus_corona_arsum.png width=100% />

## Conclusion
The project successfully utilized large-scale data processing and visualization techniques to analyze the discourse around the coronavirus on Twitter. The insights gained underscore the potential of social media analytics in understanding public sentiment and spreading awareness during global crises.

