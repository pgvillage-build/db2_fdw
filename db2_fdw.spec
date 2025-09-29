%global _prefix /usr/local
Summary: PostgreSQL {{ pgversion }} db2 foreign data wrapper
Name: postgresql{{ pgversion }}-db2_fdw
Version: {{ version }}
Release: 1%{?dist}
License: PostgreSQL License
Group: Applications/Databases
Url: https://github.com/wolfgangbrandl/db2_fdw
%undefine _disable_source_fetch
Source0: https://github.com/wolfgangbrandl/db2_fdw/archive/refs/tags/{{ version}}.tar.gz
BuildArch: x86_64


%description
db2_fdw is a PostgreSQL extension that provides a Foreign Data Wrapper for easy and efficient
access to DB2 databases, including pushdown of WHERE conditions and required columns as well
as comprehensive EXPLAIN support.

%install
mkdir -p %{buildroot}/%{_bindir}
tar -xvf %{_sourcedir}/{{ version}}.tar.gz
cd {{ version }}
make
make install DESTDIR=$RPM_BUILD_ROOT
%{__install} -m 0755 %{_builddir}/usr/pgsql-17/lib/db2_fdw.so                      %{buildroot}/usr/pgsql-17/lib/db2_fdw.so
%{__install} -m 0644 %{_builddir}/usr/pgsql-17/lib/bitcode/db2_fdw/*               %{buildroot}/usr/pgsql-17/lib/bitcode/db2_fdw/
%{__install} -m 0644 %{_builddir}/usr/pgsql-17/share/extension/db2_fdw*            %{buildroot}/usr/pgsql-17/share/extension/
%{__install} -m 0644 %{_builddir}/usr/pgsql-17/share/extension/uninstall_db2_fdw*  %{buildroot}/usr/pgsql-17/share/extension/
%{__install} -m 0644 %{_builddir}/usr/pgsql-17/doc/extension/db2_fdw.md            %{buildroot}/usr/pgsql-17/doc/extension/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{buildroot}/usr/pgsql-17/lib/db2_fdw.so
%{buildroot}/usr/pgsql-17/lib/bitcode/db2_fdw/*
%{buildroot}/usr/pgsql-17/share/extension/db2_fdw*
%{buildroot}/usr/pgsql-17/share/extension/uninstall_db2_fdw*
%{buildroot}/usr/pgsql-17/doc/extension/db2_fdw.md
