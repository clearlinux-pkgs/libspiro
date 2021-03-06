#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libspiro
Version  : 20200505
Release  : 4
URL      : https://github.com/fontforge/libspiro/archive/20200505/libspiro-20200505.tar.gz
Source0  : https://github.com/fontforge/libspiro/archive/20200505/libspiro-20200505.tar.gz
Summary  : A library for curve design. Clothoid to bezier conversion. A mechanism for drawing smooth contours with constant curvature at the spline joins.
Group    : Development/Tools
License  : GPL-3.0
Requires: libspiro-lib = %{version}-%{release}
Requires: libspiro-license = %{version}-%{release}
BuildRequires : sed
BuildRequires : valgrind

%description
LibSpiro is a shared library designed to give programs the ability to create
smooth continuous curves based on a given set of codes and X,Y constraints.

%package dev
Summary: dev components for the libspiro package.
Group: Development
Requires: libspiro-lib = %{version}-%{release}
Provides: libspiro-devel = %{version}-%{release}
Requires: libspiro = %{version}-%{release}

%description dev
dev components for the libspiro package.


%package lib
Summary: lib components for the libspiro package.
Group: Libraries
Requires: libspiro-license = %{version}-%{release}

%description lib
lib components for the libspiro package.


%package license
Summary: license components for the libspiro package.
Group: Default

%description license
license components for the libspiro package.


%prep
%setup -q -n libspiro-20200505
cd %{_builddir}/libspiro-20200505

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617659427
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1617659427
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libspiro
cp %{_builddir}/libspiro-20200505/COPYING %{buildroot}/usr/share/package-licenses/libspiro/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/bezctx.h
/usr/include/bezctx_intf.h
/usr/include/spiro.h
/usr/include/spiroentrypoints.h
/usr/lib64/libspiro.so
/usr/lib64/pkgconfig/libspiro.pc
/usr/share/man/man3/libspiro.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libspiro.so.1
/usr/lib64/libspiro.so.1.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libspiro/8624bcdae55baeef00cd11d5dfcfa60f68710a02
