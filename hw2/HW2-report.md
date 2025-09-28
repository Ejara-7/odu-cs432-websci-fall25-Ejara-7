Name: Ejara
Class: CS 432 Web Science
Assignment: HW2 – Ranking Webpages
Date: 28 september 2025

# Introduction
This assignment ranks webpages for a query. I collect HTML for 500 URIs from HW1, remove boilerplate, and prepare plain text for ranking.

# Q1.  How many of your 500 URIs produced useful text? If that number was less than 500, did that surprise you?
- Processed text files: 500  
- Non-empty processed files: 424  
- Percent non-empty: 84.8%

  it did not really. Several pages yielded little or no extractable text because they were JS-rendered, paywalled/consent-gated, mostly navigation/templates, or returned errors/redirects. Boilerplate removal also discards pages without a dense content block, so fewer than 500 non-empty files is expected.

# Q2 

 I chose the query term “research.”
This word appeared frequently in my processed documents and was meaningful in the context of academic and informational content, but it was not a stop word (like “the” or “and”). It was also present in many English-language documents from different domains, which made it a strong candidate for TF-IDF analysis.

DF Value from Google

To estimate the document frequency (DF) of “research” on the web, I searched "research" in Google. The search returned about 2,530,000,000 results (≈2.53 billion).
For the total web size, I used the estimate of 40 billion pages (as given in the assignment instructions).

So:

DF_web = 2,530,000,000

Web size = 40,000,000,000

How TF, IDF, and TF-IDF Were Calculated

TF (Term Frequency): number of times “research” appears in a given processed document divided by the total number of words in that document.

IDF (Inverse Document Frequency): calculated with

IDF=log2​(2,530,000,000/40,000,000,000​) = 3.983


TF-IDF: product of TF and IDF.
