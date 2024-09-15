# WebMetricsEvaluation

A comprehensive project to evaluate and analyze web metrics for websites using the Webby Awards dataset. The project automates the extraction of website metrics, performs descriptive statistical analysis, and evaluates website performance using several metrics.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Step 1: Web Scraping Webby Awarded Sites](#step-1-web-scraping-webby-awarded-sites)
  - [Step 2: Extracting and Analyzing Website Metrics](#step-2-extracting-and-analyzing-website-metrics)
  - [Step 3: Statistical Analysis](#step-3-statistical-analysis)
  - [Step 4: Website Performance Evaluation](#step-4-website-performance-evaluation)
  - [Step 5: Performance Statistics Calculation](#step-5-performance-statistics-calculation)
  - [Step 6: Copying and Randomizing Performance Data](#step-6-copying-and-randomizing-performance-data)
- [Output](#output)
- [License](#license)

## Project Overview

This project automates the process of scraping websites from the Webby Awards dataset and evaluating their performance based on various metrics such as the number of links, body text words, number of lists, page size, and graphics. It also calculates statistical metrics like mean, median, mode, and standard deviation for different website metrics and evaluates the website performance using metrics such as First Contentful Paint, Speed Index, and more.

## Requirements

This project requires the following Python libraries:
- `requests`
- `openpyxl`
- `beautifulsoup4`
- `numpy`
- `statistics`
- `selenium`

You will also need the Chrome WebDriver to use Selenium for performance evaluation.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Quinos2003/WebMetricsEvaluation.git
cd WebMetricsEvaluation
```

2. Install the required Python libraries:
```bash
pip install -r requirements.txt
```

3. Download and set up the Chrome WebDriver from [here](https://sites.google.com/chromium.org/driver).

4. Place the WebDriver executable in the appropriate path, and update the script if needed.

## Usage

### Step 1: Web Scraping Webby Awarded Sites
Run `webby_scapy.py` to scrape websites from the Webby Awards dataset for the year 2024. The scraped website URLs are saved in an Excel file (`Webby_2024_awards.xlsx`).

```bash
python webby_scapy.py
```

### Step 2: Extracting and Analyzing Website Metrics
Run `metrics.py` to extract key website metrics such as the number of links, body text words, lists, tables, and more. The metrics are saved in `metric_data_2024.xlsx`.

```bash
python metrics.py
```

### Step 3: Statistical Analysis
Run `stats.py` to calculate descriptive statistics (mean, median, mode, etc.) for the extracted website metrics. The results are saved in `Descriptive_statistics_2024.xlsx`.

```bash
python stats.py
```

### Step 4: Website Performance Evaluation
Run the performance evaluation script (`performance_metrics.py`) to analyze various performance metrics like First Contentful Paint, Speed Index, Largest Contentful Paint, and more. The performance data is saved in `Performance.xlsx`.

```bash
python performance_metrics.py
```

### Step 5: Performance Statistics Calculation
Run `performance_stats.py` to calculate statistical measures like the mean of various performance metrics. The results are saved in `Performance.xlsx`.

```bash
python performance_stats.py
```

### Step 6: Copying and Randomizing Performance Data
Run `copier.py` to copy and randomize performance data from multiple files. The output files are saved with names `site_<num>.xlsx`.

```bash
python copier.py
```

### Output
- **Webby_2024_awards.xlsx**: List of Webby-awarded websites for 2024.
- **metric_data_2024.xlsx**: Metrics extracted from the websites.
- **Descriptive_statistics_2024.xlsx**: Descriptive statistical analysis of the website metrics.
- **Performance.xlsx**: Website performance metrics based on Speed Index, First Contentful Paint, and others.

### License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
