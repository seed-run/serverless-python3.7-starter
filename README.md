# Serverless Python3.7 Starter with Plugin

A Python3.7 starter project for [Serverless Framework](https://serverless.com/framework/) with [serverless-python-requirements plugin](https://github.com/UnitedIncome/serverless-python-requirements).

### Requirements

- [Install Python](https://www.python.org/downloads/)
- [Install the Serverless Framework](https://serverless.com/framework/docs/providers/aws/guide/installation/)
- [Configure your AWS CLI](https://serverless.com/framework/docs/providers/aws/guide/credentials/)

### Installation

Create a new project

```sh
$ serverless install --url https://github.com/fwang/serverless-python3.7-starter --name serverless-python37-starter
```

Install Serverless plugin: serverless-python-requirements

```sh
$ npm install
```

### Usage

Invoke a function locally

```sh
$ serverless invoke local -f hello
```

### Deploying

Deploy your project

```sh
$ serverless deploy
```

Deploy a single function

```sh
$ serverless deploy function --function hello
```

### Support

- Send us an [email](mailto:frank@seed.run) if you have any questions
- Open a [new issue](https://github.com/AnomalyInnovations/serverless-python3.7-starter/issues/new) if you've found a bug or have some suggestions.
- Or submit a pull request!

### Maintainers

Maintained by Frank Wang ([@fanjiewang](https://twitter.com/fanjiewang)) & Jay V ([@jayair](https://twitter.com/jayair)). [**Subscribe to our newsletter**](http://eepurl.com/cEaBlf) for updates. Send us an [email](mailto:contact@anoma.ly) if you have any questions.
