Summary:	Virtual Console Management Daemon
Summary(pl):	Menad¿er wirtualnej konsoli
Name:		consd
Version:	1.3
Release:	1
License:	GPL
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tgz
Patch0:		%{name}-errno.patch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual console management daemon - starts and kills gettys as needed
(depending on the amount of currently idle gettys). Runs automatically
in the background. Can coexist with gettys started by init. There's
also a helper daemon that can display what process is running on the
current console.

%description -l pl
Menad¿er wirtualnej konsoli - startuje i zabija getty w razie potrzeby
(w zale¿no¶ci od ilo¶ci nieaktywnych getty). Dzia³a automatycznie w
tle. Mo¿e koegzystowaæ z getty uruchomionymi przez inita. Jest tak¿e
pomocniczy demon, który mo¿e wy¶wietlaæ, jaki proces jest uruchomiony
na aktualnej konsoli.

%prep
%setup -q
%patch -p1

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install consd consinfod $RPM_BUILD_ROOT%{_sbindir}
install consd.8 consinfod.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*
