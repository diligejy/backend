## 1. What is GitHub Action

- GitHub Actions is a continuous integration and continuous delivery(CI/CD) platform that allows you to automate your build, test, and deployment pipeline.

## 2. Components of GitHub Actions

#### A. Workflows

- This is just processes you define in a YAML file that you use to run your jobs automatically or manually or on a schedule.

- Workflows are defined within the `.github/workflows` directory. You can have multiple workflows. Eg one for building and testing the other for deployment.

#### B. Events

- These are triggers that run workflows. Eg a pull request or a push request and much more.

#### C. Runner

- This is a virtual machine or a server that runs your workflows when triggered. Each workflow runs on its own virtual machine and a runner can run only one workflow at a time. 

- GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners. You can provision your own hosts to run a runner.

#### D. Action

- "An action is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task."

- Actions simpler are pre-written set of instructions used to perform tasks that are frequently used.

#### E. Job

- Step by step set of instructions that are exeucted on a runner.
- This instructions are actions or shell scripts.
- Steps in a job sare dependent on each other so are the step by step instructions and data sharing between each instruction is allowed

- Jobs by default are not dependent on other jobs and run independetly in parallel.

## 3. Example Project 1 

