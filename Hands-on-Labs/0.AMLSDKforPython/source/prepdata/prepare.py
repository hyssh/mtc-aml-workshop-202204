
import os
import argparse
from azureml.core import Dataset, Run

parser = argparse.ArgumentParser("prep")

parser.add_argument("--output_path", type=str, help="output data directory")

args = parser.parse_args()

print(os.environ)

run = Run.get_context()
ws = run.experiment.workspace

dataset = run.input_datasets['titanic']
df = dataset.to_pandas_dataframe()
df = df.drop(labels=['PassengerId', 'Name', 'Ticket', 'Fare', 'Embarked'], axis=1)

print(df)

os.makedirs(args.output_path)
df.to_csv(os.path.join(args.output_path, 'prepdTitanic.csv'))
