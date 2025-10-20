#!/bin/bash
set -ex
export PATH="${PATH}:/usr/pgsql-${PGVERSION}/bin"
echo %pgversion "${PGVERSION}" >>~/.rpmmacros

git config --global --add safe.directory /host/db2_fdw
cd /host/db2_fdw
FDW_MAJOR=$(git describe --tags --abbrev=0)
echo %fdw_version "${FDW_MAJOR}" >>~/.rpmmacros

rpmbuild -ba /host/db2_fdw.spec

cp ~/rpmbuild/RPMS/x86_64/postgresql*-db2_fdw-*.rpm /host/rpms/
