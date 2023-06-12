{{ config(materialized='external') }}

select * from {{ source("external_source", "raw") }}