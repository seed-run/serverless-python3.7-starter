import numpy as np
import json
import boto3

def hello(event, context):
  a = np.arange(15).reshape(3, 5)
  print("Your numpy array:")
  print(a);

  return {
    "statusCode": 200,
    "body": json.dumps({
      "message": "Python Hello with tests!!",
    })
  }

