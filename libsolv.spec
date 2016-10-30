#
# Conditional build:
%bcond_without	static_libs	# static libraries
%bcond_without	python3		# Python 3.x bindings
%bcond_without	ruby		# Ruby bindings
%bcond_without	tcl		# Tcl bindings

%include	/usr/lib/rpm/macros.perl
Summary:	Package dependency solver
Summary(pl.UTF-8):	Biblioteka do rozwiązywania zależności pakietów
Name:		libsolv
Version:	0.6.23
Release:	2
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/openSUSE/libsolv/releases
Source0:	https://github.com/openSUSE/libsolv/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	80098e081712368d38ade6affb39dd65
Patch0:		ruby.patch
Patch1:		%{name}-python.patch
URL:		https://github.com/openSUSE/libsolv
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.4
BuildRequires:	db-devel
BuildRequires:	expat-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2
%{?with_python3:BuildRequires:	python3-devel >= 3}
BuildRequires:	rpm-devel >= 5
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	swig-perl
BuildRequires:	swig-python
%{?with_tcl:BuildRequires:	swig-tcl}
BuildRequires:	tar >= 1:1.22
%{?with_tcl:BuildRequires:	tcl-devel}
BuildRequires:	xz
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
%if %{with ruby}
BuildRequires:	rpm-rubyprov
BuildRequires:	ruby-devel
BuildRequires:	swig-ruby
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free package dependency solver using a satisfiability algorithm. The
library is based on two major, but independent, blocks:

- Using a dictionary approach to store and retrieve package and
  dependency information.

- Using satisfiability, a well known and researched topic, for
  resolving package dependencies.

%description -l pl.UTF-8
Wolnodostępna biblioteka do rozwiązywania zależności pakietów przy
użyciu algorytmu spełnialności. Biblioteka jest podzielona na dwa
główne, niezależne bloki:

- wykorzystanie podejścia słownikowego do przechowywania i odtwarzania
  informacji o pakietach i zależnościach,

- wykorzystanie spełnialności - dobrze znanego i zbadanego tematu do
  rozwiązywania zależności pakietów.

%package devel
Summary:	Header files for libsolv libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libsolv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	rpm-devel >= 5

%description devel
Development files for libsolv.

%description devel -l pl.UTF-8
Pliki programistyczne biblioetk libsolv.

%package static
Summary:	Static libsolv libraries
Summary(pl.UTF-8):	Statyczne biblioteki libsolv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsolv libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libsolv.

%package tools
Summary:	Package dependency solver tools
Summary(pl.UTF-8):	Narzędzia do rozwiązywania zależności pakietów
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2
Requires:	coreutils
Requires:	gzip

%description tools
Package dependency solver tools.

%description tools -l pl.UTF-8
Narzędzia do rozwiązywania zależności pakietów.

%package -n perl-solv
Summary:	Perl bindings for the libsolv libraries
Summary(pl.UTF-8):	Wiązania Perla do bibliotek libsolv
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-solv
Perl bindings for the libsolv libraries.

%description -n perl-solv -l pl.UTF-8
Wiązania Perla do bibliotek libsolv.

%package -n python-solv
Summary:	Python 2.x bindings for the libsolv library
Summary(pl.UTF-8):	Wiązania Pythona 2.x do bibliotek libsolv
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-libs

%description -n python-solv
Python 2.x bindings for the libsolv library.

%description -n python-solv -l pl.UTF-8
Wiązania Pythona 2.x do bibliotek libsolv.

%package -n python3-solv
Summary:	Python 3.x bindings for the libsolv library
Summary(pl.UTF-8):	Wiązania Pythona 2.x do bibliotek libsolv
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-libs

%description -n python3-solv
Python 3.x bindings for the libsolv library.

%description -n python3-solv -l pl.UTF-8
Wiązania Pythona 3.x do bibliotek libsolv.

%package -n ruby-solv
Summary:	Ruby bindings for the libsolv libraries
Summary(pl.UTF-8):	Wiązania języka Ruby do bibliotek libsolv
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description -n ruby-solv
Ruby bindings for the libsolv libraries.

%description -n ruby-solv -l pl.UTF-8
Wiązania języka Ruby do bibliotek libsolv.

%package -n tcl-solv
Summary:	Tcl bindings for the libsolv libraries
Summary(pl.UTF-8):	Wiązania języka Tcl do bibliotek libsolv
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	tcl

%description -n tcl-solv
Tcl bindings for the libsolv libraries.

%description -n tcl-solv -l pl.UTF-8
Wiązania języka Tcl do bibliotek libsolv.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# use system one
%{__rm} cmake/modules/FindRuby.cmake

