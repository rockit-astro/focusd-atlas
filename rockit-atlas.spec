Name:      rockit-atlas
Version:   %{_version}
Release:   1%{dist}
Summary:   FLI Atlas focuser.
Url:       https://github.com/rockit-astro/atlasd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/focusd/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/focus %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/focusd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/focusd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/focus %{buildroot}/etc/bash_completion.d

%{__install} %{_sourcedir}/warwick.json %{buildroot}%{_sysconfdir}/focusd/

%package server
Summary:  Focuser control server.
Group:    Unspecified
Requires: python3-rockit-atlas libfli
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/focusd
%defattr(0644,root,root,-)
%{_unitdir}/focusd@.service

%package client
Summary:  Focuser control client.
Group:    Unspecified
Requires: python3-rockit-atlas
%description client

%files client
%defattr(0755,root,root,-)
%{_bindir}/focus
/etc/bash_completion.d/focus

%package data-warwick
Summary: Focuser data for Windmill Hill Observatory telescope
Group:   Unspecified
%description data-warwick

%files data-warwick
%defattr(0644,root,root,-)
%{_sysconfdir}/focusd/warwick.json

%changelog
