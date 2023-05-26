from dagster_dbt import load_assets_from_dbt_project
from dagster import file_relative_path
import boto3

DBT_PROJECT_PATH = file_relative_path(__file__, "../../surf_l201")
DBT_PROFILES = file_relative_path(__file__, "../../surf_l201")

# download profiles.yml
bucket = "delfi-clindev"
s3_file = "cds-pipeline-data/dev/profiles.yml"
local_file = DBT_PROFILES + "/profiles.yml"
s3 = boto3.client("s3")
s3.download_file(bucket, s3_file, local_file)

# define dbt assets
dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES, key_prefix=["staging"]
)
