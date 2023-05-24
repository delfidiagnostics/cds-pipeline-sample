
with
    source as (select * from {{ source("staging", "raw_lims") }}),
    renamed as (
        select
            {{ adapter.quote("sampleId") }} as sample_id,
            {{ adapter.quote("sampleTypeId") }} as sample_type_id,
            cast({{ adapter.quote("hemolysisRating") }} as int) as hemolysis_rating,
            cast({{ adapter.quote("collectionDate") }} as timestamp) as collection_date,
            {{ adapter.quote("externalSampleId") }} as external_sample_id,
            case
                when {{ adapter.quote("specimenType") }} = 'Camo Streck Tube'
                then 'Streck DNA Plasma'
                when {{ adapter.quote("specimenType") }} = 'Red Streck Tube'
                then 'Streck RNA Plasma'
                else 'ERROR'
            end as specimen_type,
            {{ adapter.quote("preprocessed_blood_volume") }}
            as preprocessed_blood_volume,
            {{ adapter.quote("volumeUnits") }} as volume_units,
            {{ adapter.quote("quality") }} as quality,
            {{ adapter.quote("studyId") }} as study_id,
            {{ adapter.quote("studySiteId") }} as study_site_id,
            {{ adapter.quote("studySiteName") }} as study_site_name,
            {{ adapter.quote("subjectId") }} as subject_id,
            {{ adapter.quote("participantId") }} as participant_id,
            {{ adapter.quote("externalParticipantId") }} as external_participant_id,
            {{ adapter.quote("kitId") }} as kit_id,
            {{ adapter.quote("externalKitId") }} as external_kit_id,
            {{ adapter.quote("kitCreationDate") }} as kit_creation_date,
            {{ adapter.quote("spin1ChildSampleId") }} as spin1_child_sample_id,
            cast({{ adapter.quote("spin1Date") }} as timestamp) as spin1_date,
            {{ adapter.quote("spin1Instruments") }} as spin1_instruments,
            {{ adapter.quote("spin2ChildSampleId") }} as spin2_child_sample_id,
            {{ adapter.quote("spin2Volume") }} as spin2_volume,
            {{ adapter.quote("spin2Location") }} as spin2_location,
            cast({{ adapter.quote("spin2Date") }} as date) as spin2_date,
            {{ adapter.quote("spin2Instruments") }} as spin2_instruments

        from source
    )
select *
from renamed
