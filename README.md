# cloudpubsub-to-slack

Pub/Sub-triggerd Cloud Function which transfers Pub/Sub message to Slack.

## How to deploy

```
$ gcloud beta functions deploy [function_name] \
    --runtime=python37 --entry-point=pubsub_to_slack \
    --trigger-topic=[topic_name] \
    --set-env-vars=SLACK_TOKEN=[token],SLACK_CHANNEL=[channel]
```

## Environment variables

- SLACK_TOKEN
- SLACK_CHANNEL
