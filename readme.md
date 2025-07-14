# Getting Started

This mini-project contains a small set of challenges for interviewing. This test is mostly focused
on how well candidates can adapt to a codebase and solve some typical problems.

## Test Expectations

This project assumes the following:

1. You have access to python 3.9. Anything newer _should_ work, but is not guaranteed.
2. You have access to pypi to download the few requirements.
3. You're running on Linux or Macos (or similar *nix based platform). There should be nothing stopping
   you from doing this in Windows, but the advice here isn't set up to support that.
4. Most importantly, you have some experience with Python -- in particular, in a more software-engineering
   based way (as opposed to data engineering).

This test is intended to be a slightly more specific whiteboarding-like exercise. That is, we hope
at the end of this process there is runnable code. However, this is not a strict requirement and there
is more an emphasis on logic-correctness.

**Please remember**:

- Feel free to ask questions if you have any. We're also here to help.
- Talk through your implementation. We don't know what you're thinking if you don't say it outloud.
- Relax. Our goal isn't to trick or decieve -- we're hoping we're talking to a future colleague today!

## Setup and running locally

To turn this into a (theoretically) runnable project, do the following:

1. Create a virtual environment: `python3 -m venv venv`
2. activate the virtual environment: `source venv/bin/activate`
3. Install the dependencies: `pip install -r requirements.txt`

The program is intended to be started from onboard_user or another lambda. There is a basic test runner
in src/_local_runs/run.py. You can start it by running `python3 src/_local_runs/run.py`

Note that this application reaches out to localhost to make network connections. These are not
currently provided, so the application is likely to fail when it invokes those APIs.
