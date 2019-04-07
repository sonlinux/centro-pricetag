#!/bin/bash
MYDATE=`date +%d-%B-%Y`
MONTH=$(date +%B)
YEAR=$(date +%Y)
cd /home/data/changelog.pricetag.com/deployment
MYBASEDIR=`pwd`/backups
MYBACKUPDIR=${MYBASEDIR}/${YEAR}/${MONTH}
mkdir -p ${MYBACKUPDIR}

cd ${MYBACKUPDIR}
docker exec -ti pricetag-db /bin/bash -c "PGPASSWORD=docker pg_dump -Fc -f /tmp/latest.dmp -h localhost -U docker gis"
docker cp pricetag-db:/tmp/latest.dmp PG_pricetag-${MYDATE}.dmp

cd -
rm backups/latest.dmp

cd backups
ln -s ${MYBACKUPDIR}/PG_pricetag-${MYDATE}.dmp latest.dmp

cd ..
