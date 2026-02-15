# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-greenlet
Epoch: 100
Version: 3.2.4
Release: 1%{?dist}
Summary: Lightweight in-process concurrent programming
License: MIT
URL: https://github.com/python-greenlet/greenlet/tags
Source0: %{name}_%{version}.orig.tar.gz
Source99: %{name}.rpmlintrc
BuildRequires: fdupes
BuildRequires: gcc-c++
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools

%description
Greenlets are lightweight coroutines for in-process concurrent
programming.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} >= 1500
%package -n python%{python3_version_nodots}-greenlet
Summary: Lightweight in-process concurrent programming
Requires: python3
Provides: python3-greenlet = %{epoch}:%{version}-%{release}
Provides: python3dist(greenlet) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-greenlet = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(greenlet) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-greenlet = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(greenlet) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-greenlet
Greenlets are lightweight coroutines for in-process concurrent 
programming.

%package -n python%{python3_version_nodots}-greenlet-devel
Summary: C development headers for python-greenlet
Requires: python3-greenlet = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-greenlet-devel
This package contains header files required for C modules development.

%files -n python%{python3_version_nodots}-greenlet
%license LICENSE
%{python3_sitearch}/*

%files -n python%{python3_version_nodots}-greenlet-devel
%{_includedir}/*
%endif

%if !(0%{?suse_version} >= 1500)
%package -n python3-greenlet
Summary: Lightweight in-process concurrent programming
Requires: python3
Provides: python3-greenlet = %{epoch}:%{version}-%{release}
Provides: python3dist(greenlet) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-greenlet = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(greenlet) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-greenlet = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(greenlet) = %{epoch}:%{version}-%{release}

%description -n python3-greenlet
Greenlets are lightweight coroutines for in-process concurrent 
programming.

%package -n python3-greenlet-devel
Summary: C development headers for python-greenlet
Requires: python3-greenlet = %{epoch}:%{version}-%{release}

%description -n python3-greenlet-devel
This package contains header files required for C modules development.

%files -n python3-greenlet
%license LICENSE
%{python3_sitearch}/*

%files -n python3-greenlet-devel
%{_includedir}/*
%endif

%changelog
