# Contributing to alertmanager-karma-proxy
The intended use case of this operator is to be deployed together with 
alertmanager-karma.

## Bugs and pull requests
- Generally, before developing enhancements to this charm, you should consider
  opening an issue explaining your use case.
- If you would like to chat with us about your use-cases or proposed
  implementation, you can reach us at
  [Canonical Mattermost public channel](https://chat.charmhub.io/charmhub/channels/charm-dev)
  or [Discourse](https://discourse.charmhub.io/).
- It is strongly recommended that prior to engaging in any enhancements
  to this charm you familiarise your self with Juju.
- Familiarising yourself with the
  [Charmed Operator Framework](https://juju.is/docs/sdk).
  library will help you a lot when working on PRs.
- All enhancements require review before being merged. Besides the
  code quality and test coverage, the review will also take into
  account the resulting user experience for Juju administrators using
  this charm. Please help us out in having easier reviews by rebasing
  onto the `main` branch, avoid merge commits and enjoy a linear Git
  history.


## Setup

A typical setup using [snaps](https://snapcraft.io/), for deployments
to a [microk8s](https://microk8s.io/) cluster can be found in the 
[Juju docs](https://juju.is/docs/olm/microk8s).

## Developing

Use your existing Python 3 development environment or create and
activate a Python 3 virtualenv

    virtualenv -p python3 venv
    source venv/bin/activate

Install the development requirements

    pip install -r requirements-dev.txt

Later on, upgrade packages as needed

    pip install --upgrade -r requirements-dev.txt


### Testing

    ./run_tests

## Build charm

Install the charmcraft tool

    sudo snap install charmcraft

Build the charm in this git repository using

    charmcraft pack

## Usage
See alertmanager-karma for details.

## Code overview
TODO

## Design choices
- Every alertmanager unit requires a proxy app. This allows to partially mimic a cross-model relation from 
  the point of view of the karma operator.

## Roadmap
- Support [additional fields](https://github.com/prymitive/karma/blob/main/docs/CONFIGURATION.md#alertmanagers),
  such as cluster name.