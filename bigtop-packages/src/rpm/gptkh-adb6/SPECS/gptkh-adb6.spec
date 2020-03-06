%define debug_package %{nil}

Name: gptkh-adb6
Version: %{gptkh_adb6_version}
Release: %{gptkh_adb6_release}
Summary: Connection pool for Greenplum Database
Group: Development/Tools

Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
License:  Arenadata License
Source0: gptkh-adb6-%{gptkh_adb6_base_version}.tar.gz
Source1: do-component-build 
Source2: install_%{name}.sh
Source3: bigtop.bom

Requires: bash, gpdb
Provides: gptkh-adb6
Obsoletes: gptkh
AutoReqProv: no

%description 
gptkh-adb6 - is a Greenplum extension for "transaction-like" data loading into ClickHouse via PXF.

%prep
%setup -q -n %{name}-%{gptkh_adb6_base_version}

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{gptkh_adb6_base_version}


%files 
%attr(0755,root,root) /usr/lib/gpdb/lib/postgresql/*
%attr(0644,root,root) /usr/lib/gpdb/share/postgresql/extension/*
