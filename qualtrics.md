---
layout: default
title: "Recruitment and Qualtrics"
permalink: /qualtrics
---

The [Qualtrics help pages](https://www.qualtrics.com/support/survey-platform/survey-module/survey-module-overview/) are actually quite good. Learn about basic topics like survey flow, randomization, branching, etc.

![Embedded data from Prolific](/assets/img/embedded.png)

Embedded data from Prolific

## Recruitment

***Free***

1.  If at the UvA: our participant pool of psychology undergrads can provide hundreds per term. Get ethics permission through rms.uva.nl, and then when approved go to lab.uva.nl, log in as a researcher, and go to the "recruitment" tab (upper left). Then search for your project under "search projects" and typing FMG-2090 into "ethic title". You’ll need to provide more information about the recruitment (see [bsl.socsci.uva.nl](http://bsl.socsci.uva.nl/)), then you can request publication.

2.  [StudySwap](https://twitter.com/Study_Swap)

    - <http://daniellakens.blogspot.com/2017/08/towards-more-collaborative-science-with.html>

3.  [/r/SampleSize](http://reddit.com/r/SampleSize)

4.  [SurveyCircle](https://www.surveycircle.com/)

***Paid***

1.  Qualtrics, Kantar, Nielsen, YouGov, Gallup, Harris Polls, Respondi, Dyanata, [MSI](https://msi-aci.com), [Prolific](https://www.prolific.com) (these last two are perhaps most affordable)

## Qualtrics

1.  If using Prolific, use [**embedded data**](https://researcher-help.prolific.com/en/articles/445133-recording-prolific-id-s) to automatically capture information like their Participant ID. Embedded data can also capture mobile vs. desktop, where they clicked on the survey link from, etc. See image above.

2.  Options: Security: **Anonymize responses**: “Don’t record respondents’ IP Address, location data, and contact info”

3.  Options: Responses: **Incomplete Survey Responses**: “How much time should pass before they’re considered incomplete?” Change this to 1 or 4 hours. Otherwise, it’s easy to miss participants that recently finished but didn’t press the final screen, and so haven’t been “recorded” yet.

4.  Use separate **blocks** for sections. It’s often easier to use separate blocks than to use page breaks, depending on the situation.

5.  Learn about [**survey flow**](https://www.qualtrics.com/support/survey-platform/survey-module/survey-flow/survey-flow-overview/), randomization, and branching.

6.  Use **request response** rather than **force response***:* it’s more ethical not to force participants.

7.  **Relabel** all variables from *V1*, *V2*, etc. to informative labels: *age*, *female*, etc. Notice that *female* is preferable over *gender* because the latter is ambiguous as to high vs. low. Keep the labels short and don’t use spaces or special characters (numbers are ok).

8.  There are three levels of **randomization**: of response options, of items within a scale, and of questionnaire stages/sections. I recommend randomization within variables (e.g., the order of the four identity questions); for the rest, please think through a plan that makes sense to you to minimize order effects, etc.

9.  **Manipulation checks**: in experiments, it’s good to add a question or two that require having paid attention to the manipulated content, whether or not they were convinced or changed their beliefs or preferences in any way. These manipulation checks measure exposure and basic comprehension of the treatment.

10. Add **timing** questions to some critical pages, e.g., the manipulation.

11. To control **participant behavior**, for example to maximize treatment exposure, consider using code to [show/hide the next button](https://wiki.harvard.edu/confluence/display/UHL/Qualtrics+Customizations) for a specified period, allow users to start a video but not pause it, etc.

12. To record **clicking: \[2/22 some are reporting issues with this code: be sure to pilot test\]**

    A\) Add the embedded variable to survey flow before the question block:

        clicked = 0

    B\) Add the link to the question text (in HTML mode):

        This is a link: <a href="http://www.google.com" target="_blank" id="extLink">Click here</a>

    C\) Add the following JavaScript to the question where "extLink" matches the id of the link in (2) and "clicked" matches the embedded variable in (A).

        Qualtrics.SurveyEngine.addOnload(function() {     $('extLink').on('click', function(name, event) {         Qualtrics.SurveyEngine.setEmbeddedData('clicked', '1');     }); });

13. Pilot test your study before launching it! A lot! See https://twitter.com/CameronBrick/status/1468880976092741635
