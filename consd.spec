Summary:	Virtual Console Management Daemon
Summary(pl):	Menad¿er konsoli
Name:		consd
Version:	1.3
Release:	1
Copyright:	GPL
Group:		System
Group(pl):	System
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tgz
#Patch0:		
#BuildRequires:	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description

%description -l pl

%prep
%setup -q

#%patch

%build
#./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
