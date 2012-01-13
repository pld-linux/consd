Summary:	Virtual console management daemon
Summary(pl.UTF-8):	Zarządca wirtualnych konsol
Name:		consd
Version:	1.5.8
Release:	1
License:	GPL
Group:		Daemons
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tgz
# Source0-md5:	6a18c17650286f9426d308b29a46e258
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual console management daemon - starts and kills gettys as needed
(depending on the amount of currently idle gettys). Runs automatically
in the background. Can coexist with gettys started by init. There's
also a helper daemon that can display what process is running on the
current console.

%description -l pl.UTF-8
Jest to program zarządzający wirtualnymi konsolami - uruchamia i
zabija getty w razie potrzeby (w zależności od ilości nieaktywnych
getty). Działa automatycznie w tle. Może współistnieć z getty
uruchomionymi przez inita. Zawiera także pomocniczego demona, który
może wyświetlać, jaki proces jest uruchomiony na aktualnej konsoli.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install consd consinfod $RPM_BUILD_ROOT%{_sbindir}
install consd.8 consinfod.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*
