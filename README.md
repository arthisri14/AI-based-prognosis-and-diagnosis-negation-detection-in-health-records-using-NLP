# AI-Based Prognosis and Diagnosis Negation Detection in Health Records using NLP

## Project Description

This project aims to develop an AI-based system for prognosis and diagnosis negation detection in health records using Natural Language Processing (NLP). The workflow includes building a Recurrent Neural Network (RNN) model, applying the negex algorithm using negspacy, and visualizing the results through a Power BI dashboard. The entire system is integrated into a web application using Flask.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Datasets](#datasets)
- [Model and Algorithms](#model-and-algorithms)
- [Dashboard Analytics](#dashboard-analytics)
- [Web Application](#web-application)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Healthcare records often contain critical information about a patient's diagnosis and prognosis. Detecting negations in these records is vital for accurate medical analysis and decision-making. This project leverages NLP techniques to preprocess radiology reports, detect negations using an RNN model combined with the negex algorithm, and visualize the findings through a user-friendly web application and Power BI dashboards.

## Features

- Preprocessing of radiology reports and text extraction from PDF documents.
- Negation detection using an RNN model and negex algorithm with negspacy.
- Dashboard analytics implemented using Power BI.
- Integration of all components into a Flask-based web application.
- Open-source datasets for training and testing.

## Installation

1. Clone the repository:
   <br/>
   ```git clone https://github.com/arthisri14/AI-based-prognosis-and-diagnosis-negation-detection-in-health-records-using-NLP.git```
   ```cd AI-based-prognosis-and-diagnosis-negation-detection-in-health-records-using-NLP```
   <br/>

2. Create a virtual environment and activate it:
   <br/>
   ```python -m venv venv```
   <br/>
   ```source venv/bin/activate```
   <br/>
   ```On Windows use `venv\Scripts\activate` ```

4. Install the required packages:
   <br/>
   ```pip install -r requirements.txt```

## Usage

1. Run the Flask application:
   <br/>
   ```python run.py```
2. Access the web application:
   <br/>
   ```Open your browser and go to http://127.0.0.1:5000
3. Upload radiology reports and view the negation detection results.

## Datasets

The radiology reports dataset is obtained from open-source dataset directories available on the internet. 
The preprocessing includes extracting text from PDF documents using NLP techniques.

## Models and Algorithms

Recurrent Neural Network (RNN): Used for processing and analyzing sequential data from the radiology reports.<br/>
Negex Algorithm: Implemented using negspacy to detect negations in the medical text.

## Dashboard Analytics

The Power BI dashboard provides insightful visualizations of the negation detection results, offering an overview of the data and helping in better decision-making.

## Web Application

The web application, built using Flask, integrates all components and provides an interactive interface for users to upload reports and view results.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

Special thanks to the open-source community for providing the datasets and tools necessary for this project.
