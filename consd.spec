Summary:	Virtual console management daemon
Summary(pl):	Zarz±dca wirtualnych konsol
Name:		consd
Version:	1.5.2
Release:	1
License:	GPL
Group:		Daemons
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tgz
# Source0-md5:	54268011070aa9a78295762c35346dea
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual console management daemon - starts and kills gettys as needed
(depending on the amount of currently idle gettys). Runs automatically
in the background. Can coexist with gettys started by init. There's
also a helper daemon that can display what process is running on the
current console.

%description -l pl
Jest to program zarz±dzaj±cy wirtualnymi konsolami - uruchamia i
zabija getty w razie potrzeby (w zale¿no¶ci od ilo¶ci nieaktywnych
getty). Dzia³a automatycznie w tle. Mo¿e wspó³istnieæ z getty
uruchomionymi przez inita. Zawiera tak¿e pomocniczego demon, który
mo¿e wy¶wietlaæ, jaki proces jest uruchomiony na aktualnej konsoli.

%prep
%setup -q

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install consd consinfod $RPM_BUILD_ROOT%{_sbindir}
install consd.8 consinfod.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*
