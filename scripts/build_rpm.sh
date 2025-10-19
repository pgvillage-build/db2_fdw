#!/bin/bash
set -ex
export PATH=$PATH:/usr/pgsql-17/bin
cd /host/db2_fdw
make clean

PGVERSION=$(pg_config --version | grep -oE '[0-9.]+')
PGMAJOR=${PGVERSION%.*}
FDW_MAJOR=$(git describe --tags --abbrev=0)
echo %pgversion $PGMAJOR >> ~/.rpmmacros
echo %fdw_version ${FDW_MAJOR} >> ~/.rpmmacros

rpmbuild -ba /host/db2_fdw.spec
cp ~/rpmbuild/RPMS/x86_64/postgresql*-db2_fdw-*.rpm /host/rpms/