%build
install -d build %{?with_python3:build-py3}
cd build
%cmake .. \
	-DENABLE_APPDATA=ON \
	-DENABLE_BZIP2_COMPRESSION=ON \
	-DENABLE_HELIXREPO=ON \
	-DENABLE_LZMA_COMPRESSION=ON \
	-DENABLE_PERL=ON \
	-DENABLE_PUBKEY=ON \
	-DENABLE_PYTHON=ON \
	-DENABLE_RPMDB=ON \
	-DENABLE_RPMDB_BYRPMHEADER=ON \
	-DENABLE_RPMMD=ON \
	%{?with_ruby:-DENABLE_RUBY=ON} \
	%{?with_static_libs:-DENABLE_STATIC=ON} \
	%{?with_tcl:-DENABLE_TCL=ON} \
	-DPythonLibs_FIND_VERSION=2 \
	-DPythonLibs_FIND_VERSION_MAJOR=2 \
	-DRPM5=ON \
	-DUSE_VENDORDIRS=ON

%{__make}
%if %{with python3}
cd ../build-py3
%cmake .. \
	-DENABLE_APPDATA=ON \
	-DENABLE_BZIP2_COMPRESSION=ON \
	-DENABLE_LZMA_COMPRESSION=ON \
	-DENABLE_PUBKEY=ON \
	-DENABLE_PYTHON=ON \
	-DENABLE_RPMDB=ON \
	-DENABLE_RPMMD=ON \
	-DENABLE_RPMDB_BYRPMHEADER=ON \
	-DPythonLibs_FIND_VERSION=3 \
	-DPythonLibs_FIND_VERSION_MAJOR=3 \
	-DRPM5=ON

%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%{__make} -C build-py3/bindings/python install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS LICENSE.BSD NEWS README
%attr(755,root,root) %{_libdir}/libsolv.so.0
%attr(755,root,root) %{_libdir}/libsolvext.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsolv.so
%attr(755,root,root) %{_libdir}/libsolvext.so
%{_includedir}/solv
%{_pkgconfigdir}/libsolv.pc
%{_datadir}/cmake/Modules/FindLibSolv.cmake
%{_mandir}/man3/libsolv*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libsolv.a
%{_libdir}/libsolvext.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appdata2solv
%attr(755,root,root) %{_bindir}/deltainfoxml2solv
%attr(755,root,root) %{_bindir}/dumpsolv
%attr(755,root,root) %{_bindir}/helix2solv
%attr(755,root,root) %{_bindir}/installcheck
%attr(755,root,root) %{_bindir}/mergesolv
%attr(755,root,root) %{_bindir}/repo2solv.sh
%attr(755,root,root) %{_bindir}/repomdxml2solv
%attr(755,root,root) %{_bindir}/rpmdb2solv
%attr(755,root,root) %{_bindir}/rpmmd2solv
%attr(755,root,root) %{_bindir}/rpms2solv
%attr(755,root,root) %{_bindir}/testsolv
%attr(755,root,root) %{_bindir}/updateinfoxml2solv
%{_mandir}/man1/appdata2solv.1*
%{_mandir}/man1/deltainfoxml2solv.1*
%{_mandir}/man1/dumpsolv.1*
%{_mandir}/man1/helix2solv.1*
%{_mandir}/man1/installcheck.1*
%{_mandir}/man1/mergesolv.1*
%{_mandir}/man1/repomdxml2solv.1*
%{_mandir}/man1/rpmdb2solv.1*
%{_mandir}/man1/rpmmd2solv.1*
%{_mandir}/man1/rpms2solv.1*
%{_mandir}/man1/testsolv.1*
%{_mandir}/man1/updateinfoxml2solv.1*

%files -n perl-solv
%defattr(644,root,root,755)
%doc examples/p5solv
%attr(755,root,root) %{perl_vendorarch}/solv.so
%{perl_vendorarch}/solv.pm

%files -n python-solv
%defattr(644,root,root,755)
%doc examples/pysolv
%attr(755,root,root) %{py_sitedir}/_solv.so
%{py_sitedir}/solv.py[co]

%if %{with python3}
%files -n python3-solv
%defattr(644,root,root,755)
%doc examples/pysolv
%attr(755,root,root) %{py3_sitedir}/_solv.so
%{py3_sitedir}/solv.py
%endif

%if %{with ruby}
%files -n ruby-solv
%defattr(644,root,root,755)
%doc examples/rbsolv
%attr(755,root,root) %{ruby_vendorarchdir}/solv.so
%endif

%if %{with tcl}
%files -n tcl-solv
%defattr(644,root,root,755)
%doc examples/tclsolv
%attr(755,root,root) %{_prefix}/lib/tcl8/8.*/solv-%{version}.so
%{_prefix}/lib/tcl8/8.*/solv-%{version}.tm
%endif
