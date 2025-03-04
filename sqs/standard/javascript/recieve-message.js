// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");

// Create an SQS service object
var sqs = new AWS.SQS({ apiVersion: "2012-11-05", region: "us-east-1" });

var queueURL = "https://sqs.us-east-1.amazonaws.com/376129873245/sqs-standard-deploy-MyQueue-xIiaOLZ4looK";

var params = {
  AttributeNames: ["All"],
  MaxNumberOfMessages: 10,
  MessageAttributeNames: ["All"],
  QueueUrl: queueURL,
  VisibilityTimeout: 20,
  WaitTimeSeconds: 0,
};

sqs.receiveMessage(params, function (err, data) {
  if (err) {
    console.log("Receive Error", err);
  } else if (data.Messages) {
    var deleteParams = {
      QueueUrl: queueURL,
      ReceiptHandle: data.Messages[0].ReceiptHandle,
    };
    console.log(data.Messages.map((x) => x.MessageAttributes));
    sqs.deleteMessage(deleteParams, function (err, data) {
      if (err) {
        console.log("Delete Error", err);
      } else {
        console.log("Message Deleted", data);
      }
    });
  }
});
