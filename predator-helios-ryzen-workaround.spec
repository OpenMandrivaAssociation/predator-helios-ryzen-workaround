Summary:	Workaround for a BIOS Bug in Acer Predator Helios 500 Ryzen laptops
Name:		predator-helios-ryzen-workaround
Version:	1.0
Release:	3
Source0:	https://raw.githubusercontent.com/pastaq/Acer-Ryzen-Helios-AC-Fix/master/acfix.service
Source1:	https://raw.githubusercontent.com/pastaq/Acer-Ryzen-Helios-AC-Fix/master/acfix.sh
ExclusiveArch:	%{x86_64}
License:	BSD-like
BuildRequires:	systemd-rpm-macros

%description
Workaround for a BIOS Bug in Acer Predator Helios 500 Ryzen laptops

Install this package if (and only if) you're using an Acer Predator
Helios 500 with a Ryzen CPU and Vega GPU.

%prep

%build

%install
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_unitdir}
install -c -m 755 %{S:1} %{buildroot}%{_sbindir}/%{name}
sed -e 's,/usr/local/sbin/acfix.sh,%{_sbindir}/%{name},g' %{S:0} >%{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}

%postun
%systemd_postun %{name}

%files
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
