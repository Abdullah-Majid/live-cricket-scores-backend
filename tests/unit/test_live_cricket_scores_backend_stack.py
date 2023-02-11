import aws_cdk as core
import aws_cdk.assertions as assertions

from live_cricket_scores_backend.live_cricket_scores_backend_stack import LiveCricketScoresBackendStack

# example tests. To run these tests, uncomment this file along with the example
# resource in live_cricket_scores_backend/live_cricket_scores_backend_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LiveCricketScoresBackendStack(app, "live-cricket-scores-backend")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
