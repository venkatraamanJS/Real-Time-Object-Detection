import os,sys
import yaml
from signLanguage.utils.main_utils import read_yaml_file
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import ModelTrainerConfig
from signLanguage.entity.artifacts_entity import ModelTrainerArtifact
import subprocess


class ModelTrainer:
    def __init__(self,model_trainer_config: ModelTrainerConfig,):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            os.system("unzip Sign%20Language.v2i.yolov5pytorch.zip")
            os.system("rm Sign%20Language.v2i.yolov5pytorch.zip")
            os.system("git clone https://github.com/ultralytics/yolov5.git")

            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            config['nc'] = int(num_classes)


            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
            print("all computation are completed")
            print("***********************************")
            #os.system("rm -rf yolov5/.git")
            #os.system("rm -rf yolov5/runs")
            commands = ["rm -rf yolov5/.git","rm -rf yolov5/runs"]
            for command in commands:
                return_code = subprocess.call(command, shell=True)
                if return_code == 0:
                    print(f"Command '{command}' executed successfully.")
                else:
                    print(f"Command '{command}' failed with return code {return_code}.")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf valid")
            os.system("rm -rf README.roboflow.txt")
            os.system("rm -rf data.yaml")
            #os.system("cd yolov5")
            #os.system("rm  -rf .git")
            #os.system("cd ..")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise SignException(e, sys)


