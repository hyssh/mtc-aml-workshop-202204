# What are compute targets in Azure Machine Learning?

> Original document located in: https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target

A *compute target* is a designated compute resource or environment where you run your training script or host your service deployment. This location might be your local machine or a cloud-based compute resource. Using compute targets makes it easy for you to later change your compute environment without having to change your code.

In a typical model development lifecycle, you might:

1. Start by developing and experimenting on a small amount of data. At this stage, use your local environment, such as a local computer or cloud-based virtual machine (VM), as your compute target.
1. Scale up to larger data, or do distributed training by using one of these [training compute targets](#train).
1. After your model is ready, deploy it to a web hosting environment or IoT device with one of these [deployment compute targets](#deploy).

The compute resources you use for your compute targets are attached to a [workspace](concept-workspace.md). Compute resources other than the local machine are shared by users of the workspace.

## Training compute targets

Azure Machine Learning has varying support across different compute targets. A typical model development lifecycle starts with development or experimentation on a small amount of data. At this stage, use a local environment like your local computer or a cloud-based VM. As you scale up your training on larger datasets or perform distributed training, use Azure Machine Learning compute to create a single- or multi-node cluster that autoscales each time you submit a run. You can also attach your own compute resource, although support for different scenarios might vary.

**Compute targets can be reused from one training job to the next.** For example, after you attach a remote VM to your workspace, you can reuse it for multiple jobs. For machine learning pipelines, use the appropriate [pipeline step](/python/api/azureml-pipeline-steps/azureml.pipeline.steps) for each compute target.

You can use any of the following resources for a training compute target for most jobs. Not all resources can be used for automated machine learning, machine learning pipelines, or designer.

|Training &nbsp;targets|[Automated machine learning](../articles/machine-learning/concept-automated-ml.md) | [Machine learning pipelines](../articles/machine-learning/concept-ml-pipelines.md) | [Azure Machine Learning designer](../articles/machine-learning/concept-designer.md)
|----|:----:|:----:|:----:|
|[Local computer](../articles/machine-learning/how-to-attach-compute-targets.md#local)| Yes | &nbsp; | &nbsp; |
|[Azure Machine Learning compute cluster](../articles/machine-learning/how-to-create-attach-compute-cluster.md)| Yes | Yes | Yes |
|[Azure Machine Learning compute instance](../articles/machine-learning/how-to-create-manage-compute-instance.md) | Yes (through SDK)  | Yes |  |
|[Remote VM](../articles/machine-learning/how-to-attach-compute-targets.md#vm) | Yes  | Yes | &nbsp; |
|[Azure&nbsp;Databricks](../articles/machine-learning/how-to-attach-compute-targets.md#databricks)| Yes (SDK local mode only) | Yes | &nbsp; |
|[Azure Data Lake Analytics](../articles/machine-learning/how-to-attach-compute-targets.md#adla) | &nbsp; | Yes | &nbsp; |
|[Azure HDInsight](../articles/machine-learning/how-to-attach-compute-targets.md#hdinsight) | &nbsp; | Yes | &nbsp; |
|[Azure Batch](../articles/machine-learning/how-to-attach-compute-targets.md#azbatch) | &nbsp; | Yes | &nbsp; |

> [!TIP]
> The compute instance has 120GB OS disk. If you run out of disk space, [use the terminal](../articles/machine-learning/how-to-access-terminal.md) to clear at least 1-2 GB before you [stop or restart](../articles/machine-learning/how-to-create-manage-compute-instance.md#manage) the compute instance.


## Compute targets for inference

The following compute resources can be used to host your model deployment.

The compute target you use to host your model will affect the cost and availability of your deployed endpoint. Use this table to choose an appropriate compute target.

| Compute target | Used for | GPU support | FPGA support | Description |
| ----- | ----- | ----- | ----- | ----- |
| [Local&nbsp;web&nbsp;service](../articles/machine-learning/how-to-deploy-local-container-notebook-vm.md) | Testing/debugging | &nbsp; | &nbsp; | Use for limited testing and troubleshooting. Hardware acceleration depends on use of libraries in the local system.
| [Azure Kubernetes Service (AKS)](../articles/machine-learning/how-to-deploy-azure-kubernetes-service.md) | Real-time inference |  [Yes](../articles/machine-learning/how-to-deploy-inferencing-gpus.md) (web service deployment) | [Yes](../articles/machine-learning/how-to-deploy-fpga-web-service.md)   |Use for high-scale production deployments. Provides fast response time and autoscaling of the deployed service. Cluster autoscaling isn't supported through the Azure Machine Learning SDK. To change the nodes in the AKS cluster, use the UI for your AKS cluster in the Azure portal. <br/><br/> Supported in the designer. |
| [Azure Container Instances](../articles/machine-learning/how-to-deploy-azure-container-instance.md) | Testing or development | &nbsp;  | &nbsp; | Use for low-scale CPU-based workloads that require less than 48 GB of RAM. <br/><br/> Supported in the designer. |
| [Azure Machine Learning compute clusters](../articles/machine-learning/tutorial-pipeline-batch-scoring-classification.md) | Batch&nbsp;inference | [Yes](../articles/machine-learning/tutorial-pipeline-batch-scoring-classification.md) (machine learning pipeline) | &nbsp;  | Run batch scoring on serverless compute. Supports normal and low-priority VMs. No support for realtime inference.|

> Although compute targets like local, Azure Machine Learning compute, and Azure Machine Learning compute clusters support GPU for training and experimentation, using GPU for inference _when deployed as a web service_ is supported only on AKS.
>
> Using a GPU for inference _when scoring with a machine learning pipeline_ is supported only on Azure Machine Learning compute.
>
> When choosing a cluster SKU, first scale up and then scale out. Start with a machine that has 150% of the RAM your model requires, profile the result and find a machine that has the performance you need. Once you've learned that, increase the number of machines to fit your need for concurrent inference.
> * Container instances are suitable only for small models less than 1 GB in size.
> * Use single-node AKS clusters for dev/test of larger models.

When performing inference, Azure Machine Learning creates a Docker container that hosts the model and associated resources needed to use it. This container is then used in one of the following deployment scenarios:

* As a *web service* that's used for real-time inference. Web service deployments use one of the following compute targets:

    * [Local computer](how-to-attach-compute-targets.md#local)
    * [Azure Machine Learning compute instance](how-to-create-manage-compute-instance.md)
    * [Azure Container Instances](how-to-attach-compute-targets.md#aci)
    * [Azure Kubernetes Service](how-to-create-attach-kubernetes.md)
    * Azure Functions (preview). Deployment to Functions only relies on Azure Machine Learning to build the Docker container. From there, it's deployed by using Functions. For more information, see [Deploy a machine learning model to Azure Functions (preview)](how-to-deploy-functions.md).

* As a _batch inference_ endpoint that's used to periodically process batches of data. Batch inferences use [Azure Machine Learning compute clusters](how-to-create-attach-compute-cluster.md).

* To an _IoT device_ (preview). Deployment to an IoT device only relies on Azure Machine Learning to build the Docker container. From there, it's deployed by using Azure IoT Edge. For more information, see [Deploy as an IoT Edge module (preview)](../iot-edge/tutorial-deploy-machine-learning.md).

Learn [where and how to deploy your model to a compute target](how-to-deploy-and-where.md).

<a name="amlcompute"></a>
## Azure Machine Learning compute (managed)

A managed compute resource is created and managed by Azure Machine Learning. This compute is optimized for machine learning workloads. Azure Machine Learning compute clusters and [compute instances](concept-compute-instance.md) are the only managed computes.

You can create Azure Machine Learning compute instances or compute clusters from:

* [Azure Machine Learning studio](how-to-create-attach-compute-studio.md).
* The Python SDK and CLI:
    * [Compute instance](how-to-create-manage-compute-instance.md).
    * [Compute cluster](how-to-create-attach-compute-cluster.md).
* The [R SDK](https://azure.github.io/azureml-sdk-for-r/reference/index.html#section-compute-targets) (preview).
* An Azure Resource Manager template. For an example template, see [Create an Azure Machine Learning compute cluster](https://github.com/Azure/azure-quickstart-templates/tree/master/101-machine-learning-compute-create-amlcompute).
* A machine learning [extension for the Azure CLI](reference-azure-machine-learning-cli.md#resource-management).

When created, these compute resources are automatically part of your workspace, unlike other kinds of compute targets.


|Capability  |Compute cluster  |Compute instance  |
|---------|---------|---------|
|Single- or multi-node cluster     |    **&check;**       |         |
|Autoscales each time you submit a run     |     **&check;**      |         |
|Automatic cluster management and job scheduling     |   **&check;**        |     **&check;**      |
|Support for both CPU and GPU resources     |  **&check;**         |    **&check;**       |



> When a compute *cluster* is idle, it autoscales to 0 nodes, so you don't pay when it's not in use. A compute *instance* is always on and doesn't autoscale. You should [stop the compute instance](how-to-create-manage-compute-instance.md#manage) when you aren't using it to avoid extra cost.

### Supported VM series and sizes

When you select a node size for a managed compute resource in Azure Machine Learning, you can choose from among select VM sizes available in Azure. Azure offers a range of sizes for Linux and Windows for different workloads. To learn more, see [VM types and sizes](../virtual-machines/sizes.md).

There are a few exceptions and limitations to choosing a VM size:

* Some VM series aren't supported in Azure Machine Learning.
* Some VM series are restricted. To use a restricted series, contact support and request a quota increase for the series. For information on how to contact support, see [Azure support options](https://azure.microsoft.com/support/options/).

See the following table to learn more about supported series and restrictions.

| **Supported VM series**  | **Restrictions** | **Category** | **Supported by** |
|------------|------------|------------|------------|
| D | None. | General purpose | Compute clusters and instance |
| DDSv4 | None. | General purpose | Compute clusters and instance |
| Dv2 | None. | General purpose | Compute clusters and instance |
| Dv3 | None.| General purpose | Compute clusters and instance |
| DSv2 | None. | General purpose | Compute clusters and instance |
| DSv3 | None.| General purpose | Compute clusters and instance |
| EAv4 | None. | Memory optimized | Compute clusters and instance |
| Ev3 | None. | Memory optimized | Compute clusters and instance |
| FSv2 | None. | Compute optimized | Compute clusters and instance |
| H | None. | High performance compute | Compute clusters and instance |
| HB | Requires approval. | High performance compute | Compute clusters and instance |
| HBv2 | Requires approval. |  High performance compute | Compute clusters and instance |
| HCS | Requires approval. |  High performance compute | Compute clusters and instance |
| M | Requires approval. | Memory optimized | Compute clusters and instance |
| NC | None. |  GPU | Compute clusters and instance |
| NC Promo | None. | GPU | Compute clusters and instance |
| NCsv2 | Requires approval. | GPU | Compute clusters and instance |
| NCsv3 | Requires approval. | GPU | Compute clusters and instance |  
| NDs | Requires approval. | GPU | Compute clusters and instance | 
| NDv2 | Requires approval. | GPU | Compute clusters and instance | 
| NV | None. | GPU | Compute clusters and instance | 
| NVv3 | Requires approval. | GPU | Compute clusters and instance | 


While Azure Machine Learning supports these VM series, they might not be available in all Azure regions. To check whether VM series are available, see [Products available by region](https://azure.microsoft.com/global-infrastructure/services/?products=virtual-machines).


> Azure Machine Learning doesn't support all VM sizes that Azure Compute supports. To list the available VM sizes, use one of the following methods:
> * [REST API](https://github.com/Azure/azure-rest-api-specs/blob/master/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/stable/2020-08-01/examples/ListVMSizesResult.json)
> * [Python SDK](/python/api/azureml-core/azureml.core.compute.amlcompute.amlcompute#supported-vmsizes-workspace--location-none-)
>

### Compute isolation

Azure Machine Learning compute offers VM sizes that are isolated to a specific hardware type and dedicated to a single customer. Isolated VM sizes are best suited for workloads that require a high degree of isolation from other customers' workloads for reasons that include meeting compliance and regulatory requirements. Utilizing an isolated size guarantees that your VM will be the only one running on that specific server instance.

The current isolated VM offerings include:

* Standard_M128ms
* Standard_F72s_v2
* Standard_NC24s_v3
* Standard_NC24rs_v3*

*RDMA capable

## Unmanaged compute

An unmanaged compute target is *not* managed by Azure Machine Learning. You create this type of compute target outside Azure Machine Learning and then attach it to your workspace. Unmanaged compute resources can require additional steps for you to maintain or to improve performance for machine learning workloads.

---

[Go back to main page](https://github.com/hyssh/mtc-open-workshop)
