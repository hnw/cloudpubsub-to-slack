import sys
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
    for env_name in ['SLACK_TOKEN', 'SLACK_CHANNEL']:
        if os.environ.get(env_name) is None:
            sys.exit('Specify environment variable "%s"' % env_name)

    keys = ['channel', 'username', 'icon_emoji', 'icon_url', 'mrkdwn']
    opts = {}
    for key in keys:
        env_name = 'SLACK_'+key.upper()
        val = os.environ.get(env_name)
        if val:
            opts[key] = val

    sc = SlackClient(slack_token)
    pp = pprint.PrettyPrinter()
    slack_text = pubsub_message
    if event['attributes']:
        slack_text = slack_text + "\n```\n" + pp.pformat(event['attributes']) + "\n```\n"
    sc.api_call(
        "chat.postMessage",
        text=slack_text,
        **opts
    )


if __name__ == '__main__':
    pubsub_to_slack({'data': 'Zm9v', 'attributes': {'bar': 'baz'}}, {})
