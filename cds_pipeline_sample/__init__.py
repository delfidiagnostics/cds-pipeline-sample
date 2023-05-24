import os

from dagster_dbt import DbtCliClientResource
from cds_pipeline_sample import assets
from cds_pipeline_sample.assets import DBT_PROFILES, DBT_PROJECT_PATH
from dagster import ScheduleDefinition, define_asset_job, Definitions
from dagster import Definitions, load_assets_from_modules

run_everything_job = define_asset_job("run_everything", selection="*")

resources = {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES,
    ),
}

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