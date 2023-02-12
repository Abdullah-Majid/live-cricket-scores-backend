from aws_cdk import ( aws_lambda as _lambda, aws_apigateway as apigw, aws_lambda_python_alpha as _alambda, Stack)
from constructs import Construct

class LiveCricketScoresBackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _alambda.PythonFunction(
            self, 
            'GetMatchesHandler', 
            runtime=_lambda.Runtime.PYTHON_3_9,
            entry="./lambda/",
            index="get_matches.py",
            handler='handler',
        )
        apigw.LambdaRestApi(
            self,
            'cricket-data-api',
            handler=my_lambda
        )
