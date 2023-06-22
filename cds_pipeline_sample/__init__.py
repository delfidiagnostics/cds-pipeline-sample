import os
from dagster_dbt import DbtCliClientResource
from dagster import (
    ScheduleDefinition,
    define_asset_job,
    Definitions,
    load_assets_from_modules,
)
from cds_pipeline_sample import assets
from cds_pipeline_sample.assets import DBT_PROFILES, DBT_PROJECT_PATH

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

# if you want to debug locally without running a dagit instance, you can uncomment the following
if __name__ == "__main__":
    _result = defs.get_job_def("run_everything").execute_in_process()
    local_file = DBT_PROFILES + "/profiles.yml"
    os.remove(local_file)
