Name: Ejara
Class: CS 432 Web Science
Assignment: HW2 – Ranking Webpages
Date: 28 september 2025

# Introduction
This assignment ranks webpages for a query. I collect HTML for 500 URIs from HW1, remove boilerplate, and prepare plain text for ranking.

  Q1.  How many of your 500 URIs produced useful text? If that number was less than 500, did that surprise you?
- Processed text files: 500  
- Non-empty processed files: 424  
- Percent non-empty: 84.8%

  it did not really. Several pages yielded little or no extractable text because they were JS-rendered, paywalled/consent-gated, mostly navigation/templates, or returned errors/redirects. Boilerplate removal also discards pages without a dense content block, so fewer than 500 non-empty files is expected.

