#!/bin/bash

manifest_file="GSA-24v3-0_A1_manifest.csv"

map_rsid_file="GSA-24v3-0_A1_b151_rsids.txt"

#manifest file first 8 lines not needed, extract using tail to GSA-24v3-0_A1_manifest_processed.csv file

tail -n+9 GSA-24v3-0_A1_manifest_processed.csv | awk -F ',' '{print $1,$2,$4,$9,$10,$14}' > minimal_GSA-24v3-0_A1_manifest.csv #minimal info for mapping

#then get rsid using the ID mapping. The rsid containing file has a header, remove the header to run the command below

awk '(NR==FNR){arr[$2];next} { if ($1 in arr && $2!=".") {print $2} else  {print $1} }' minimal_GSA-24v3-0_A1_manifest.csv GSA-24v3-0_A1_b151_rsids.txt > mapped_GSA-24v3-0_A1_manifest.rsids

# download PGS for colorectal cancer from PGS catelogue
