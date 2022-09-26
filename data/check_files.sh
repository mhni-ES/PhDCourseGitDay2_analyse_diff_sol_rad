#! /bin/bash

for file in diffuse_sol_rad/*.csv
do
  year=`echo $file | grep -oP "(?<=r)20[0-9]{2}"` ## only works in linux since -P option for perl is not supported on mac.
  echo $year
  grep -c "$year,[0-9]\{1,2\},1" $file
done

