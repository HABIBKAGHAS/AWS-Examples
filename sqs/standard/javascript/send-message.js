const AWS = require("aws-sdk");
const MessageAttributes = require("../send-message.json");
// Create an SQS service object
var sqs = new AWS.SQS({ apiVersion: "2012-11-05", region: "us-east-1" });

const QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/376129873245/sqs-standard-deploy-MyQueue-xIiaOLZ4looK";

var params = {
  MessageBody: "Information about the largest city in Any Region." /* required */,
  QueueUrl: QUEUE_URL /* required */,
  DelaySeconds: 0,
  MessageAttributes: MessageAttributes,
};

sqs.sendMessage(params, function (err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else console.log(data); // successful response
});
