Starter tool for [flake8](https://flake8.pycqa.org/)

* [flake8 error codes](https://flake8.pycqa.org/en/latest/user/error-codes.html)
* [flake8-pylint](https://pypi.org/project/flake8-pylint/)
* [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)


## Setup

1. Run this script providing the path to the repository of your project. It will create the `.flake8` file in the root of the project. This configuration will ignore all the failure types in your code and it will also list them as comments
   for easier review.
1. Commit this file to your version control system and configure your CI system to run `flake8` on your code on every push. This will ensure no new type of failure will get past the CI system.

## Cleanup

1. Review the failures. Pick one of them that you feel is important to fix. Remove its code from the ignore list. Run `flake8` on your code to see where is this failure reported. Fix the code.
1. Commit your new version of the code and the `.flake8` file that does not ignore this error-type any more.
1. Repeate the cleanup process.

