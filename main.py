import os
import pprint
import base64
from slackclient import SlackClient

def pubsub_to_slack(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    slack_token = os.environ.get('SLACK_TOKEN')
    slack_channel = os.environ.get('SLACK_CHANNEL')
    sc = SlackClient(slack_token)
    pp = pprint.PrettyPrinter()
    slack_text=pubsub_message
    if event['attributes']:
        slack_text = slack_text + "\n```\n" + pp.pformat(event['attributes']) + "\n```\n"
    sc.api_call(
        "chat.postMessage",
        channel=slack_channel,
        text=slack_text
    )

if __name__ == '__main__':
    pubsub_to_slack({'data':'Zm9v', 'attributes':{'bar':'baz'}}, {})
