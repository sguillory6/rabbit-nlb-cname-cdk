#!/usr/bin/env python3

import aws_cdk as cdk

from the_basic_mq.the_basic_mq_stack import TheBasicMQStack


app = cdk.App()

env = cdk.Environment(account="750353892954",
                      region="us-west-2"
                      )

TheBasicMQStack(app, "TheBasicMQStack", env=env)

app.synth()
