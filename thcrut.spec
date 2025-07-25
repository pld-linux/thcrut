Summary:	THC-RUT gathers informations from local and remote networks
Summary(pl.UTF-8):	THC-RUT - zbieranie informacji z sieci zdalnych i lokalnych
Name:		thcrut
Version:	1.2.5
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.thc.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	190f08ce6839aecb0fa0ce8d5ddd09ee
Patch0:		%{name}-libnet.patch
URL:		http://thc.org/thc-rut/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnet1-devel
BuildRequires:	libpcap-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
THC-RUT offers a wide range of network discovery utilities like ARP
lookup on an IP range, spoofed DHCP request, RARP, BOOTP, ICMP-ping,
ICMP address mask request, OS fingerprinting, high-speed host
discovery, ...

%description -l pl.UTF-8
THC-RUT oferuje takie narzędzia do rozpoznawania sieci jak zapytania
ARP zakresu IP, spoofowane żądania DHCP, RARP, BOOTP, ICMP-ping,
ICMP, OS fingerprinting, szybkie wykrywanie hostów...

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
