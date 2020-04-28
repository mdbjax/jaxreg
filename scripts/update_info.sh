#!/bin/bash

while read name version size; do
	docker exec sregistry_db_1 psql -U postgres -c "update main_container set size='${size}' where name like '${name}' and version='${version}';" 
done < update_info
