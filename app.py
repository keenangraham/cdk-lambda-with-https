from aws_cdk import App
from aws_cdk import Environment
from aws_cdk import Stack

from constructs import Construct


US_WEST_2 = Environment(
    account='618537831167',
    region='us-west-2',
)


class LambdaWithHttpsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


app = App()


LambdaWithHttpsStack(
    app,
    'LambdaWithHttpsStack',
    env=US_WEST_2,
)

app.synth()
