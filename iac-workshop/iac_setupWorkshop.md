# Setup AML Workshop 

## Goal 

- Setup Azure ML workspace and components

## Tasks

    1. Create resources in Azure


### 1. Create resources in Azure

To create resources you need Owner role or Contributor role. If you don't have one of role you can't run the script. So make sure you have proper role. 

- Go to [Azure Portal](https://portal.azure.com) and open __Cloud Shell__
    
    ![cloudshell](../images/cloudshell.png)

- Change directory to `$HOME/clouddrive'
    > Note: This is cloudshell path.

    ```bash
    cd $HOME/clouddrive
    ```

- Run following command to clone repo
    ```bash
    git clone https://github.com/hyssh/mtc-open-workshop.git
    ```
- Change directory to `$HOME/clouddrive/mtc-open-workshop/iac-workshop/`
- Run `iac_mlopsworkshop.azcli`

    1. Read message carefully and hit `Enter` key to move next step.
        ![](../images/run_mlopsworkshop_azcli000.png)

    1. Type your Subscription Name. Note that it's __CaSE SeNSiTivE__.
        ![](../images/run_mlopsworkshop_azcli001.png)

    1. Type region where you want to create the resources. Default region is `westus2`.
        ![](../images/run_mlopsworkshop_azcli002.png)
    
    1. The script will run 5 to 7 mintues.
        > Note that this script will create SP (Service Principal) under scope of your resource group.
        >
        > Save the Service Principal `ClientID(AppId)`, `Password` in a safe place

        ![](../images/run_mlopsworkshop_azcli003.png)

> IMPORTANT: If this script failed, you can't do following labs.
>
> Reach out to CSA to get help. 

---

## [HOME](https://github.com/hyssh/mtc-open-workshop)