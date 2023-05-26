import os

import boto3
from dagster_dbt import DbtCliClientResource
from dagster import (
    ScheduleDefinition,
    graph,
    define_asset_job,
    Definitions,
    load_assets_from_modules,
    op,
)

from cds_pipeline_sample import assets
from cds_pipeline_sample.assets import DBT_PROFILES, DBT_PROJECT_PATH


# op definition for downloading profiles.yml
@op
def download_profiles_file_from_s3(context):
    bucket = "delfi-clindev"
    s3_file = "cds-pipeline-data/dev/profiles.yml"
    local_file = DBT_PROFILES + "/profiles.yml"
    s3 = boto3.client("s3")
    s3.download_file(bucket, s3_file, local_file)
    context.log.info(f"Downloaded {s3_file} from S3 to {local_file}")


# op definition for delete profiles.yml
@op
def delete_profiles_file(context):
    local_file = DBT_PROFILES + "/profiles.yml"
    if os.path.isfile(local_file):
        os.remove(local_file)

    context.log.info(f"Deleted {local_file}")


# define resources
resources = {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES,
    ),
}


# define jobs
run_everything_job = define_asset_job("run_everything", selection="*")


defs = Definitions(
    assets=load_assets_from_modules([assets]),
    schedules=[
        ScheduleDefinition(
            job=run_everything_job,
            cron_schedule="@daily",
        ),
    ],
    resources=resources,
)

# If you want to debug locally without running a dagit instance, you can uncomment the following.
# This runs the load_all_job job which runs all assets.
if __name__ == "__main__":
    _result = defs.get_job_def("run_everything").execute_in_process()
