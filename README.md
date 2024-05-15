# Real-Time-Object-Detection

## Workflows

- constants
- config_entity
- artifact_entity
- components
- pipeline
- app.py

## Project Configuration

```bash
#install aws cli from the following link

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

```bash
#Configure aws crediential (secret key & access key)

aws configure
```

```bash
#Create a s3 bucket for model pusher. name is mentioned in the consrtant

```



## How to run:

```bash
conda create -n signlang python=3.7 -y
```

```bash
conda activate signlang
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```






(Categories_huut) venkat@amtexs-MacBook-Pro Layers % aws configure --profile VenkatRam                                                                        
AWS Access Key ID [None]:  AKIA2QGELPGCJCXHBLYD                            
AWS Secret Access Key [None]: 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
Default region name [None]: ap-south-1
Default output format [None]: 
(Categories_huut) venkat@amtexs-MacBook-Pro Layers % export AWS_PROFILE=VenkatRam
export AWS_PROFILE=VenkatRam
aws s3 ls
