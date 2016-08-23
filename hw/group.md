# Data acquisition group project

*Adapted from a previous project description by Prof. Matthew Dixon*

## Goals

The data acquisition project is a team project (2-4 students) with the goal of evaluating and experimenting with the data acquisition workflow.  

To get the ball rolling, each student must pose the kernel of a data acquisition problem and then students will vote on the proposals (via Canvas survey). We will then pick the top five or so. Each team must pick a project from one of those five. Teams must draw from students in the same class section. Teams will self-assemble, but the instructor reserves the right to override your choices.

You are not expected to actually perform the analytics--just the planning, writing, and data collection part. The analytics work itself is beyond the scope of the course.

## Deliverables

### Proposal

First, you must turn in a fleshed-out proposal that gives details on how you interpret and define the data acquisition problem chosen by your team. Ideally this would be one page and no longer. The intended audience is *business decision-maker* (who was not dropped on their head as a child).

Once you get the okay from me on this proposal, you can begin work to collect data associated with your project.

### Final Deliverable

The final deliverable is a PDF report that is a summary of what you have learned and a description of how you solved the problem. The intended audience for the final report is again *business decision-maker*, but you must add some meat for your *technical manager* in a technical details section.  The write up is meant to summarize your findings---it should not just be a data or Python code dump. Your report can include items and address question such as:

*  Statement of the problem you're solving in non-technical terms
*  Summary of your main findings in a table or similar format
*  Your recommendations for pursuing this problem further
*  Experiments or evaluations you performed
*  Challenges and issues you encountered
*  Description of any assumptions you made about the problem or the data
*  Useful URLs to data sources or descriptions

Also, from your description, it should be clear to the reader what software you wrote to collect and process data. E.g., from where did you pull data, what format, what data structure represented this data in memory, what processing you did to clean or fill in missing data, etc...

## Advice

Remember that this is a data acquisition project, which means that the focus is primarily on using the skills that you’ve learned in this course. Don't race off into machine learning land (just yet!).

* Try not to get lost in the details for the main report. It’s important that you summarize the challenges in data acquisition rather than provide a dry set of instructions on how to access and clean the data.
* Technical details should be isolated in a section by itself, so as not to frighten off business droids.* You can assume that all readers understand use of basic terminology such as REST, URL, Python script.
* Conciseness is key (without being too vague) and the content of your report is more important than elegance, aesthetics and flashy designer logos, etc...* Try to make your insight actionable. How could someone who hasn’t taken this course evaluate and use your findings?

To give you a flavor for the various elements you describe in the project, here is how you might describe your experiments to the business decision-maker audience:

> We implemented a python data acquisition application to extract JSON and XML files from data sources X, Y, and Z and merged them into memory as a Q structure. This application was automatically run hourly over N weeks to avoid breaching throttle limits and to overcome limitations on the maximum number of companies returned by RESTful API queries. We subsequently merged data sources by transforming company names into canonical form.## Evaluation

The evaluation of your final report is necessarily subjective, but I will consider, among other things:

* the clarity of your report
* the difficulty of the problem you attempted
* your methodology for data acquisition
* whether you have useful software collecting data

As usual, an **A** grade means your team did extremely well on the project, **B** means your team did a decent job, and **C** or below means your team's work was unsatisfactory. **+/-** can be used to shade the above grades.

**All students will anonymously report their impression of team member contributions, which will affect an individual's project grade.**