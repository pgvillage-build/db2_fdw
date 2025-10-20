FROM icr.io/db2_community/db2
ARG PGVERSION
ENV PGVERSION=${PGVERSION}
ENV LICENSE=accept
ENV DB2INST1_PASSWORD=testpwd
ENV DBNAME=test
ENV DB2_HOME=/opt/ibm/db2/V12.1
#RUN   dnf erase -y ksh && \
#      dnf update -y && \
RUN   dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm && \
      dnf -qy module disable postgresql && \
      dnf install -y postgresql${PGVERSION}-server postgresql${PGVERSION}-devel git rpm-build
ENTRYPOINT []
