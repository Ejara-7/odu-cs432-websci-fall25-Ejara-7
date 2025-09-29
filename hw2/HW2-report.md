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

# Q2  Rank with TF-IDF

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
The top 10 documents ranked by TF-IDF are shown in the table below:
<img width="697" height="280" alt="image" src="https://github.com/user-attachments/assets/b6d46450-468d-4ed1-a6b5-49256d83dfe2" />

# Q3
### Q3: PageRank Results

| PageRank | URI |
|---------:|-----|
| 0.80 | https://oducsreu.github.io/ |
| 0.80 | https://www.ssrc.org/ |
| 0.70 | https://www.odu.edu/ |
| 0.70 | https://weiglemc.github.io/ |
| 0.60 | https://www.cs.odu.edu/ |
| 0.40 | https://vmasc.org/ |
| 0.40 | https://www.catalyzex.com/ |
| 0.20 | https://ws-dl.blogspot.com/ |
| 0.00 | https://www.cornell.edu/ |
| 0.00 | https://www.txyz.ai/ |

Q2 (TF-IDF): Ranked URIs based on how often the word “research” appeared in each document compared to the entire corpus. This measures local relevance to the query. For example, ODU’s research compliance page ranked highest because it had the densest and most relevant mentions of “research.”

Q3 (PageRank): Ranked URIs based on the importance of their domains across the web. Here, GitHub pages (oducsreu.github.io, weiglemc.github.io), ODU’s main site, and SSRC scored higher because their domains are considered more authoritative or widely linked, even if the specific page wasn’t the most textually relevant for “research.”

Key difference:

TF-IDF prioritizes relevance within your dataset.

PageRank prioritizes overall authority on the web.

That’s why some sites with high TF-IDF scores (like catalyzex.com) got pushed lower in PageRank, while more “trusted” domains (like odu.edu or ssrc.org) rose up.

# Q4
The Kendall Tau-b correlation between the TF-IDF and PageRank results was 0.289, with a p-value of 0.291. This shows a weak positive correlation, but not statistically significant. In other words, while some overlap exists between query relevance (TF-IDF) and domain authority (PageRank), the two ranking methods measure different properties of the documents.

# Q5 
