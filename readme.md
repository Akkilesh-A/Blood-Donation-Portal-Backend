# Blood Donation Portal V2

The Blood Donation Portal V2

## Contributing to Blood Donation Portal V2

We welcome contributions to enhance the functionality and stability of the Blood Donation Portal V2. Below are guidelines for contributing to the main repository.

Feel free to raise a pull request to [the main repository](https://github.com/ShyamSundhar1411/Blood-Donation-Portal-V2). The maintainers will review your proposed modifications, provide feedback, and merge your changes if appropriate. Discussions are encouraged to ensure the code meets the project's standards.

### Getting Started

1. Create your fork of the repository.

```bash
# Clone your fork
$ git clone [path_to_your_fork]

# Navigate to the project directory
$ cd blood-donation-portal-v2

# Add the upstream repository
$ git remote add upstream [URL_of_main_repository]


2. Configuring Environment

Setting up development environment.

**Step 1**: Install make
 - windows (Run in power shell)
    ```bash
      winget install GnuWin32.Make
    ```
    Add ```C:\Program Files (x86)\GnuWin32\bin``` to path
 - Linux based system
    ```bash
    sudo apt-get -y install make
    ```
**Step 2**: Install poetry
  ```bash
  pip install poetry
  ```
**Step 3**: Install dependencies
  ```bash
  poetry install
  ```
**Step 4**: Run server
  ```bash
   make run-server
  ```
​
## Making Changes
​
1. Make all your changes in a `topic branch` created from your fork's `develop`. Here example of GraphQL is used for explanation purposes.
​
   `$ git fetch upstream && git checkout GraphQL && git rebase upstream/GraphQL`
   `$ git checkout GraphQL && git checkout -b <topic-branch-name>`
​
2. Make sure that your changes adhere to the current coding conventions used throughout the project, indentation, accurate comments, etc.
3. Lint your code regularly and ensure it passes prior to submitting a PR
4. Ensure existing tests pass and include test cases which fail without your change and succeed with it.
​
## Commit Message Naming Guidelines
​
1. Commit messages should be of the format `commit-type(Affected-Section): Description of the task that has been implemented.`
2. Commit Types can be from the following: `chore, feat, docs, style, fix, refactor, test`
​
An example can be: `docs(Guidelines): Added initial files for documentation`
​
## Submitting Changes
1. Run tests for dJango with the following command `python3 manage.py test`.
2. Before commiting a new change, make sure pre-commit hooks are installed.
```bash
    make setup-hooks
```
3. Commit your changes. When making a new commit, `pre-commit` will run linters on all staged files as for django. Resolve any remaining issues reported by the linters, stage the changed files and attempt to commit again until resolution.
4. Push your topic branch up to your fork: `$ git push origin <topic-branch-name>`.
5. Open a Pull Request with a clear title and description.
​
Note: All the migration files associated with the backend changes will be ignored.
​
## After your PR is merged
​
1. You may choose to delete the topic branch.
2. Update your local copy's `GraphQL` branch with the `upstream`'s updated `GraphQL`:
​
   `$ git fetch upstream && git checkout GraphQL && git rebase upstream/GraphQL`
​
3. Push the updated GraphQL branch to `origin`:
​
   `$ git push origin GraphQL`
​
You will be all updated and ready to make new changes now
​
If you have any questions about contributing, feel free to reach out the repository maintainers.
