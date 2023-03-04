from aws_cdk import ( aws_lambda as _lambda, aws_apigateway as apigw, aws_lambda_python_alpha as _alambda, Stack)
from constructs import Construct

class LiveCricketScoresBackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        match_lambda = _alambda.PythonFunction(
            self, 
            'GetDataHandler', 
            runtime=_lambda.Runtime.PYTHON_3_9,
            entry="./lambda/",
            index="handler.py",
            handler='lambda_handler',
        )
        apigw.LambdaRestApi(
            self,
            'cricket-data-api',
            handler=match_lambda
        )
        