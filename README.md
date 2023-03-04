# Live Cricket Score App

### Motivation

I'm a big cricket fan and always want to keep up with matches wherever I am. Currently, I use ![ESPNCricinfo](https://www.espncricinfo.com/) which is great on desktop however the mobile version is a bit too slow for my liking. Hence, I want to build my own version that means I'm up to date with the ball by ball coverage 🏏. This repo is concerned with the backend stack of the application.

#### Stack

- Python v3.8.10
- AWS CDK v2.64.0

#### Infrastructure

- AWS API Gateway
- AWS Lambda
- AWS Cloudfront

# Installation

Create a virtualenv:

```
$ python3 -m venv .venv
```

Activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Install the required dependencies.

```
$ pip install -r requirements.txt
```

Synthesize the CloudFormation template for this code.

```
$ cdk synth
```
