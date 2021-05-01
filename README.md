# CoWinSlotsChecker
AWS lambda function to check CoWin slots for 18+ for my pincodes. This  function is triggerred every 10 minutes using EventBridge and sends email using AWS SNS 

1. Deploy the python file (By changing the pincode as per your need ) to AWS Lambda using Python3.7 runtime.
2. Create and attach lambda layer on top of it, using python.zip file
3. Create a trigger for lambda function from lambda console
4. Create SNS topic, subscription for sending email.
5. Configure the subscription as destination on lambda function.
