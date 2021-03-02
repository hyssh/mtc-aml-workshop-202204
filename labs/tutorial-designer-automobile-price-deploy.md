---
title: 'Tutorial: Deploy ML models with the designer'
titleSuffix: Azure Machine Learning
description: Build a predictive analytics solution in Azure Machine Learning designer. Train, score, and deploy a machine learning model using drag-and-drop modules.

author: likebupt
ms.author: keli19
services: machine-learning
ms.service: machine-learning
ms.subservice: core
ms.topic: tutorial
ms.date: 01/15/2021
ms.custom: designer
---

# Tutorial: Deploy a machine learning model with the designer

> Source of this document: [Tutorial: Deploy a machine learning model with the designer](https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-designer-automobile-price-deploy)

You can deploy the predictive model developed in [part one of the tutorial](tutorial-designer-automobile-price-train-score.md) to give others a chance to use it. In part one, you trained your model. Now, it's time to generate predictions based on user input. In this part of the tutorial, you will:

> * Create a real-time inference pipeline.
> * Create an inferencing cluster.
> * Deploy the real-time endpoint.
> * Test the real-time endpoint.

## Prerequisites

Complete [part one of the tutorial](tutorial-designer-automobile-price-train-score.md) to learn how to train and score a machine learning model in the designer.

## Create a real-time inference pipeline

To deploy your pipeline, you must first convert the training pipeline into a real-time inference pipeline. This process removes training modules and adds web service inputs and outputs to handle requests.

### Create a real-time inference pipeline

1. Above the pipeline canvas, select **Create inference pipeline** > **Real-time inference pipeline**.

    ![create-inference-pipeline](../images/tutorial2-create-inference-pipeline.png)

    Your pipeline should now look like this: 

   ![Screenshot showing the expected configuration of the pipeline after preparing it for deployment](../images/real-time-inference-pipeline.png)

    When you select **Create inference pipeline**, several things happen:
    
    * The trained model is stored as a **Dataset** module in the module palette. You can find it under **My Datasets**.
    * Training modules like **Train Model** and **Split Data** are removed.
    * The saved trained model is added back into the pipeline.
    * **Web Service Input** and **Web Service Output** modules are added. These modules show where user data enters the pipeline and where data is returned.

    > [NOTE]
    > By default, the **Web Service Input** will expect the same data schema as the training data used to create the predictive pipeline. In this scenario, price is included in the schema. However, price isn't used as a factor during prediction.
    >

1. Select **Submit**, and use the same compute target and experiment that you used in part one.

    If this is the first run, it may take up to 20 minutes for your pipeline to finish running. The default compute settings have a minimum node size of 0, which means that the designer must allocate resources after being idle. Repeated pipeline runs will take less time since the compute resources are already allocated. Additionally, the designer uses cached results for each module to further improve efficiency.

1. Select **Deploy**.

## Create an inferencing cluster

In the dialog box that appears, you can select from any existing Azure Kubernetes Service (AKS) clusters to deploy your model to. If you don't have an AKS cluster, use the following steps to create one.

1. Select **Compute** in the dialog box that appears to go to the **Compute** page.

1. On the navigation ribbon, select **Inference Clusters** > **+ New**.

    ![Screenshot showing how to get to the new inference cluster pane](../images/new-inference-cluster.png)
   
1. In the inference cluster pane, configure a new Kubernetes Service.

1. Enter *aks-compute* for the **Compute name**.
    
1. Select a nearby region that's available for the **Region**.

1. Select **Create**.

    > [NOTE]
    > It takes approximately 15 minutes to create a new AKS service. You can check the provisioning state on the **Inference Clusters** page.
    >

## Deploy the real-time endpoint

After your AKS service has finished provisioning, return to the real-time inferencing pipeline to complete deployment.

1. Select **Deploy** above the canvas.

1. Select **Deploy new real-time endpoint**. 

1. Select the AKS cluster you created.

    ![setup-endpoint](../images/setup-endpoint.png)

    You can also change **Advanced** setting for your real-time endpoint.
    
    |Advanced setting|Description|
    |---|---|
    |Enable Application Insights diagnostics and data collection| Whether to enable Azure Application Ingishts to collect data from the deployed endpoints. </br> By default: false |
    |Scoring timeout| A timeout in milliseconds to enforce for scoring calls to the web service.</br>By default: 60000|
    |Auto scale enabled|   Whether to enable autoscaling for the web service.</br>By default: true|
    |Min replicas| The minimum number of containers to use when autoscaling this web service.</br>By default: 1|
    |Max replicas| The maximum number of containers to use when autoscaling this web service.</br> By default: 10|
    |Target utilization|The target utilization (in percent out of 100) that the autoscaler should attempt to maintain for this web service.</br> By default: 70|
    |Refresh period|How often (in seconds) the autoscaler attempts to scale this web service.</br> By default: 1|
    |CPU reserve capacity|The number of CPU cores to allocate for this web service.</br> By default: 0.1|
    |Memory reserve capacity|The amount of memory (in GB) to allocate for this web service.</br> By default: 0.5|
        

1. Select **Deploy**. 

    A success notification above the canvas appears after deployment finishes. It might take a few minutes.

> [TIP]
> You can also deploy to **Azure Container Instance** (ACI) if you select **Azure Container Instance** for **Compute type** in the real-time endpoint setting box.
> Azure Container Instance is used for testing or development. Use ACI for low-scale CPU-based workloads that require less than 48 GB of RAM.

## Test the real-time endpoint

After deployment finishes, you can view your real-time endpoint by going to the **Endpoints** page.

1. On the **Endpoints** page, select the endpoint you deployed.

    In the **Details** tab, you can see more information such as the REST URI, Swagger definition, status, and tags.

    In the **Consume** tab, you can find sample consumption code, security keys, and set authentication methods.

    In the **Deployment logs** tab, you can find the detailed deployment logs of your real-time endpoint.

1. To test your endpoint, go to the **Test** tab. From here, you can enter test data and select **Test** verify the output of your endpoint.

For more information on consuming your web service, see [Consume a model deployed as a webservice](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-consume-web-service?tabs=python)

## Go back to main

> [Go back to main](readme.md)