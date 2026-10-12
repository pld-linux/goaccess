Summary:	Real-time web log analyzer and interactive viewer
Summary(pl.UTF-8):	Analizator logów serwera WWW działający w czasie rzeczywistym
Name:		goaccess
Version:	1.12
Release:	1
License:	MIT, Apache v2.0 (hogan.js), ISC (d3.js, topojson)
Group:		Networking/Utilities
Source0:	https://tar.goaccess.io/%{name}-%{version}.tar.gz
# Source0-md5:	cab0547c687eee584d83c1cce9b7989c
Patch0:		%{name}-conf.patch
Patch1:		%{name}-rdynamic.patch
URL:		https://goaccess.io/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	libmaxminddb-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
Suggests:	dbip-city-lite-GeoLite2-compat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GoAccess is a real-time web log analyzer and interactive viewer that
runs in a terminal or through a browser. It provides fast and
valuable HTTP statistics for system administrators that require a
visual server report on the fly.

%description -l pl.UTF-8
GoAccess to działający w czasie rzeczywistym analizator logów serwera
WWW. Wyniki można przeglądać interaktywnie w terminalu albo jako
raport HTML w przeglądarce WWW. Program szybko dostarcza statystyki
HTTP administratorom, którzy potrzebują na bieżąco czytelnego raportu
o pracy serwera.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-geoip=mmdb \
	--enable-utf8 \
	--with-getline \
	--with-openssl \
	--with-zlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md TODO
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/browsers.list
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/goaccess.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/podcast.list
%attr(755,root,root) %{_bindir}/goaccess
%{_mandir}/man1/goaccess.1*
