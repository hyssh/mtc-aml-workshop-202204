# Lab: Automated Machine Learning

## Tutorial: Create a classification model with automated ML in Azure Machine Learning

Source of this tutorial: https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-first-experiment-automated-ml

In this tutorial, you learn how to create a simple classification model without writing a single line of code using automated machine learning in the Azure Machine Learning studio. This classification model predicts if a client will subscribe to a fixed term deposit with a financial institution.

With automated machine learning, you can automate away time intensive tasks. Automated machine learning rapidly iterates over many combinations of algorithms and hyperparameters to help you find the best model based on a success metric of your choosing.

In this tutorial, you learn how to do the following tasks:

> * Create an Azure Machine Learning workspace.
> * Run an automated machine learning experiment.
> * View experiment details.
> * Understand the experiments results

## Get started in Azure Machine Learning studio

You complete the following experiment set-up and run steps  via the Azure Machine Learning studio at https://ml.azure.com, a consolidated web interface that includes machine learning tools to perform data science scenarios for data science practitioners of all skill levels. The studio is not supported on Internet Explorer browsers.


1. Before you start Auomated ML job, download [bankmarketing_train.csv](https://mtcseattle.blob.core.windows.net/mtcopenworkshop/bankmarketing_train.csv?sp=r&st=2021-04-01T20:50:04Z&se=2029-04-02T04:50:04Z&spr=https&sv=2020-02-10&sr=b&sig=U5lhyfJVv4kpruqDpO5mPqfacT3FeYQN%2F1kKwcv1w1U%3D) file to your local computer. The file will be used for this lab.

1. Sign in to [Azure Machine Learning studio](https://ml.azure.com).

1. Select your subscription and the workspace you created.

1. Select **Get started**.

1. In the left pane, select **Automated ML** under the **Author** section.

   Since this is your first automated ML experiment, you'll see an empty list and links to documentation.

   ![Get started page](../images/get-started.png)

1. Select **+New automated ML run**. 

## Create and load dataset

Before you configure your experiment, upload your data file to your workspace in the form of an Azure Machine Learning dataset. Doing so, allows you to ensure that your data is formatted appropriately for your experiment.

1. Create a new dataset by selecting **From local files** from the  **+Create dataset** drop-down. 

    1. On the **Basic info** form, give your dataset a name and provide an optional description. The automated ML interface currently only supports TabularDatasets, so the dataset type should default to *Tabular*.

    1. Select **Next** on the bottom left

    1. On the **Datastore and file selection** form, select the default datastore that was automatically set up during your workspace creation, **workspaceblobstore (Azure Blob Storage)**. This is where you'll upload your data file to make it available to your workspace.

    1. Select **Browse**.
    
    1. Locate the file, '**bankmarketing_train.csv**' you download in local computer and use the file for training.

    1. Select **Next** on the bottom left, to  upload it to the default container that was automatically set up during your workspace creation.  
    
       When the upload is complete, the Settings and preview form is pre-populated based on the file type. 
       
    1. Verify that the **Settings and preview** form is populated as follows and select **Next**.
        
        Field|Description| Value for tutorial
        ---|---|---
        File format|Defines the layout and type of data stored in a file.| Delimited
        Delimiter|One or more characters for specifying the boundary between&nbsp; separate, independent regions in plain text or other data streams. |Comma
        Encoding|Identifies what bit to character schema table to use to read your dataset.| UTF-8
        Column headers| Indicates how the headers of the dataset, if any, will be treated.| All files have same headers
        Skip rows | Indicates how many, if any, rows are skipped in the dataset.| None

    1. The **Schema** form allows for further configuration of your data for this experiment. For this example, select the toggle switch for the **day_of_week**, so as to not include it. Select **Next**.
         ![Schema form](../images/schema-tab-config.gif)
    1. On the **Confirm details** form, verify the information matches what was previously  populated on the **Basic info, Datastore and file selection** and **Settings and preview** forms. Leave 'Profile this dataset after creation' unchecked.
    
    1. Select **Create** to complete the creation of your dataset.
    
    1. Select your dataset once it appears in the list.
    
    1. Review the **Data preview**  to ensure you didn't include **day_of_week** then, select **Close**.

    1. Select  **Next**.

## Configure run

After you load and configure your data, you can set up your experiment. This setup includes experiment design tasks such as, selecting the size of your compute environment and specifying what column you want to predict. 

1. Select the **Create new** radio button.

1. Populate the **Configure Run** form as follows:
    1. Enter this experiment name: `my-1st-automl-experiment`

    1. Select **y** as the target column, what you want to predict. This column indicates whether the client subscribed to a term deposit or not.
    
    1. Select **+Create a new compute** and configure your compute target. A compute target is a local or cloud-based resource environment used to run your training script or host your service deployment. For this experiment, we use a cloud-based compute. 
        1. Populate the **Virtual Machine** form to set up your compute.

            Field | Description | Value for tutorial
            ----|---|---
            Virtual&nbsp;machine&nbsp;priority |Select what priority your experiment should have| Dedicated
            Virtual&nbsp;machine&nbsp;type| Select the virtual machine type for your compute.|CPU (Central Processing Unit)
            Virtual&nbsp;machine&nbsp;size| Select the virtual machine size for your compute. A list of recommended sizes is provided based on your data and experiment type. |Standard_D2_v2
        
        1. Select **Next** to populate the **Configure settings form**.
        
            Field | Description | Value for tutorial
            ----|---|---
            Compute name |	A unique name that identifies your compute context. | cpu-cluster
            Min / Max nodes| To profile data, you must specify 1 or more nodes.|Min nodes: 0<br>Max nodes: 4
            Idle seconds before scale down | Idle time before  the cluster is automatically scaled down to the minimum node count.|120 (default)
            Advanced settings | Settings to configure and authorize a virtual network for your experiment.| None               

        > If you see an error, please lower the max node down to 1.
        > ![insufficient-quota](../images/insufficient-quota.png)

        1. Select **Create** to create your compute target. 

            **This takes a couple minutes to complete.** 

             ![Settings page](../images/compute-settings.png)

        2. After creation, select your new compute target from the drop-down list.

    2. Select **Next**.

2. On the **Task type and settings** form, complete the setup for your automated ML experiment by specifying the machine learning task type and configuration settings.
    
    1.  Select **Classification** as the machine learning task type.

    2. Select **View additional configuration settings** and populate the fields as follows. These settings are to better control the training job. Otherwise, defaults are applied based on experiment selection and data. 
        > To control training time, set the training job time at exit criterion **0.25 (hour)**.

        Additional&nbsp;configurations|Description|Value&nbsp;for&nbsp;tutorial
        ------|---------|---
        Primary metric| Evaluation metric that the machine learning algorithm will be measured by.|AUC_weighted
        Explain best model| Automatically shows explainability on the best model created by automated ML.| Enable
        Blocked algorithms | Algorithms you want to exclude from the training job| None
        Exit criterion| If a criteria is met, the training job is stopped. |Training&nbsp;job&nbsp;time (hours): 0.25 <br> Metric&nbsp;score&nbsp;threshold: None
        Validation | Choose a cross-validation type and number of tests.|Validation type:<br>&nbsp;k-fold&nbsp;cross-validation <br> <br> Number of validations: 2
        Concurrency| The maximum number of parallel iterations executed per iteration| Max&nbsp;concurrent&nbsp;iterations: 4
        
        Select **Save**.
    
3. Select **Finish** to run the experiment. The **Run Detail**  screen opens with the **Run status** at the top as the experiment preparation begins. This status updates as the experiment progresses. Notifications also appear in the top right corner of the studio, to inform you of the status of your experiment.

> Preparation takes **10-15 minutes** to prepare the experiment run.
> Once running, it takes **2-3 minutes more for each iteration**.
>
> In production, you'd likely walk away for a bit. But for this tutorial, we suggest you start exploring the tested algorithms on the **Models** tab as they complete while the others are still running. 

##  Explore models

Navigate to the **Models** tab to see the algorithms (models) tested. By default, the models are ordered by metric score as they complete. For this tutorial, the model that scores the highest based on the chosen **AUC_weighted** metric is at the top of the list.

While you wait for all of the experiment models to finish, select the **Algorithm name** of a completed model to explore its performance details. 

The following navigates through the **Details** and the **Metrics** tabs to view the selected model's properties, metrics, and performance charts. 

![Run iteration detail](../images/run-detail.gif)

## Model explanations

While you wait for the models to complete, you can also take a look at model explanations and see which data features (raw or engineered) influenced a particular model's predictions. 

These model explanations can be generated on demand, and are summarized in the model explanations dashboard  that's part of the **Explanations (preview)** tab.

To generate model explanations, 
 
1. Select **Run 1** at the top to navigate back to the **Models** screen. 
1. Select the **Models** tab.
1. For this tutorial, select the first **MaxAbsScaler, LightGBM** model.
1. Select the **Explain model** button at the top. On the right, the **Explain model** pane appears. 
1. Select the **automl-compute** that you created previously. This compute cluster initiates a child run to generate the model explanations.
1. Select **Create** at the bottom. A green success message appears towards the top of your screen. 
    > The explainability run takes about 2-5 minutes to complete.
1. Select the **Explanations (preview)** button. This tab populates once the explainability run completes.
1. On the left hand side, expand the pane and select the row that says **raw** under **Features**. 
1. Select the **Aggregate feature importance** tab on the right. This chart shows which data features influenced the predictions of the selected model. 

    In this example, the *duration* appears to have the most influence on the predictions of this model.
    
    ![Model explanation dashboard](../images/model-explanation-dashboard.png)

## Discussion

In this automated machine learning tutorial, you used Azure Machine Learning's automated ML interface to create and deploy a classification model. See these articles for more information and next steps:

* For more information on classification metrics and charts, see the [Understand automated machine learning results](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-understand-automated-ml) article.
* Learn more about [featurization](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-features).


> The **Bank Marketing** dataset is made available under the [Creative Commons (CCO: Public Domain) License](https://creativecommons.org/publicdomain/zero/1.0/). Any rights in individual contents of the database are licensed under the [Database Contents License](https://creativecommons.org/publicdomain/zero/1.0/) and available on [Kaggle](https://www.kaggle.com/janiobachmann/bank-marketing-dataset). This dataset was originally available within the [UCI Machine Learning Database](https://archive.ics.uci.edu/ml/datasets/bank+marketing).
>
> [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014.

---

[Go back to main page](https://github.com/hyssh/mtc-open-workshop)
