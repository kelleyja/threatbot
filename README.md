# threatbot
Slackbot integration for Threatwatch.io

This bot is made for AWS Lambda and will do the following:

1. It receieves data as a Slack event any time someone mentions the bot's name in a Slack channel 
2. It will take that data and do something with it
3. It will respond to the originting slack channel via an incoming webhook url 

Here's what you need
In AWS:
1. An AWS REST API Gateway, Slack will POST data to this URL 
2.  A Lambda_function linked to the API gateway.  In this Repo it's called lambda_function.py.  ** in Lambda you must      define the handler, as written this is lambda_function.lambda_handler.  lambda_funtion.py is the filename and lambda_handler is defined in that file 
 
In Slack 
1. You need to create an APP that has the OAuth permissions to recieve events and post to a channel 
2. UNDER EVENTS - you'll need to post the URL of your API endpoint, we're not racking up any AWS charges unless the bot is mentioned so Slack will tell us via this URL 
3. Incoming Webhooks URL - We will POST the response data to this URL to make the bot respont to the user that mentioned it 

That's it 
