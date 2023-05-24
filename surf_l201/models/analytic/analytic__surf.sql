
with samples as (select * from {{ ref("stg_lims__l201") }})
select
    'LIMS' as source,
    lower(split_part(study_id, ' ', 1)) as study,
    study_site_name as site_number,
    external_participant_id as subject_id,
    lower(split_part(study_id, ' ', 1))
    || '-'
    || external_participant_id as usubject_id,
    specimen_type as matrix,
    case
        when specimen_type = 'Streck DNA Plasma'
        then 'DNA'
        when specimen_type = 'Streck RNA Plasma'
        then 'RNA'
        else 'ERROR'
    end as tube_matrix,
    null as htp_id,
    null as tube_type,
    external_sample_id as tube_barcode_id,
    null as tube_suffix,
    spin2_child_sample_id as aliquot_barcode_id,
    spin2_child_sample_id as sample_id,
    null as aliquot_suffix,
    null as status,
    preprocessed_blood_volume,
    spin2_volume as volume_ml,
    hemolysis_rating,
    null as hemolysis_raw,
    case
        when
            preprocessed_blood_volume >= 5
            and round(extract(epoch from (spin1_date - collection_date)) / 86400) <= 7
        then 'Yes'
        else 'No'
    end as streck_ifu,
    null as processing_method,
    null as processing_technician_identifier,
    null as work_instruction_version,
    spin1_instruments as centrifuge_1_id,
    spin2_instruments as centrifuge_2_id,
    cast(collection_date as date) as date_of_collection,
    null as date_of_receipt,
    cast(spin1_date as date) as date_of_processing,
    null as date_of_storage,
    null as date_of_storage_removal,
    collection_date as datetime_of_collection,
    spin1_date as datetime_of_first_centrifuge,
    round(
        extract(epoch from (spin1_date - collection_date)) / 86400
    ) as duration_collection_processing,
    null as last_updated,
    null as restricted_aliquot,
    null as manual_volume,
    'tempbox' as box_id,
    'templocation' as location,
    external_kit_id as kit_barcode_id,
    sample_id as lims_sampleid,
    participant_id as lims_participantid
from samples
