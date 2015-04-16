Name:           jansson
Summary:        Plain C JSON library
Version:        2.7
Release:        1
Group:          Applications/Native Applications
License:        GPL-3.0
URL:            http://www.tizen.org
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(capi-appfw-package-manager)

%define debug_package %{nil}

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description
Local JLR mirror for Jansson binaries.

%description devel
Local JLR mirror for Jansson development files.

%prep
%autosetup

%build
%reconfigure
make %{?_smp_mflags}

%install
%make_install

%check
make %{?_smp_mflags} check

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE
%doc README.rst
%{_libdir}/libjansson.so*

%files devel
%{_includedir}/jansson*.h
%{_libdir}/pkgconfig/jansson.pc
