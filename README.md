# Open Utility Code Challenge :sunny: :partly_sunny: :rainbow:

Thanks for your interest in joining the OU team. Below are a number of tasks
for building our highly scientific weather forecasting feature. There are four
tasks and a fifth provisioning task available for extra credit. Each task
should take about 30 mins.


## Task 1

Write a function which takes a date and returns
 * “Rain” when the day of the month is an even number
 * “Wind” when the day of the month is a prime number
 * “Sun” when the day of the month is divisible by 3 or 5, but not both
 * “Overcast” if none of the above

For example “Rain, Sun” for 20th of the month.

## Task 2

Return a response to a GET request
 * /forecast/2017/01/07/ - `"Wind"`
 * /forecast/2017/01/09/ - `"Sun"`
 * /forecast/2017/01/12/ - `"Rain, Sun"`

## Task 3

Return a JSON object mapping dates to forecasts in response to POST request of
a JSON array of dates.

 * Request:
~~~~
["2017/01/03", "2017/03/14", "2017/03/15", "2017/07/24"]
~~~~
 * Response:
~~~~
{
  "2017/01/03": "Wind, Sun",
  "2017/03/14": "Rain",
  "2017/03/15": "Overcast",
  "2017/07/24": "Rain, Sun"
}
~~~~

## Task 4

Create and serve an HTML webpage which shows the forecast for the next 10 days.
The forecast should be loaded via a request to the API from Task 3. Bonus
points for use of flexbox.

## Provisioning

For additional credits - provide repeatable steps (with instructions) to
install all requirements and be able to run any tests or commands. Ideally the
solution would work on any platform. The minimum requirement is to work on OSX.


# Submitting your solutions

For each task do the following:

1. create a new branch
2. work on the new branch commiting early and often
3. create a pull request and merge your branch back into master
4. repeat for the next task
