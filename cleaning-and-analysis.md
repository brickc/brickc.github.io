---
layout: default
title: "Cleaning & Analysis"
permalink: /cleaning-and-analysis
---

# Help within the UvA

- [Methodology shop](https://docs.google.com/spreadsheets/d/1S6siv3owG7nzqf5n5e6C8AldN8Z1Ds4b1BtCKWmWpgM/edit?fbclid=IwAR0EZkffWW_b5mnwXpdVv_x-C-0Wn7lxkNLo7fIC-DV8f0huq3igJoYk0D8#gid=0) (for students)

- [Writing centre](https://intt.uva.nl/language-training/writing-centre/writing-centre.html) (for students)

- [Stats shop](http://www.stats-store.socsci.uva.nl/) (for faculty)

# Data Cleaning

## Dataset
1.  Data privacy and ethics applications: [rms.uva.nl](https://rms.uva.nl)

2.  Acquire the data. Never modify the raw data: work with copies.

3.  Ideal: use scripts for cleaning and analysis (e.g., R code). Minimum expectations: write down cleaning steps in words in a list.

## Items

1.  Check scale: ratio, interval, ordinal, categorical

2.  Exclusions: 99, NA, etc.? Always look at range and *N* of output

# Analysis

Also see the [Thesis Quality](/thesis-quality) page for advanced suggestions.

1.  Check scale of items & composites and see handouts below on statistical tests.

2.  Best practices: make a time-stamped preregistration at the [Open Science Framework](https://osf.io), [As Predicted](https://aspredicted.org), etc. The key benefit is cleanly distinguishing between confirmatory, inferential tests (anything with a *p*-value) and exploratory tests where analytic decisions such as scoring and exclusions are made during analysis. Here’s a [longer handout](/s/UKRN_Primer_Preregistration.pdf) explaining why pre-registration is valuable and what it should contain. At a minimum, in the method include one line per hypothesis explaining how exactly it will be tested. Do you need a multiple comparisons correction?

3.  Graph histograms of all key variables (check test assumptions) and look at scatter plots and zero-order correlations. Anything unexpected? Do you need to document and justify additional exclusions or analytic changes?

4.  Compute composites.

    - Any items need reversing? Compute new variable (don't overwrite old). Copy value labels.

    - Make sure all items are on same scale before combining

    - Make rule & document in methods how many can be missing before the composite should be missing (half?)

    - Compute with mean (equivalent to sum). Cannot be done with ordinal variables, which would require a median instead.

    - Should it be a composite at all? There's not a single right answer. It depends on how you conceptualize the overall category. Is it a latent variable which is causing the different indicators? (Like, for example, you might think about a person having high intelligence, and that feature driving high performance in different domains such as math and reading.) Or is some unitary variable not causing the indicators and it is not a latent variable, but instead a functional collection of items that have mostly separate causes? Now, it's still possible to combine disparate items into a useful composite, like with BMI (body mass index from height and weight), but scholars disagree about how appropriate that is. It depends on the research question. The shallowest approach is to combine them and check Cronbach's alpha. (This is sufficient, but not deep.) EFA/PCA is also possible to test how similar the behaviors are. Zooming out for a moment, the point isn't to make any particular decision about these things, but to keep this chain explicit and coherent:

      Using a psychological construct

      intuition --\> theory --\> definition --\> operationalization --\> measurement --\> analysis --\> interpretation

6.  Between-subjects moderation/interaction? The design is probably under-powered. See [this blog](https://approachingblog.wordpress.com/2018/01/24/powering-your-interaction-2/).

7.  Do you have categorical predictors with more than two levels? You will need simple or dummy coding to do linear analyses: [UCLA guide to coding systems for categorical variables (R)](https://stats.oarc.ucla.edu/r/library/r-library-contrast-coding-systems-for-categorical-variables/)

8.  Metadata: If using the [open datasets](https://docs.google.com/spreadsheets/d/1ejOJTNTL5ApCuGTUciV0REEEAqvhI2Rd2FCoj7afops/edit#gid=0) resource, please help the community by going back and improving the detail in the sheet.

9.  Logistic regression: [UCLA logistic regression guide (R)](https://stats.oarc.ucla.edu/r/dae/logit-regression/)

    - interpreting effect sizes and converting between linear and logistic: [scientificallysound.org/2017/07/27/cohens-d-how-interpretation](https://scientificallysound.org/2017/07/27/cohens-d-how-interpretation/); [rpsychologist.com/d3/cohend](https://rpsychologist.com/d3/cohend/); [katherinemwood.shinyapps.io/effect_size/](https://katherinemwood.shinyapps.io/effect_size/); [psychometrica.de/effect_size.html](https://www.psychometrica.de/effect_size.html) (#14); [ncbi.nlm.nih.gov/pubmed/11113947](https://www.ncbi.nlm.nih.gov/pubmed/11113947)

10. Include a power analysis. Here is a [slide deck tutorial on power](https://www.dropbox.com/s/m52dgdgqssgzsum/power%20tutorial.pptx?raw=1) by me, including code in R. Below is how a complete report looks (by [Guy Prochilo](https://twitter.com/GuyProchilo/status/1292780240977223681)). Play around with [an interactive tool](https://rpsychologist.com/d3/pdist/) for the distribution of p-values when comparing two groups.

## Mediation

Statistical mediation is widely misunderstood and misapplied even in journals. The most common error I see is taking correlational data, applying a mediation model, and assuming that what comes out has somehow improved in causal value. Even if you know it's not strong causal evidence, you might reduce the causal language—to apply this causal model and then describe it in correlational terms ("X was associated with Y"). But, this doesn't fix the deeper problem, which is that causality can't be removed from this model. I have tried and I cannot imagine a mediation model that isn't causal. Often, it's better just to interpret zero-order and partial correlations, whether in a table or network model. If you must use causal models without much causal evidence, at least mention or hopefully evaluate other possible models (e.g., the same model backwards).

Another problem I see a lot is describing mediations as partial or full. This is no longer coherent, because the interpretation of mediation has changed. Here's a good short paper explaining why. And how nice to have fully open reviewers with named reviewers, who happen in this case to be domain experts!

> Meule 2019 Contemporary understanding of mediation testing. Meta-Psychology, 3, <https://doi.org/10.15626/MP.2018.870>: “*...in contemporary thinking about mediation analysis, the indirect effect is either significant or not significant, regardless of the significance of the total effect. As there is, therefore, no need for an “effect to be mediated”, the concept of “partial mediation” is incompatible with the contemporary approach.”*

For more depth, I recommend:

> Bullock, J. G., Green, D. P., & Ha, S. E. (2010). Yes, but what’s the mechanism? (don’t expect an easy answer). Journal of Personality and Social Psychology, 98(4), 550–558. [https://doi.org/10.1037/a0018933](https://doi.org/10.1037/a0018933): Causal inference is much harder in mediation than people realize
>
> Spencer, S. J., Zanna, M. P., & Fong, G. T. (2005). Establishing a causal chain: Why experiments are often more effective than mediational analyses in examining psychological processes. Journal of Personality and Social Psychology, 89(6), 845–851. [https://doi.org/10.1037/0022-3514.89.6.845](https://doi.org/10.1037/0022-3514.89.6.845): If you haven't manipulated the mediator independently, without manipulating the outcome variable, it's very hard to get the causal story.

![](/assets/img/power.jpg)

## Select tests

Which inferential tests are appropriate for your design? See the summary image below and this [detailed flowchart](/s/Statistical-Analysis-Flowchart.pdf).

<div class="row">
<div class="col c3" markdown="1">



</div>
<div class="col c9" markdown="1">

![](/assets/img/which-test-should-we-use.png)

</div>
</div>

# Results writing

1.  If you compare two values using inferential statistics, say 3.11 and 3.24, and they are not significantly different—you cannot say that one is bigger than the other. Each estimate is just a central tendency of a distribution, and the *p*-value means that the we can’t distinguish whether values came from one distribution or the other. I suggest wording like this: “There was no difference between A, *M* (*SD*) = X.XX (.XX) and B, *M* (*SD*) = X.XX (.XX), *p* = .XX.” Subtly however, neither does this constitute confirmatory evidence that the values are the same (for this, use an equivalence test: [Lakens, 2018](https://journals.sagepub.com/doi/10.1177/2515245918770963)).

2.  **Statistical significance:** it's shallow to just note which effects were significant based on *p*-values, because significance tests are very sensitive to sample size, the .05 alpha threshold is arbitrary, and low *p*-values don't give a clear sense of how strong the effect is (this point is counterintuitive). Researchers are turning away from *p*-values and towards effect sizes and confidence intervals. Here's a good introduction: [Cumming 2014 The New Statistics—Why and How](https://journals.sagepub.com/doi/10.1177/0956797613504966). Most psychology manipulations are probably Cohen's *d* = .1 or weaker; the largest I've published was *d* = .4 (text vs. tables on comprehension); the height difference between men and women is *d* = 1.7. The strongest Discussion sections will demonstrate an understanding of the size of effects found in previous literature; using power or sensitivity analyses to estimate what kind of size effect your study was well-powered to find (usually this is much larger than we would wish); and reflecting on supporting or rejecting the hypotheses based on the above. Many times, the appropriate answer will be that we don't have enough evidence to support or reject a hypothesis.
