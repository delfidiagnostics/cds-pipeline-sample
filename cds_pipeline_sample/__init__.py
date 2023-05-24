import os

from dagster_dbt import DbtCliClientResource
from cds_pipeline_sample import assets
from cds_pipeline_sample.assets import DBT_PROFILES, DBT_PROJECT_PATH

from dagster import Definitions, load_assets_from_modules

resources = {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES,
    ),
}

defs = Definitions(assets=load_assets_from_modules([assets]), resources=resources)
