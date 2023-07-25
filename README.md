# Repo to reproduce bug for Azure ML Python SDK v2: batch endpoint job invoke operation.

The issue: https://github.com/Azure/azure-sdk-for-python/issues/31166

## Environment

There is conda env with python dependencies you must have to reproduce the issue.

List of dependencies can be found in `conda.lock.yml` file.

To create a virtual env out of that file:

```
conda env update --prune --file conda.lock.yml
conda activate neptune-recspoc
```

## Jupyter notebook to run the issue

### Pre-requisite

You must have a valid Microsoft azure subscription and Azure machine learning workspace.
There is a python jupyter notebook which should provide step-by-step guidance for the issue reproduction.

There is also might be required to provide a valid AML `environment` in the yaml configurations. Any should work.

**Location**: `msft-sdk-v2-test-batch-invoke-bug/aml/pipelines/collaborative_filtering_yaml/sdk-deploy-and-test-light.ipynb`

**Usage**: Substitute your subscription id, resource group id and workspace name in the notebook.
Execute cell by cell until you reach the last one with `.invoke()` function call.

While calling the last cell - take a look into your workspace batch endpoint jobs,
if it submits multiple jobs and in the end, you have an error out of API calls to the AML REST endpoint - then you reproduced the issue.
if it submits only one single job and there is no errors out of `.invoke()` call - the issue wasn't reproduced and it is expected behaviour.

More details can be found in the original github issue request: https://github.com/Azure/azure-sdk-for-python/issues/31166
