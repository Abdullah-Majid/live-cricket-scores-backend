#!/usr/bin/env python3
import os

import aws_cdk as cdk

from live_cricket_scores_backend.live_cricket_scores_backend_stack import LiveCricketScoresBackendStack


app = cdk.App()
LiveCricketScoresBackendStack(app, "LiveCricketScoresBackendStack")

app.synth()
