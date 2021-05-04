# CoWinSlotsChecker
AWS lambda function to check CoWin slots for 18+ for my pincodes. This  function is triggerred every 10 minutes using EventBridge and sends email using AWS SNS 

1. Deploy the python file (By changing the pincode as per your need ) as AWS Lambda function using Python3.7 runtime.
2. Create a trigger for lambda function from lambda console, using AWS EventBridge rule
3. Create AWS SNS topic and subscription for sending email.
4. Configure the subscription as destination on lambda function.
