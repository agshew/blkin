Name:		blkin
Version:	0.1
Release:	1%{?dist}
Summary:	blkin is a Dapper-style tracing library to be used with Zipkin

Group:		Development/Libraries
License:	BSD
URL:		https://github.com/marioskogias/blkin
Source0:	blkin-%{version}.tgz
Patch0:		blkin-make.patch
Provides:	libblkin-front.so()(64bit), libzipkin-cpp.so()(64bit)

BuildRequires:	boost-devel, lttng-ust-devel
#Requires:	

%description
blkin is a C/C++ library that enables you to get traces from C/C++ applications
according to the tracing semantics mentioned in the Dapper paper and
implemented in Zipkin

As a tracing backend blkin uses LTTng


%package devel
Summary:	blkin library headers and development files
Group:		Development/Libraries

%description devel
Support for developing programs using the blkin tracing library

%prep
%setup -q
%patch0 -p 1


%build
make %{?_smp_mflags}


%install
%{__mkdir_p} %{buildroot}%{_prefix}/lib
%{__mkdir_p} %{buildroot}%{_includedir}/%{name}
make install prefix=%{_prefix} DESTDIR=%{buildroot}
%{__mv} %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
%{__mv} %{buildroot}%{_includedir}/*.h* %{buildroot}%{_includedir}/%{name}


%files
%doc README.md
%doc COPYRIGHT
%{_libdir}/libblkin-front.*
%{_libdir}/libzipkin-c.*
%{_libdir}/libzipkin-cpp.*

%files devel
%{_includedir}/blkin/blkin-front.h
%{_includedir}/blkin/zipkin_c.h
%{_includedir}/blkin/zipkin_trace.h
%{_includedir}/blkin/ztracer.hpp

%changelog
* Mon Nov 3 2014 Andrew Shewmaker <agshe@gmail.com> 0.1
- Initial packaging
