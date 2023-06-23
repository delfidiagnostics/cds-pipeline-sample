from os import environ
from dagster_dbt import load_assets_from_dbt_project
from dagster import file_relative_path
import boto3
import delfipypr as pypr

DBT_PROJECT_PATH = file_relative_path(__file__, "../../surf_l201")
DBT_PROFILES = file_relative_path(__file__, "../../surf_l201")

# set environ vars
ENV = environ.get('BUILD_VERSION', 'dev')

if ENV:
    AWS_KEYS = pypr.get_aws_secret("srv-clindev_keys")
    environ["AWS_ACCESS_KEY_ID"] = AWS_KEYS["AWS_ACCESS_KEY_ID"]
    environ["AWS_SECRET_ACCESS_KEY"] = AWS_KEYS["AWS_SECRET_ACCESS_KEY"]

# define dbt assets
dbt_assets = load_assets_from_dbt_project(  
    project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES, key_prefix=["staging"], node_info_to_group_fn=lambda k: "cds_pipeline_sample"
)
