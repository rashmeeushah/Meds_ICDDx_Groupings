# Meds_ICDDx_Groupings
This is the code to map the medication and ICD diagnoses hierarchies to more specific, clinically relevant groups. I have not created a virtual environment for this code, which was written using Python 3.7.

For medication grouping, 4_meds_group.py provides the Python script to create the groupings. The CATALOG_HIER_e2.xlsx file is the starting point to create the groups. This file is based on the medication hierarchy from a single health system and may not match with all health systems. The output from this script should includes the hieracrhy mapped to new groups, many of which are based on the existing hierarchy. Most changes occurred for cardiovascular-specific medications, since that is my area of interest. The file rx_names_mapped.csv provdes the mappings after I ran the code.
